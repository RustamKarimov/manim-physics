# macOS: local project, uv, and PyCharm

## 1. Keep the working project outside OneDrive

In Finder, create `Projects/manim-physics` in your home folder and copy this
scaffold's contents there, including hidden files. Open the copied folder in
PyCharm with **File → Open**; do not generate a second project over it.

Leave `shared-assets/` and `exports/` in OneDrive. Copy the other source files
and folders, including hidden configuration files, to the local project.

The folder you open must directly contain `pyproject.toml` and `manim.cfg`.
Use OneDrive for large shared assets and chosen final exports, not environments.

## 2. Check uv

At scaffold creation, your Mac had uv 0.12.22 at
`/Users/rustamkarimov/.local/bin/uv`. This is YOUR local tool path, not a
portable project setting. In Terminal or PyCharm's terminal:

```bash
uv --version
```

If not found, reopen Terminal/PyCharm after installation, or use the full path.
Official standalone installation, only if needed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Source: <https://docs.astral.sh/uv/getting-started/installation/>

## 3. System prerequisites

Manim uses native Cairo/Pango libraries for graphics and text. Follow the
official installation guide for your Mac. With Homebrew available, install:

```bash
brew install cairo pango pkg-config
```

If a Python dependency must compile and reports missing compiler tools, install
Apple's Command Line Tools (`xcode-select --install`), then retry the sync.
LaTeX is required when requested units use Tex/MathTex. Your Mac already exposed
`latex` and `ffmpeg` on PATH at initial inspection; versions/packages were not
verified. Do not reinstall them merely because they appear in this guide.
If LaTeX is absent, the official guide describes MacTeX installation.

Source: <https://docs.manim.community/en/stable/installation/uv.html>

## 4. Install the Python environment

In PyCharm's terminal, confirm you are in the LOCAL copied project, then run:

```bash
uv python install 3.12
uv sync --locked
```

These download Python if necessary and create `.venv` locally. The lockfile is
shared, but the actual environment must be created separately on each computer.
If an installation fails, retain the error text for diagnosis; do not change
the pinned Manim version as a workaround without discussing it.

## 5. Select the interpreter in PyCharm

Open **Settings → Python → Interpreter → Add Interpreter → Add Local Interpreter**.
Select **uv** and the existing project environment. If uv is not detected,
browse to `/Users/rustamkarimov/.local/bin/uv`. If necessary use the ordinary
existing-interpreter option and select `<local-project>/.venv/bin/python`.
Menu labels can differ slightly by PyCharm build.

Do not ask PyCharm to create another environment named `venv`.
The working directory in a run configuration must be the project root.
Python source packages are already rooted there; no custom source-root settings
are required for the launcher.

Source: <https://www.jetbrains.com/help/pycharm/uv.html>

## 6. Verify without rendering

```bash
uv run --locked python tools/check_project.py
uv run --locked python -m unittest discover -s tests -v
uv run --locked python -c "import manim; print(manim.__version__)"
```

The last command verifies imports only; it does not construct a Scene.
Fonts and LaTeX visuals remain subject to your later visual checks. Before using
the suggested DejaVu Sans font, install matching font files on both machines.
