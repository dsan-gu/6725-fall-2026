"""Count class attendance from Slack roll-call channel exports.

Each class day, an instructor posts a greeting in the roll-call channel and
students react to it with an emoji. Export that day's messages as one JSON
file named YYYY-MM-DD.json. This script reads every such file in a folder,
marks a person present on a day if they reacted to or posted a message that
day, and writes a CSV with each person's netid, name, email, count, and
percentage.

Slack stores reactions as bare user IDs, so the script needs the users.json
file from a Slack workspace export to turn those IDs into netids and names.
"""

import argparse
import csv
import json
import logging
import time
from pathlib import Path
from typing import (
    Dict,
    List,
    Optional,
    Set,
    Tuple,
)


# Configure logging with basicConfig
logging.basicConfig(
    level=logging.INFO,  # Set the log level to INFO
    # Define log message format
    format="%(asctime)s,p%(process)s,{%(filename)s:%(lineno)d},%(levelname)s,%(message)s",
)
logger = logging.getLogger(__name__)


DAY_FILE_PATTERN: str = "????-??-??.json"
DEFAULT_OUTPUT_NAME: str = "attendance_summary.csv"
BUCKETS_OUTPUT_NAME: str = "attendance_buckets.csv"

# Attendance buckets as (label, lowest pct in the bucket), highest bucket first.
# A student goes in the first bucket whose lowest pct they meet.
BUCKETS: List[Tuple[str, float]] = [
    ("100", 100.0),
    ("90 to 100", 90.0),
    ("80 to 90", 80.0),
    ("50 to 80", 50.0),
    ("below 50", 0.0),
]
DEFAULT_USERS_FILE_NAME: str = "users.json"
CSV_HEADER: List[str] = [
    "slack_id",
    "netid",
    "name",
    "email",
    "days_present",
    "days_total",
    "pct",
]

# A person is stored as (netid, name, email).
Person = Tuple[str, str, str]
UNKNOWN_PERSON: Person = ("", "", "")


def _load_json(
    path: Path,
) -> list:
    """Read a JSON file that holds a list."""
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON list in {path}, got {type(data).__name__}")
    return data


def _pick_name(
    netid: str,
    real_name: str,
    display_name: str,
) -> str:
    """Pick the best human name for a user.

    Many students leave real_name set to their netid and put their actual
    name in display_name, so fall back to display_name in that case.
    """
    if real_name and real_name != netid:
        return real_name
    if display_name:
        return display_name
    return real_name


def _load_users(
    users_file: Path,
) -> Dict[str, Person]:
    """Map Slack user IDs to (netid, name, email) from a Slack users.json export.

    Bots and deleted accounts are skipped.
    """
    people: Dict[str, Person] = {}
    for user in _load_json(users_file):
        if user.get("is_bot") or user.get("deleted"):
            continue
        profile = user.get("profile", {})
        netid = user.get("name", "")
        real_name = user.get("real_name") or profile.get("real_name", "")
        name = _pick_name(netid, real_name, profile.get("display_name", ""))
        people[user["id"]] = (netid, name, profile.get("email", ""))
    logger.info(f"Loaded {len(people)} people from {users_file}")
    return people


def _load_roster(
    roster_file: Path,
) -> Dict[str, str]:
    """Map netid to name from a tab-separated roster (name, then netid)."""
    roster: Dict[str, str] = {}
    with roster_file.open(encoding="utf-8") as f:
        for line in f:
            columns = line.rstrip("\n").split("\t")
            if len(columns) < 2 or not columns[1].strip():
                continue
            roster[columns[1].strip()] = columns[0].strip()
    logger.info(f"Loaded {len(roster)} names from {roster_file}")
    return roster


def _fill_names_from_roster(
    people: Dict[str, Person],
    roster: Dict[str, str],
) -> None:
    """Replace names that are only a netid with the name from the roster."""
    for user_id, (netid, name, email) in people.items():
        if name and name != netid:
            continue
        if netid in roster:
            people[user_id] = (netid, roster[netid], email)
            logger.debug(f"Took name for {netid} from roster")


def _people_present(
    messages: List[dict],
) -> Set[str]:
    """Return the Slack user IDs that reacted to or posted a message."""
    present: Set[str] = set()
    for message in messages:
        for reaction in message.get("reactions", []):
            present.update(reaction.get("users", []))

        # Join and leave events have a subtype; real posts do not.
        if message.get("subtype") is None and message.get("user"):
            present.add(message["user"])
    return present


def _read_days(
    input_dir: Path,
) -> Dict[str, Set[str]]:
    """Read every day file and return the Slack user IDs present each day."""
    day_files = sorted(input_dir.glob(DAY_FILE_PATTERN))
    if not day_files:
        raise ValueError(
            f"No files matching {DAY_FILE_PATTERN} in {input_dir}. "
            "Export each class day's roll-call messages as YYYY-MM-DD.json."
        )

    present_by_day: Dict[str, Set[str]] = {}
    for day_file in day_files:
        messages = _load_json(day_file)
        present_by_day[day_file.stem] = _people_present(messages)
        logger.debug(f"{day_file.name}: {len(messages)} messages")
    return present_by_day


def _is_excluded(
    user_id: str,
    people: Dict[str, Person],
    exclude: Set[str],
) -> bool:
    """Return True if the user ID or its netid is in the exclude set."""
    if user_id in exclude:
        return True
    netid = people.get(user_id, UNKNOWN_PERSON)[0]
    return netid in exclude


def _days_present(
    user_id: str,
    present_by_day: Dict[str, Set[str]],
) -> int:
    """Count the days a user was present."""
    count = 0
    for present in present_by_day.values():
        if user_id in present:
            count += 1
    return count


def _write_csv(
    output_csv: Path,
    present_by_day: Dict[str, Set[str]],
    people: Dict[str, Person],
    user_ids: List[str],
) -> None:
    """Write one row per person with a 1/0 column for each day."""
    days = list(present_by_day)
    total = len(days)
    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER + days)
        for user_id in user_ids:
            netid, name, email = people.get(user_id, UNKNOWN_PERSON)
            flags = [1 if user_id in present_by_day[day] else 0 for day in days]
            count = sum(flags)
            pct = round(100 * count / total, 1)
            writer.writerow([user_id, netid, name, email, count, total, pct] + flags)
    logger.info(f"Wrote {len(user_ids)} rows to {output_csv}")


def _bucket_for(
    pct: float,
) -> str:
    """Return the label of the attendance bucket for a percentage."""
    for label, lowest_pct in BUCKETS:
        if pct >= lowest_pct:
            return label
    return BUCKETS[-1][0]


def _write_buckets_csv(
    output_csv: Path,
    present_by_day: Dict[str, Set[str]],
    people: Dict[str, Person],
    user_ids: List[str],
) -> None:
    """Write one row per person grouped by attendance bucket, highest bucket first."""
    total = len(present_by_day)
    rows_by_bucket: Dict[str, List[list]] = {label: [] for label, _ in BUCKETS}
    for user_id in user_ids:
        netid, name, email = people.get(user_id, UNKNOWN_PERSON)
        count = _days_present(user_id, present_by_day)
        pct = round(100 * count / total, 1)
        rows_by_bucket[_bucket_for(pct)].append([netid, name, email, count, total, pct])

    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["bucket", "netid", "name", "email", "days_present", "days_total", "pct"])
        for label, rows in rows_by_bucket.items():
            logger.info(f"Bucket {label}: {len(rows)} students")
            for row in rows:
                writer.writerow([label] + row)
    logger.info(f"Wrote attendance buckets to {output_csv}")


def _log_summary(
    present_by_day: Dict[str, Set[str]],
    people: Dict[str, Person],
    user_ids: List[str],
) -> None:
    """Log the head count for each day and the attendance for each person."""
    total = len(present_by_day)
    for day, present in present_by_day.items():
        logger.info(f"{day}: {len(present)} present")

    for user_id in user_ids:
        count = _days_present(user_id, present_by_day)
        netid, name, _ = people.get(user_id, UNKNOWN_PERSON)
        logger.info(f"{netid:10s} {name:30s} {count}/{total} {100 * count / total:5.1f}%")

    unnamed = [user_id for user_id in user_ids if user_id not in people]
    if unnamed:
        logger.warning(
            f"{len(unnamed)} of {len(user_ids)} people are not in the users file: {unnamed}. "
            "Download a fresh users.json from a Slack workspace export."
        )


def count_attendance(
    input_dir: Path,
    output_csv: Path,
    users_file: Path,
    roster_file: Optional[Path] = None,
    exclude: Optional[Set[str]] = None,
) -> None:
    """Count attendance across all day files in input_dir and write a CSV.

    Everyone in the users file appears in the CSV, including people who never
    checked in, so missing students show up with 0 days.

    Args:
        input_dir: Folder holding one YYYY-MM-DD.json Slack export per class day.
        output_csv: Path of the summary CSV to write. The buckets CSV goes in
            the same folder as attendance_buckets.csv.
        users_file: Slack users.json that maps user IDs to netids, names, and emails.
        roster_file: Optional tab-separated roster (name, then netid) used when a
            Slack profile has only the netid as its name.
        exclude: Slack user IDs or netids to leave out, such as instructors and TAs.

    Raises:
        ValueError: If input_dir has no day files or a file is not a JSON list.
        FileNotFoundError: If users_file does not exist.
    """
    if not users_file.exists():
        raise FileNotFoundError(
            f"Users file {users_file} not found. Export the Slack workspace "
            "(Workspace settings, then Import/Export Data) and copy users.json here."
        )
    present_by_day = _read_days(input_dir)
    people = _load_users(users_file)
    if roster_file:
        _fill_names_from_roster(people, _load_roster(roster_file))
    exclude = exclude or set()

    everyone = set(people)
    for present in present_by_day.values():
        everyone.update(present)
    kept = [user_id for user_id in everyone if not _is_excluded(user_id, people, exclude)]

    # Fewest days present first, then by netid so the order is stable.
    user_ids = sorted(
        kept,
        key=lambda user_id: (
            _days_present(user_id, present_by_day),
            people.get(user_id, UNKNOWN_PERSON)[0],
        ),
    )
    for day in present_by_day:
        present_by_day[day] = present_by_day[day] & set(kept)

    _log_summary(present_by_day, people, user_ids)
    _write_csv(output_csv, present_by_day, people, user_ids)
    buckets_csv = output_csv.parent / BUCKETS_OUTPUT_NAME
    _write_buckets_csv(buckets_csv, present_by_day, people, user_ids)


def _parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Count class attendance from Slack roll-call channel exports.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
    # Day files and users.json in the same folder
    uv run python rollcall/count_attendance.py --input-dir .scratchpad/roll-call

    # Fill in missing names from a roster and leave out the instructor and TA
    uv run python rollcall/count_attendance.py --input-dir .scratchpad/roll-call \\
        --roster .scratchpad/students --exclude aa1603 akk103
""",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        required=True,
        help="Folder with one YYYY-MM-DD.json Slack export per class day",
    )
    parser.add_argument(
        "--users-file",
        type=Path,
        help=f"Slack users.json export (default: <input-dir>/{DEFAULT_USERS_FILE_NAME})",
    )
    parser.add_argument(
        "--roster",
        type=Path,
        help="Tab-separated class roster (name, then netid) to fill in missing names",
    )
    parser.add_argument(
        "--output-csv",
        type=Path,
        help=f"CSV to write (default: <input-dir>/{DEFAULT_OUTPUT_NAME})",
    )
    parser.add_argument(
        "--exclude",
        nargs="*",
        default=[],
        help="Slack user IDs or netids to leave out, such as instructors and TAs",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Turn on debug logging",
    )
    return parser.parse_args()


def main() -> None:
    """Parse arguments and run the attendance count."""
    args = _parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    start_time = time.time()
    count_attendance(
        input_dir=args.input_dir,
        output_csv=args.output_csv or args.input_dir / DEFAULT_OUTPUT_NAME,
        users_file=args.users_file or args.input_dir / DEFAULT_USERS_FILE_NAME,
        roster_file=args.roster,
        exclude=set(args.exclude),
    )
    logger.info(f"Completed in {time.time() - start_time:.1f} seconds")


if __name__ == "__main__":
    main()
