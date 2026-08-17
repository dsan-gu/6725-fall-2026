# Applied Generative AI for AI developers (DSAN 6725) Fall 2026 <a href='https://github.com/dsan-gu/6725-fall-2026'><img src='docs/assets/images/logo.png' align="right" height="139" /></a>

[DSAN 6725 • Fall 2026](https://github.com/dsan-gu/6725-fall-2026)  
[Amit Arora](https://www.linkedin.com/in/amit-arora-539120a/) • Graduate School of Arts & Sciences • Georgetown University

------------------------------------------------------------------------

## How the site works

The website is a custom static site: all content is authored as **Markdown files under `docs/`**, and `build_site.py` converts them into a hand-designed HTML/CSS site in `site/`. Lecture slides are Quarto reveal.js decks (`docs/lectures/slides/*.qmd`) rendered by `render_slides.sh` into `docs/assets/html/`, which the weekly pages embed.

To add or edit content, just edit the Markdown and rebuild — no framework knowledge needed.

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
