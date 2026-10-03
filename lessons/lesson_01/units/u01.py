"""Opening title: write Physical Quantities, hold, then unwrite it."""

from manim import Scene, Text, Unwrite, Write

from lessons.lesson_01.state import LessonState

# TITLE SETTINGS: edit these directly to adjust this opening action.
TITLE_TEXT = "Physical Quantities"  # Exact wording visible to the audience.
TITLE_FONT = "Arial"  # Installed on this Mac; use the same font on Windows.
TITLE_FONT_SIZE = 64  # Manim font size: larger numbers produce larger text.
TITLE_COLOR = "#FFFFFF"  # White; change to a hex colour such as "#FFD54F".
TITLE_POSITION = (0.0, 0.0, 0.0)  # Screen units: x right, y up; (0, 0, 0) centres it.

# TIMING SETTINGS: all three values are playback seconds.
WRITE_SECONDS = 1.5  # Time spent drawing the title, before the hold begins.
HOLD_SECONDS = 2.0  # Fully written title stays still for these two seconds.
UNWRITE_SECONDS = 1.0  # Time spent removing it, after the hold ends.


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

    # 2. WRITE IT ON SCREEN
    # Write draws the letter outlines and fills them. run_time controls the total
    # duration. Write(title, lag_ratio=0.1) is an optional way to adjust overlap
    # between successive letter animations; larger lag_ratio increases staggering.
    scene.play(Write(title), run_time=WRITE_SECONDS)

    # Other appearance animations you can try by REPLACING Write(title) above:
    # - FadeIn(title): reveal the text by gradually increasing its opacity.
    # - GrowFromCenter(title): enlarge it from its centre to its final size.
    # Add the chosen class to the explicit import above before using it.
    # For future requested shapes, Create(shape) draws their paths, while
    # DrawBorderThenFill(shape) draws the outline before revealing the fill.
    # A shape needs nonzero fill_opacity for its fill to be visible.
    # These are alternatives for your choice; none is added to the actual scene.
    # Reference: https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html

    # 3. HOLD THE COMPLETED TITLE
    # This wait starts AFTER Write finishes, so the full title is readable for
    # two seconds. It does not include either appearance or removal time.
    scene.wait(HOLD_SECONDS)

    # 4. REMOVE THE TITLE
    # Unwrite reverses the writing effect and removes the title from the Scene.
    # Alternatives: FadeOut(title) fades it away; Uncreate(title) erases paths.
    # scene.remove(title) removes it instantly, without any animation.
    # Import FadeOut or Uncreate if you choose one of those alternatives.
    scene.play(Unwrite(title), run_time=UNWRITE_SECONDS)
    # Reference: https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html

    # The title is intentionally removed, so there is no visible object to pass
    # on. Other diagrams, when requested, may remain in state.objects instead.
    return state
