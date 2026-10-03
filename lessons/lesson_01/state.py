"""Named references that remain available across the lesson's units."""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from manim import Mobject, ValueTracker


@dataclass
class LessonState:
    # Store references, not copies, so later units adjust the same visible object.
    # Example when requested: state.objects["box"] = box
    objects: dict[str, "Mobject"] = field(default_factory=dict)
    # Name trackers by meaning, e.g. "physical_time". Their values should have
    # explicitly documented units in the unit that creates them.
    trackers: dict[str, "ValueTracker"] = field(default_factory=dict)
    # Numerical values may be shared without mixing them with visual objects.
    values: dict[str, float] = field(default_factory=dict)
