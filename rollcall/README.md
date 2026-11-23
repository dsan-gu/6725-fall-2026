# Roll call

We take attendance in a Slack channel set up for roll call. At the start of
each class, the instructor or TA posts a greeting there, such as "Hi, roll call
for 11/17". Each student who is in class reacts to that message with any emoji.
At the end of the semester, or at any point during it, we export the channel
and run `count_attendance.py` to count who was present each day.

## Files you need

Put all of these in one folder outside git, such as `.scratchpad/roll-call/`.
They hold student names, netids, and emails, so never commit them.

| File | Where it comes from | Required |
| --- | --- | --- |
| `YYYY-MM-DD.json` | One per class day: that day's messages from the roll-call channel export | Yes |
| `users.json` | The Slack workspace export (Workspace settings, then Import/Export Data) | Yes |
| Class roster | Tab-separated file with the student's name in column 1 and netid in column 2 | No |

The script needs `users.json`. Slack stores each reaction as a bare user ID
like `U0123ABCDEF`, and `users.json` is the only file that maps those IDs to a
netid, name, and email. In our workspace the Slack username is the netid. The
script stops with an error if it cannot find `users.json`.

Some students leave their Slack name set to their netid. Pass the class roster
with `--roster` and the script fills in their names from it.

## Each class day

1. Post a greeting in the roll-call channel.
2. Ask students to react to it with an emoji.
3. Export that day's messages to a file named `YYYY-MM-DD.json`.

## Running the script

```bash
# Day files and users.json in the same folder
uv run python rollcall/count_attendance.py --input-dir .scratchpad/roll-call

# Fill in missing names from the roster and leave out the instructor and TA
uv run python rollcall/count_attendance.py \
    --input-dir .scratchpad/roll-call \
    --roster .scratchpad/students \
    --exclude aa1603 akk103
```

The script needs only the Python standard library.

| Option | Meaning |
| --- | --- |
| `--input-dir` | Folder with the day files. Required. |
| `--users-file` | Slack `users.json`. Defaults to `<input-dir>/users.json`. |
| `--roster` | Tab-separated roster (name, then netid) to fill in missing names. |
| `--output-csv` | Where to write the CSV. Defaults to `<input-dir>/attendance_summary.csv`. |
| `--exclude` | Slack user IDs or netids to leave out, such as the instructor and TAs. |
| `--debug` | Turn on debug logging. |

## How it counts

A person counts as present on a day if they reacted to any message in that
day's file or posted a message of their own. Anyone who posts the roll-call
message counts as present, so pass the instructor's and TAs' netids to
`--exclude`.

The script logs the head count for each day and writes a CSV with one row per
person in `users.json`. Bots and deleted accounts are skipped. Students who
never checked in still get a row, with 0 days present. The columns are:

- `slack_id`, `netid`, `name`, `email`
- `days_present`, `days_total`, `pct`
- one column per day, with 1 for present and 0 for absent

The script also writes `attendance_buckets.csv` in the same folder. It groups
students by attendance into five buckets: 100, 90 to 100, 80 to 90, 50 to 80,
and below 50. Each bucket includes its lower bound, so a student at exactly 90%
lands in "90 to 100". The columns are `bucket`, `netid`, `name`, `email`,
`days_present`, `days_total`, and `pct`.
