# Applied Generative AI for AI developers (DSAN 6725) Fall 2026 <a href='https://github.com/dsan-gu/6725-fall-2026'><img src='docs/assets/images/logo.png' align="right" height="139" /></a>

[DSAN 6725 • Fall 2026](https://github.com/dsan-gu/6725-fall-2026)  
[Amit Arora](https://www.linkedin.com/in/amit-arora-539120a/) • Graduate School of Arts & Sciences • Georgetown University

------------------------------------------------------------------------

## How to build the site

1. Clone this repository.

1. Install [VSCode](https://code.visualstudio.com/download).

1. Open the folder for this repository in VSCode.

1. Install `uv` using the following command and sync the `pyprojecttoml` to install the dependencies.

    ```{.bash}
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv venv && source .venv/bin/activate && uv pip install --requirement pyproject.toml
    ```

1. Install [`Quarto`](https://quarto.org/) as per the instructions given [here](https://quarto.org/docs/download/tarball.html).

    ```{.bashrc}
    wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.6.40/quarto-1.6.40-linux-amd64.tar.gz
    mkdir ~/opt
    tar -C ~/opt -xvzf quarto-1.6.40-linux-amd64.tar.gz
    mkdir ~/.local/bin
    ln -s ~/opt/quarto-1.6.40/bin/quarto ~/.local/bin/quarto
    rm -f quarto-1.6.40-linux-amd64.tar.gz 
    ```

1. The slides for the lectures every week are created in quarto, so first render the slides.

    ```{.bash}
    ./render_slides.sh
    ```

1. To deploy the site to a custom domain (e.g., georgetown.domains), use `pscp` to upload the built site.

    ```{.bash}
    pscp -r site/ <username>@<subdomain>.georgetown.domains:/home/<username>/<sitename>.<subdomain>.georgetown.domains
    ```

1. To render the site locally run the following command. This will start a local website and provide a URL such as `http://127.0.0.1:8000/course/` for accessing the website.

    ```{.bash}
    mkdocs serve -a 127.0.0.1:9999
    ```

1. To build the static site for offline viewing or download, run the following command. This will generate the site in the `site/` directory.

    ```{.bash}
    mkdocs build
    ```

1. To publish the website on GitHub use the following command. This will publish the site to GitHub and provide the URL for accessing it, such as `https://gu-dsan.github.io/6725-fall-2026/`

    ```{.bash}
    mkdocs gh-deploy
    ```

## Licenses

**Text and figures:** All prose and images are licensed under Creative
Commons ([CC-BY-NC4.0](https://creativecommons.org/licenses/by-nc/4.0/))

**Code:** All code is licensed under the [MIT License](LICENSE).
