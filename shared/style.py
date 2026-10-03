"""Editable visual defaults; no global Manim settings are changed on import."""

# Use the same installed font on both machines. This is a suggested starting
# choice, not a checked-in font. The setup guides describe matching fonts.
TEXT_FONT = "DejaVu Sans"
TEXT_SIZE = 32  # Manim font size; increasing it enlarges new text objects.
LINE_WIDTH = 3.0  # Stroke width, not a physical thickness.
OBJECT_COLOR = "#FFFFFF"
HIGHLIGHT_COLOR = "#FFD54F"

# Future units should explicitly use these settings when constructing objects.
# Changing a default does not retroactively modify an already-created object.
