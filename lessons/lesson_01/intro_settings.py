"""Editable wording, layout and timing for the lesson introduction."""

# INTRO SETTINGS: edit these values without searching through animation code.
# These belong to the lesson introduction, not the teaching content of unit 1.
TITLE_TEXT = "Chapter 1: Physical Quantities"  # Exact wording visible to the audience.
TITLE_FONT = "DejaVu Sans"  # Install this same font on Windows for matching text.
TITLE_FONT_SIZE = 64  # Manim font size: larger numbers produce larger text.
TITLE_COLOR = "#FFFFFF"  # White; change to a hex colour such as "#FFD54F".
TITLE_POSITION = (0.0, 0.0, 0.0)  # Screen units: x right, y up; (0, 0, 0) centres it.

# COURSE HEADING: shares the title font and colour; adjust its size independently.
COURSE_TEXT = "Cambridge International AS Physics"
COURSE_FONT_SIZE = 36  # Smaller than TITLE_FONT_SIZE; Manim font size.
COURSE_GAP = 0.35  # Screen units between the heading bottom and title top.
# The heading follows the title position automatically; no separate coordinates.

# TIMING SETTINGS: all three values are playback seconds.
WRITE_SECONDS = 1.5  # Time spent drawing the title, before the hold begins.
HOLD_SECONDS = 2.0  # Fully written title stays still for these two seconds.
UNWRITE_SECONDS = 1.0  # Time spent removing it, after the hold ends.

