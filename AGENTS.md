# AGENTS.md

Instructions for AI coding agents working in this repository (DSAN 6725, Applied
Generative AI for AI Developers). Human contributors: start with `README.md`.

This file is also a teaching artifact — it is the worked example students look at in
Week 1 when we cover agent instruction files. Keep it honest, current, and short enough
that a person will actually read it.

## What this repo is

A course website plus lecture materials. There is no application code to ship.

- Content is authored as **Markdown under `docs/`**.
- `build_site.py` converts that Markdown into a hand-designed static site in `site/`.
- Lecture slides are **Quarto reveal.js decks** at `docs/lectures/slides/week-NN-*.qmd`,
  rendered by `render_slides.sh` into self-contained `docs/assets/html/week<N>.html`.
- `site/` and `docs/assets/html/` are **build output**. Never hand-edit them; edit the
  source and rebuild.

## Dev environment

- Python **>=3.11, <3.12** (pinned in `pyproject.toml`); dependencies managed with `uv`.
- `uv sync` — install everything into `.venv`.
- [Quarto](https://quarto.org/docs/download/) is required **only** when slides change.

## Commands

- **Render all slide decks:** `./render_slides.sh`
  - Quarto is located automatically; override with `QUARTO_BIN=/path/to/quarto ./render_slides.sh`.
  - Renders every deck listed in the `week_files` array at the top of the script.
- **Build the site:** `uv run python build_site.py` (writes `site/`)
- **Preview locally:** `python3 -m http.server 9999 -d site` then open <http://127.0.0.1:9999/>
- **Deploy:** see `.siteupload` for the exact `rsync` command to georgetown.domains.

The full loop after editing a deck:

```bash
./render_slides.sh                  # only if a .qmd changed
uv run python build_site.py
python3 -m http.server 9999 -d site # eyeball it before deploying
```

## Editing slides

- One `.qmd` per week. Every `##` heading starts a **new slide**; `#` starts a section
  divider slide. Keep slides to roughly 6–8 bullets — content that overflows is silently
  cut off in reveal.js.
- Add `{.smaller}` to a slide heading when it carries a table or a long list.
- Images live in `docs/lectures/slides/img/` and are referenced relatively:
  `![](img/foo.png){width=85%}`. Add new images there, not to `docs/assets/`.
- Styling is centralized in `docs/lectures/slides/custom.scss`. Do not add inline CSS to
  individual decks.
- Slide decks are rendered with `-M embed-resources=true`, so every deck is a single
  self-contained HTML file. Expect large diffs in `docs/assets/html/` — that is normal.
- If you add or rename a deck, update the `week_files` array in `render_slides.sh` **and**
  add the matching wrapper page `docs/lectures/week<N>.md`.

## Editing site content

- `docs/lectures/week<N>.md` is a thin wrapper (title plus an `<iframe>` embed). It rarely
  needs editing — put the actual content in the `.qmd`.
- `docs/syllabus-internal.md` is instructor-facing. Do not link it from the public nav.
- Navigation lives in the `NAV` list in `build_site.py`. A new top-level page needs both a
  Markdown file under `docs/` and an entry there.

## Content conventions

- Course years and model names go stale fast. When updating a deck, check that model
  names, versions, and links are current rather than copying from a previous semester.
- Prefer linking to primary sources (papers, official docs, repos) over blog summaries.
- Use `--` for an em dash in `.qmd` files; the decks avoid literal Unicode dashes.

## Python code style

Applies to `build_site.py` and `scripts/`. The full standards are in `CLAUDE.md`; the
essentials:

- Type hints on every function signature; Google-style docstrings on public functions.
- Use `logging`, never `print`, in scripts.
- Use `pathlib.Path` for filesystem work.
- Keep functions small and single-purpose; prefer early returns over deep nesting.

## Boundaries

- **Never commit build output as the *only* change** — if `site/` or
  `docs/assets/html/` changed, the corresponding source change must be in the same commit.
- **Never edit `.canvastoken`, `.siteupload`, or anything containing credentials.**
- Do not add a dependency without a stated reason; this repo intentionally has a small
  dependency footprint.
- Do not run the deploy `rsync` command. Deployment is a human decision.
- Ask before rewriting an entire deck. Incremental, reviewable edits only.

## Commits and PRs

- Conventional, scoped subject lines: `week-01: add AGENTS.md section`,
  `build_site: fix nav ordering`.
- Describe the user-visible change, not the implementation.
- Do not add yourself as a commit co-author. Agents assist; humans author.

## References

- `README.md` — human-facing build and deploy instructions
- `CLAUDE.md` — Python coding standards for this repo
- [AGENTS.md format](https://agents.md/) · [spec and examples](https://github.com/agentsmd/agents.md)
