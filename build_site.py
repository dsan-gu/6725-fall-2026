"""Static site builder for the DSAN 6725 course website.

Converts Markdown files under docs/ into a hand-designed static site in site/.
Markdown is the only authoring format; slides remain Quarto reveal.js decks
rendered separately by render_slides.sh into docs/assets/html/.

Usage:
    uv run python build_site.py
"""

import logging
import re
import shutil
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,p%(process)s,{%(filename)s:%(lineno)d},%(levelname)s,%(message)s",
)
logger = logging.getLogger(__name__)

DOCS_DIR: Path = Path("docs")
SITE_DIR: Path = Path("site")
SITE_TITLE: str = "DSAN 6725 · Applied Generative AI"
COURSE_NAME: str = "Applied Generative AI for Developers"
TERM: str = "Fall 2026"
REPO_URL: str = "https://github.com/dsan-gu/6725-fall-2026"

# Top navigation: (label, path relative to site root)
NAV: list[tuple[str, str]] = [
    ("Home", "index.html"),
    ("Syllabus", "syllabus.html"),
    ("Schedule", "schedule.html"),
    ("Lectures", "lectures/index.html"),
    ("Labs", "labs/index.html"),
    ("Project", "project/index.html"),
    ("Resources", "resources.html"),
]

# Markdown files never published to the site
EXCLUDE: set[str] = {"syllabus-internal.md"}

MD_EXTENSIONS: list[str] = [
    "tables",
    "fenced_code",
    "codehilite",
    "admonition",
    "attr_list",
    "md_in_html",
    "toc",
    "sane_lists",
    "nl2br",
]


PAGE_TEMPLATE: str = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {site_title}</title>
<link rel="icon" href="{root}assets/images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600;6..72,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}stylesheets/site.css">
<link rel="stylesheet" href="{root}stylesheets/pygments.css">
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="{root}index.html">
      <img src="{root}assets/images/logo.png" alt="Course logo">
      <span class="brand-text"><strong>DSAN 6725</strong><small>{course_name}</small></span>
    </a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle" aria-label="Toggle navigation">
    <label for="nav-toggle" class="nav-toggle-label"><span></span></label>
    <nav class="site-nav" aria-label="Main">
{nav_items}
    </nav>
  </div>
</header>
<div class="page{layout_class}">
  <main class="content">
{body}
  </main>
{toc_aside}
</div>
<footer class="site-footer">
  <div class="footer-inner">
    <p><strong>DSAN 6725 · {course_name}</strong> · {term} · Georgetown University</p>
    <p>Tuesdays 8:00–10:30 AM · CBN-203 (Car Barn 203) · <a href="{repo_url}">GitHub</a></p>
    <p class="footer-fine">© 2026 Amit Arora · Text CC-BY-NC 4.0 · Code MIT</p>
  </div>
</footer>
</body>
</html>
"""

EMPTY_PAGE_BODY: str = (
    "<h1>{title}</h1>\n"
    '<div class="admonition note"><p class="admonition-title">Coming soon</p>'
    "<p>Details will be posted here and on Canvas.</p></div>"
)


def _rel_root(
    page_path: str,
) -> str:
    """Relative prefix from a page back to the site root (e.g. 'lectures/week1.html' -> '../')."""
    depth = page_path.count("/")
    return "../" * depth if depth else "./"


def _nav_html(
    current: str,
    root: str,
) -> str:
    items = []
    current_section = current.split("/")[0]
    for label, path in NAV:
        section = path.split("/")[0]
        active = " active" if section == current_section else ""
        items.append(f'      <a class="nav-link{active}" href="{root}{path}">{label}</a>')
    return "\n".join(items)


def _toc_html(
    toc_tokens: list,
) -> str:
    """Right-rail table of contents from h2 headings; empty if the page is short."""
    h2s = []
    for token in toc_tokens:
        if token["level"] == 1:
            h2s.extend(t for t in token.get("children", []) if t["level"] == 2)
        elif token["level"] == 2:
            h2s.append(token)
    if len(h2s) < 4:
        return ""
    links = "\n".join(
        f'    <a href="#{t["id"]}">{t["name"]}</a>' for t in h2s
    )
    return (
        '<aside class="toc" aria-label="On this page">\n'
        "  <div class=\"toc-inner\">\n"
        "    <p class=\"toc-title\">On this page</p>\n"
        f"{links}\n"
        "  </div>\n"
        "</aside>"
    )


def _page_title(
    md_source: str,
    fallback: str,
) -> str:
    match = re.search(r"^#\s+(.+)$", md_source, flags=re.MULTILINE)
    return match.group(1).strip() if match else fallback


def _fix_md_links(
    html: str,
) -> str:
    """Rewrite local .md hrefs to .html so authors can link between markdown files."""
    return re.sub(
        r'href="(?!https?://)([^"#]+)\.md(#[^"]*)?"',
        lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"',
        html,
    )


def _build_page(
    md_file: Path,
    out_path: str,
) -> None:
    source = md_file.read_text(encoding="utf-8")
    if md_file.stem == "index" and md_file.parent != DOCS_DIR:
        fallback_title = md_file.parent.name.title()
    else:
        fallback_title = re.sub(r"(?<=[a-z])(?=\d)", " ", md_file.stem.replace("-", " ")).title()
    root = _rel_root(out_path)

    if not source.strip():
        title = fallback_title
        body = EMPTY_PAGE_BODY.format(title=title)
        toc_aside = ""
    else:
        md = markdown.Markdown(extensions=MD_EXTENSIONS)
        body = _fix_md_links(md.convert(source))
        title = _page_title(source, fallback_title)
        toc_aside = _toc_html(getattr(md, "toc_tokens", [])) if out_path != "index.html" else ""

    html = PAGE_TEMPLATE.format(
        title=title,
        site_title=SITE_TITLE,
        course_name=COURSE_NAME,
        term=TERM,
        repo_url=REPO_URL,
        root=root,
        nav_items=_nav_html(out_path, root),
        body=body,
        toc_aside=toc_aside,
        layout_class=" with-toc" if toc_aside else "",
    )

    dest = SITE_DIR / out_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    logger.info(f"built {out_path}")


def _copy_static() -> None:
    shutil.copytree(DOCS_DIR / "assets", SITE_DIR / "assets", dirs_exist_ok=True)
    shutil.copytree(DOCS_DIR / "stylesheets", SITE_DIR / "stylesheets", dirs_exist_ok=True)
    pygments_css = HtmlFormatter(style="xcode").get_style_defs(".codehilite")
    (SITE_DIR / "stylesheets" / "pygments.css").write_text(pygments_css, encoding="utf-8")


def main() -> None:
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()
    _copy_static()

    pages = 0
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        rel = md_file.relative_to(DOCS_DIR)
        if rel.name in EXCLUDE or rel.parts[0] in {"assets", "stylesheets"} or "slides" in rel.parts:
            continue
        out_path = str(rel.with_suffix(".html"))
        _build_page(md_file, out_path)
        pages += 1

    logger.info(f"done: {pages} pages -> {SITE_DIR}/")


if __name__ == "__main__":
    main()
