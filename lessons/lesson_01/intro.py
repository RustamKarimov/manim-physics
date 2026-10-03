"""Opening title: write Physical Quantities, hold, then unwrite it."""

from manim import Scene, Text, UP, Unwrite, VGroup, Write

from lessons.lesson_01.state import LessonState

# Adjustable values live beside this file in intro_settings.py.
# Keep animation steps here; change wording, size, spacing and timing there.
from lessons.lesson_01.intro_settings import (
    COURSE_FONT_SIZE,
    COURSE_GAP,
    COURSE_TEXT,
    HOLD_SECONDS,
    TITLE_COLOR,
    TITLE_FONT,
    TITLE_FONT_SIZE,
    TITLE_POSITION,
    TITLE_TEXT,
    UNWRITE_SECONDS,
    WRITE_SECONDS,
)


def play(scene: Scene, state: LessonState) -> LessonState:
    """Play only the requested title action; subsequent actions continue hereafter."""
    # 1. BUILD THE TITLE
    # Text uses installed fonts through Pango, so this title needs no LaTeX.
    # For formatted spans/coloured words, MarkupText is another text object.
    # Tex/MathTex are alternatives for typeset wording or mathematical notation;
    # they normally require a working LaTeX installation.
    title = Text(
        TITLE_TEXT,
        font=TITLE_FONT,
        font_size=TITLE_FONT_SIZE,
        color=TITLE_COLOR,
    )
    title.move_to(TITLE_POSITION)

    # COURSE HEADING ABOVE THE TITLE
    # next_to keeps the heading horizontally centred above the title.
    # buff is the edge-to-edge gap in screen units, controlled by COURSE_GAP.
    # This leaves your existing title position and size unchanged.
    course_heading = Text(
        COURSE_TEXT,
        font=TITLE_FONT,
        font_size=COURSE_FONT_SIZE,
        color=TITLE_COLOR,
    )
    course_heading.next_to(title, UP, buff=COURSE_GAP)

    # VGroup lets both lines share the same appearance, hold and removal.
    # Each line still has its own Text object and independent font size.
    intro_text = VGroup(course_heading, title)

    # 2. WRITE IT ON SCREEN
    # Write draws the letter outlines and fills them. run_time controls the total
    # duration. Write(intro_text, lag_ratio=0.1) is an optional way to adjust overlap
    # between successive parts of the grouped text; larger lag_ratio increases staggering.
    scene.play(Write(intro_text), run_time=WRITE_SECONDS)

    # Other appearance animations you can try by REPLACING Write(intro_text) above:
    # - FadeIn(intro_text): reveal the text by gradually increasing its opacity.
    # - GrowFromCenter(intro_text): enlarge it from its centre to its final size.
    # Add the chosen class to the explicit import above before using it.
    # For future requested shapes, Create(shape) draws their paths, while
    # DrawBorderThenFill(shape) draws the outline before revealing the fill.
    # A shape needs nonzero fill_opacity for its fill to be visible.
    # These are alternatives for your choice; none is added to the actual scene.
    # Reference: https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html

    # 3. HOLD THE COMPLETED TITLE
    # This wait starts AFTER Write finishes, so the full title is readable for
    # two seconds, together with the course heading. It does not include either appearance or removal time.
    scene.wait(HOLD_SECONDS)

    # 4. REMOVE THE TITLE
    # Unwrite reverses the writing effect and removes the title from the Scene.
    # Alternatives: FadeOut(intro_text) fades it away; Uncreate(intro_text) erases paths.
    # scene.remove(intro_text) removes it instantly, without any animation.
    # Import FadeOut or Uncreate if you choose one of those alternatives.
    scene.play(Unwrite(intro_text), run_time=UNWRITE_SECONDS)
    # Reference: https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html

    # Both intro lines are intentionally removed, so there is no visible object to pass
    # on. Other diagrams, when requested, may remain in state.objects instead.
    return state
