# Manim physics lessons

You supply each visual action and the lesson flow. The assistant implements
small, commented changes; you adjust the real code. Your changes are preserved.
No content, explanation, or transition is invented by the scaffold.

## Start in PyCharm

The working Mac project is `/Users/rustamkarimov/Projects/manim-physics`,
outside OneDrive. Open this folder with **File → Open** in PyCharm.

On Windows, clone `https://github.com/RustamKarimov/manim-physics.git` into a
local folder outside OneDrive, then open it in PyCharm. See
[Git synchronization instructions](docs/git-sync.md).

Keep OneDrive for `shared-assets` and selected `exports`. Do not copy `.venv`,
`.idea`, or `build` between computers. Each checkout has its own environment
and `.local/settings.toml` paths. The old OneDrive source is a scaffold snapshot.

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

Render commands open the completed video in your default player automatically.
An empty unit order deliberately refuses a real render until an action is added. A printed command is informational, not proof a unit is implemented.
Generated output stays under `build/<lesson>/<full-or-unit>/<profile>/`.

See [workflow](docs/workflow.md) and [editing guide](docs/code-editing-guide.md).

## Source synchronization

Use https://github.com/RustamKarimov/manim-physics as the source remote.
See [Mac/Windows Git instructions](docs/git-sync.md). Save, commit, and push
before switching computers; pull before editing on the other computer.
The source copy left in OneDrive is a scaffold snapshot, not an active checkout.
