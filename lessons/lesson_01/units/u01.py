"""Unit template. No lesson action has been specified or implemented yet."""

from manim import Scene

from lessons.lesson_01.state import LessonState


def play(scene: Scene, state: LessonState) -> LessonState:
    """Implement the user's requested actions here, retaining continuing objects."""
    # 1. ADJUSTMENT SETTINGS
    # Put physical quantities, screen sizes/positions, and playback durations in
    # separate named settings. Comment their units and linked effects.

    # 2. CONSTRUCTION / CONTINUING OBJECTS
    # Create only the requested objects, or retrieve them from state.objects.
    # Positions are Manim coordinates; axes.c2p(x, y) converts graph coordinates.

    # 3. REQUESTED ANIMATION
    # Add scene.play()/scene.wait() only as requested. run_time controls playback
    # seconds; it need not equal the physical elapsed time shown in a diagram.

    # 4. UPDATERS AND HANDOFF
    # Document each updater's inputs and when it stops. Do not clear the screen
    # or remove continuing objects just because this function finishes.
    # Register objects/trackers in state so the next unit can refer to them.
    return state
