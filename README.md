# Manim physics lessons

You supply each visual action and the lesson flow. The assistant implements
small, commented changes; you adjust the real code. Your changes are preserved.
No content, explanation, or transition is invented by the scaffold.

## Start in PyCharm

This scaffold was created in your existing OneDrive folder. Before installing
dependencies, copy the source project to a local folder OUTSIDE OneDrive, e.g.
`~/Projects/manim-physics` on Mac or `C:/Users/YourName/Projects/manim-physics`
on Windows. Open that local folder with **File → Open** in PyCharm.

Include hidden files when copying. Leave `shared-assets/` and `exports/` in
OneDrive rather than copying those two folders into the source checkout.

Keep the original OneDrive folder for `shared-assets` and selected `exports`.
An ignored folder is still synchronized by OneDrive if physically inside it.
Do not create `.venv`, `.idea`, or `build` in the synced source folder.

Follow [macOS setup](docs/setup-macos.md) or [Windows setup](docs/setup-windows.md).
After system prerequisites are ready, run in the LOCAL project terminal:

```bash
uv python install 3.12
uv sync --locked
```

Select the project's existing `.venv` interpreter in PyCharm. Requirements are
declared in `pyproject.toml` and resolved in `uv.lock`; no requirements.txt is needed.

## Navigate and check

- `course.toml`: 25 reserved lesson IDs; add more when needed.
- `lessons/lesson_01/scene.py`: one master Scene and the explicit unit order.
- `lessons/lesson_01/units/u01.py`: detailed template awaiting your first action.
- `lessons/lesson_01/state.py`: references carried between units.
- `manim.cfg`: shared render settings, with explanatory comments.
- `AGENTS.md`: editing, preservation, and no-render rules for future sessions.

Safe checks (no rendering, no lesson content executed):

```bash
uv run --locked python tools/check_project.py
uv run --locked python -m unittest discover -s tests -v
uv run --locked python tools/render.py L01 --print-command
```

The assistant never renders. Once you have implemented units, you may run:

```bash
uv run --locked python tools/render.py L01 --unit u01 --profile preview
uv run --locked python tools/render.py L01 --profile final
```

The empty scaffold deliberately refuses a real render until its unit order is
populated. A printed command is informational, not proof a unit is implemented.
Generated output stays under `build/<lesson>/<full-or-unit>/<profile>/`.

See [workflow](docs/workflow.md) and [editing guide](docs/code-editing-guide.md).

## Source synchronization

Use https://github.com/RustamKarimov/manim-physics as the source remote.
See [Mac/Windows Git instructions](docs/git-sync.md). Save, commit, and push
before switching computers; pull before editing on the other computer.
The source copy left in OneDrive is a scaffold snapshot, not an active checkout.
