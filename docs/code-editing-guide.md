# How to adjust unit code

## Settings close to the action

Small actions can keep a few named settings beside their code. As a section
grows, place editable values in a separate settings file for that section,
grouped by object or action and explained with comments. Do not extract every
literal: expose values useful for adjustment or reused in linked calculations.
Shared course-wide defaults belong in shared/style.py only when wanted.

Lesson 1's introduction uses lessons/lesson_01/intro_settings.py for wording,
font sizes, heading gap, positions and timing; intro.py contains the animation.
The introduction is separate from the first teaching unit. Future longer units
can use units/u01_settings.py beside units/u01.py, and similarly for other units.
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
tuple of implemented IDs. The current order is `("intro",)`; the comma is required for a one-element
tuple. When teaching unit 1 is implemented, the order can be
`("intro", "u01")`. Preview just the opening with
`python tools/render.py L01 --unit intro --profile preview`.

## Your changes

You can edit code directly. The assistant must read the current file and preserve
your adjustments unless explicitly asked to change that area. A USER-TUNED
comment is optional, not necessary. If an instruction may touch your adjustments,
name the exact object or block that you want changed.

Visual defaults in shared/style.py are opt-in values, not global overrides.
Future units use them explicitly only as appropriate to your instructions.
