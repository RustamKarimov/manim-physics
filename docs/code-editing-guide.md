# How to adjust unit code

## Settings close to the action

Each implementation should start with named settings and explain their effects.
For example, a future requested action might expose BOX_WIDTH, RULER_OFFSET,
and APPEAR_SECONDS. These are examples only; no box/ruler is currently created.

- Position/size: document whether a value is screen units or a physical quantity.
- Colours/strokes: explain which object receives the setting.
- Timing: run_time and wait values are playback seconds.
- Physics: document assumptions, units, sign conventions, and linked equations.

Physical elapsed time should be a separate tracker where relevant. A duration
change must not accidentally change the physics. For axes use axes.c2p() to map
physical values to the screen; unequal axis scales also affect tangent vectors.

## Object references and updaters

`state.objects["box"]` would hold the SAME box shown in a previous unit.
Retrieving that reference preserves continuity. Do not redraw or clear objects
merely because a new unit begins. Explain when an updater is attached and when
it is removed; leaving one active can change later actions unexpectedly.

## Playback order

UNIT_REGISTRY maps stable unit IDs to functions. UNIT_ORDER is the exact ordered
tuple of implemented IDs. For the first implemented unit use `("u01",)`; the
comma is required for a one-element tuple. The template starts with an empty
order so it cannot silently render invented content.

## Your changes

You can edit code directly. The assistant must read the current file and preserve
your adjustments unless explicitly asked to change that area. A USER-TUNED
comment is optional, not necessary. If an instruction may touch your adjustments,
name the exact object or block that you want changed.

Visual defaults in shared/style.py are opt-in values, not global overrides.
Future units use them explicitly only as appropriate to your instructions.
