"""Meaningful non-rendering checks for output separation and preview isolation."""

import os
from pathlib import Path
import unittest
from unittest.mock import patch

from tools.render import ROOT, build_command


class LauncherTests(unittest.TestCase):
    def test_full_and_unit_outputs_are_separate(self):
        full, _ = build_command("L01", None, "preview")
        unit, _ = build_command("L01", "u01", "preview")
        full_dir = full[full.index("--media_dir") + 1]
        unit_dir = unit[unit.index("--media_dir") + 1]
        self.assertNotEqual(full_dir, unit_dir)
        self.assertTrue(Path(full_dir).is_relative_to(ROOT / "build"))

    def test_full_render_cannot_inherit_unit_selection(self):
        with patch.dict(os.environ, {"PHYSICS_PREVIEW_UNIT": "u99"}):
            _, env = build_command("L01", None, "final")
        self.assertNotIn("PHYSICS_PREVIEW_UNIT", env)

    def test_explicit_config_and_final_profile(self):
        command, env = build_command("L01", "u01", "final")
        self.assertEqual(command[command.index("--config_file") + 1], str(ROOT / "manim.cfg"))
        self.assertEqual(command[command.index("--resolution") + 1], "1920,1080")
        self.assertEqual(command[command.index("--fps") + 1], "30")
        self.assertEqual(env["PHYSICS_PREVIEW_UNIT"], "u01")

    def test_invalid_ids_and_uncreated_lessons_fail_clearly(self):
        for lesson, unit in (("L99", None), ("L02", None), ("L01", "../bad")):
            with self.subTest(lesson=lesson, unit=unit):
                with self.assertRaises(ValueError):
                    build_command(lesson, unit, "preview")


if __name__ == "__main__":
    unittest.main()
