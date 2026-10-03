# Synchronizing the Mac and Windows projects

Repository: https://github.com/RustamKarimov/manim-physics
The working source on this Mac is /Users/rustamkarimov/Projects/manim-physics.
The original OneDrive source copy is a scaffold snapshot; do not edit it as a
second working copy. OneDrive holds shared-assets and selected exports only.

## First setup on Windows

Use PyCharm's Clone Repository / Get from Version Control option with:
https://github.com/RustamKarimov/manim-physics.git
Choose a local folder OUTSIDE OneDrive. Open the resulting project and run:

```powershell
uv python install 3.12
uv sync --locked
```

Select the existing interpreter at .venv/Scripts/python.exe. Sign in to GitHub
through PyCharm when you first push. Reading this public repository needs no
GitHub login; pushing does. Configure your Git author name and preferably your
GitHub no-reply email on the Windows checkout before committing.

Copy .local/settings.example.toml to .local/settings.toml on Windows and enter
that PC's actual OneDrive shared-assets and exports paths. Do not copy the Mac's
local settings, environment, or PyCharm settings.

## Each time you switch computers

Before editing on the next computer, run:

```bash
git status
git pull --ff-only
uv sync --locked
```

If there are unfinished local changes, preserve them before pulling. If pull
reports diverged branches, resolve the history without a force push or reset.

Before leaving the current computer, save all files, then:

```bash
git status
git diff
git add .
git diff --cached
git commit -m "Describe the small change"
git push
```

Review the staged changes before committing. In PyCharm you can use the Git
Commit/Push and Pull controls instead. A saved file is NOT uploaded until you
commit and push. Wait for OneDrive asset synchronization separately.

The repository is public: do not add passwords, tokens, personal student data,
or assets you cannot publish. .venv, .idea, build, local path settings, and large
OneDrive folders are excluded. Git tracks code, comments, configuration, and
manual adjustments. The assistant does not render.

## Commit signing on this Mac

The pre-existing global Git configuration attempted GPG signing, but its signer
failed during setup. The initial project commit was made unsigned; global signing
settings were left unchanged. If a later commit reports the same error, either
repair your GPG signing setup or make that individual commit unsigned:

```bash
git -c commit.gpgsign=false commit -m "Describe the small change"
```
