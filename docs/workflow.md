# Small changes and moving between computers

## Working on one action

Supply the lesson ID, unit, and desired action, such as: "L01/u01: make a ruler
appear below this box and show its width." Named objects or labelled blocks are
more stable targets than line numbers. You decide explanations and sequence.

The assistant reads current code, makes only the requested changes, explains
adjustment settings, and runs appropriate non-rendering checks. You modify code
and render locally to inspect it. Neither a passing check nor a printed command
claims visual accuracy. Only your review accepts the appearance and pacing.

When a unit is implemented, include its ID in UNIT_ORDER in scene.py. Later
units refer to named objects in state.py. No automatic chapter cards or fades
are inserted. A full lesson runs the entire order on one Scene and produces
one video when YOU render it.

## Unit previews

The launcher uses the full scene code. Earlier units construct their state with
animations skipped; the target plays and execution stops at its end. This may
still construct text/LaTeX in earlier units when YOU run it. Tracker-based,
analytic motion skips more reliably than accumulated dt-based updaters. You
must compare a target preview with its full-lesson context when timing or
updaters are involved. Skipping does not substitute for visual verification.

## Git and OneDrive

Keep a local source checkout on each computer, outside OneDrive. The public
remote is https://github.com/RustamKarimov/manim-physics. Git protects source
history; OneDrive holds large shared assets and selected exports. See git-sync.md
for cloning and switching computers. Uploads and exports are not automatic.

Before switching computers: save, review the diff, commit, push, and wait for
changed assets to sync. On the next computer, pull before editing and run
`uv sync --locked`. If there are local changes, preserve them before resolving
any conflict. Never discard changes just to make a pull succeed.

Keep short progress notes with the current action and important user decisions.
Git and progress notes supplement, rather than replace, reading the current code.

## Paths and outputs

Small assets can live beside the lesson. Resolve them from `Path(__file__)`, not
the terminal's current folder. Large shared assets can use machine-specific
`.local/settings.toml`; the scaffold supplies an example, but no asset loader
is added until a requested unit needs it. Match relative asset names across PCs.

The launcher explicitly selects manim.cfg and a separate lesson/unit/profile
output root. Manim does not otherwise search parent folders for this config.
Copy a chosen final MP4 to OneDrive exports yourself. Caches and previews stay
local; nothing automatically overwrites a published/exported file.
