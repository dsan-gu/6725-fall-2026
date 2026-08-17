# Applied Generative AI for AI developers (DSAN 6725) Fall 2026 <a href='https://github.com/dsan-gu/6725-fall-2026'><img src='docs/assets/images/logo.png' align="right" height="139" /></a>

[DSAN 6725 • Fall 2026](https://github.com/dsan-gu/6725-fall-2026)  
[Amit Arora](https://www.linkedin.com/in/amit-arora-539120a/) • Graduate School of Arts & Sciences • Georgetown University

------------------------------------------------------------------------

## How the site works

The website is a custom static site: all content is authored as **Markdown files under `docs/`**, and `build_site.py` converts them into a hand-designed HTML/CSS site in `site/`. Lecture slides are Quarto reveal.js decks (`docs/lectures/slides/*.qmd`) rendered by `render_slides.sh` into `docs/assets/html/`, which the weekly pages embed.

To add or edit content, just edit the Markdown and rebuild — no framework knowledge needed.

## Lecture slides: where the content lives and how to render it

The actual lecture content lives in the Quarto reveal.js source decks — one `.qmd` file per week:

```
docs/lectures/slides/week-01-genai-foundations-and-coding-assistants.qmd
docs/lectures/slides/week-02-inference.qmd
docs/lectures/slides/week-03-rag-and-intro-to-agents.qmd
docs/lectures/slides/week-04-agentic-rag-and-mcp.qmd
docs/lectures/slides/week-05-agent-architectures.qmd
docs/lectures/slides/week-06-evals-observability-guardrails.qmd
docs/lectures/slides/week-07-ontology-semantic-layer.qmd
docs/lectures/slides/week-08-tokenomics.qmd
docs/lectures/slides/week-09-agentic-platforms.qmd
docs/lectures/slides/week-10-a2a.qmd
docs/lectures/slides/week-11-finetuning.qmd
docs/lectures/slides/week-12-open-weight-vs-frontier.qmd
docs/lectures/slides/week-13-ai-ethics.qmd
```

Each `.qmd` is Markdown with a reveal.js YAML header; every `##` heading starts a new slide. Images used by the slides go in `docs/lectures/slides/img/`.

To render slides after editing (requires [Quarto](https://quarto.org/docs/download/)):

```{.bash}
./render_slides.sh
```

This renders each deck to a self-contained `docs/assets/html/week<N>.html`, which the weekly wrapper pages (`docs/lectures/week<N>.md` — just a title plus an embed, rarely edited) display on the site. So the full slide workflow is:

1. Edit `docs/lectures/slides/week-NN-*.qmd`
2. `./render_slides.sh`
3. `uv run python build_site.py`
4. Upload `site/` (see `.siteupload`)

If you add or rename a deck, update the `week_files` list at the top of `render_slides.sh`.

## How to build the site

1. Clone this repository.

1. Install `uv` and sync the dependencies.

    ```{.bash}
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv sync
    ```

1. (Only when slides change) Install [`Quarto`](https://quarto.org/docs/download/) and render the slide decks.

    ```{.bash}
    ./render_slides.sh
    ```

1. Build the website into the `site/` directory.

    ```{.bash}
    uv run python build_site.py
    ```

1. To preview locally, serve the `site/` directory and open `http://127.0.0.1:9999/`.

    ```{.bash}
    python3 -m http.server 9999 -d site
    ```

1. To deploy to georgetown.domains, upload the built site (see `.siteupload` for the exact command).

    ```{.bash}
    rsync -avz --delete site/ <username>@<subdomain>.georgetown.domains:/home/<username>/<sitename>.<subdomain>.georgetown.domains/
    ```

## Licenses

**Text and figures:** All prose and images are licensed under Creative
Commons ([CC-BY-NC4.0](https://creativecommons.org/licenses/by-nc/4.0/))

**Code:** All code is licensed under the [MIT License](LICENSE).
