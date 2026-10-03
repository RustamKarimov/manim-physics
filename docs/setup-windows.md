# Windows: local project, uv, and PyCharm

## 1. Use a separate local checkout

Use a folder outside OneDrive, such as
`C:/Users/YourName/Projects/manim-physics`. Initially copy the source there;
once your private Git remote is configured, use its clone on this computer.
Open the folder containing `pyproject.toml` with PyCharm **File → Open**.

Do not copy the Mac's `.venv`, `.idea`, or `build` folders. They are machine-local.

## 2. Check prerequisites

You already have uv. In PyCharm's PowerShell terminal, check:

```powershell
uv --version
```

Install Python dependencies as below. If native packages lack compatible wheels
and compilation fails, follow Manim's official Windows guide for the required
compiler/system libraries. Do not apply macOS Homebrew instructions on Windows.
Tex/MathTex needs a working LaTeX distribution; install MiKTeX or TeX Live if
absent. Use compatible LaTeX packages and matching font files on both machines.

Source: <https://docs.manim.community/en/stable/installation/uv.html>

## 3. Create the local environment

Run from the local project root:

```powershell
uv python install 3.12
uv sync --locked
```

## 4. Point PyCharm at it

Open **Settings → Python → Interpreter → Add Interpreter → Add Local Interpreter**.
Select **uv**, then the existing project environment. If auto-detection fails,
`(Get-Command uv).Source` in PowerShell shows the uv executable location.
The fallback existing Python interpreter is:

```text
<local-project>\.venv\Scripts\python.exe
```

Use the project root as the run configuration's working directory. Do not
create a second environment or use the system interpreter for this project.

Source: <https://www.jetbrains.com/help/pycharm/uv.html>

## 5. Check without rendering

```powershell
uv run --locked python tools/check_project.py
uv run --locked python -m unittest discover -s tests -v
uv run --locked python -c "import manim; print(manim.__version__)"
```

Configure this computer's OneDrive paths by copying
`.local/settings.example.toml` to `.local/settings.toml`. Use forward slashes
in TOML paths, even on Windows. No export or upload happens automatically.
