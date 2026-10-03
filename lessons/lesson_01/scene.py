"""One continuous Scene for this lesson, built from user-directed units."""

import os

from manim import Scene

from lessons.lesson_01.state import LessonState
from lessons.lesson_01 import intro

# Add implemented units to this registry. Keys are stable development IDs only:
# they do not create on-screen titles or transitions.
UNIT_REGISTRY = {"intro": intro.play}

# The introduction is separate from teaching unit 1. Add future actions in
# the user's order; u01 is reserved for the first actual teaching unit.
# These IDs are code organisation only; they introduce no visible boundaries.
UNIT_ORDER: tuple[str, ...] = ("intro",)


class Lesson01(Scene):
    def construct(self) -> None:
        if not UNIT_ORDER:
            raise RuntimeError("No units implemented yet. Supply the first action before rendering.")
        if len(set(UNIT_ORDER)) != len(UNIT_ORDER):
            raise ValueError("UNIT_ORDER contains duplicate unit IDs.")
        if any(unit_id not in UNIT_REGISTRY for unit_id in UNIT_ORDER):
            raise ValueError("Every ordered unit must have an entry in UNIT_REGISTRY.")

        # The launcher sets this only for an individual-unit preview.
        target = os.environ.get("PHYSICS_PREVIEW_UNIT")
        if target and target not in UNIT_ORDER:
            raise ValueError(f"Unit {target!r} is not in UNIT_ORDER.")

        state = LessonState()
        for unit_id in UNIT_ORDER:
            # Earlier units still execute to establish the correct starting
            # objects and tracker values; their animations are skipped.
            # next_section is metadata, not a visible transition.
            self.next_section(unit_id, skip_animations=bool(target and unit_id != target))
            state = UNIT_REGISTRY[unit_id](self, state)
            if target == unit_id:
                break  # Preview ends here; full lessons continue normally.
