"""Explicit user-operated Manim launcher. --print-command never renders."""

import argparse
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PROFILES = {"preview": (854, 480, 15), "final": (1920, 1080, 30)}


def build_command(lesson_id: str, unit: str | None, profile: str) -> tuple[list[str], dict[str, str]]:
    """Resolve a portable command and environment without running Manim."""
    catalogue = tomllib.loads((ROOT / "course.toml").read_text(encoding="utf-8"))
    if lesson_id not in catalogue["lessons"]:
        raise ValueError(f"Unknown lesson: {lesson_id}")
    if unit is not None and not re.fullmatch(r"(?:intro|u[0-9]{2,})", unit):
        raise ValueError("Use intro for the introduction, or unit IDs such as u01, u02, or u100.")
    entry = catalogue["lessons"][lesson_id]
    scene_file = ROOT / entry["source"]
    if not scene_file.is_file():
        raise ValueError(f"{lesson_id} is reserved but has no source folder yet.")
    width, height, fps = PROFILES[profile]
    selection = unit or "full"
    output = ROOT / "build" / lesson_id / selection / profile
    # Unique lesson/unit/profile paths prevent previews overwriting full videos.
    filename = f"{lesson_id}_{entry['slug']}" + (f"_{unit}" if unit else "")
    command = [
        # --preview opens the completed MP4 in the default video player on
        # macOS/Windows. It does not change the selected quality profile.
        # Remove this flag if you later want to render without opening playback.
        sys.executable, "-m", "manim", "--preview", "--config_file", str(ROOT / "manim.cfg"),
        "--media_dir", str(output), "--resolution", f"{width},{height}",
        "--fps", str(fps), "--output_file", filename,
        str(scene_file), entry["scene"],
    ]
    env = os.environ.copy()
    # Remove a stale preview target so a full render always runs the full order.
    env.pop("PHYSICS_PREVIEW_UNIT", None)
    if unit:
        env["PHYSICS_PREVIEW_UNIT"] = unit
    env["PYTHONPATH"] = str(ROOT) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
    return command, env


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lesson", help="Catalogue ID, e.g. L01")
    parser.add_argument("--unit", help="Preview the intro or one implemented unit, e.g. intro or u01")
    parser.add_argument("--profile", choices=PROFILES, default="preview")
    parser.add_argument("--print-command", action="store_true", help="Display the command; do not render")
    args = parser.parse_args()
    try:
        command, env = build_command(args.lesson, args.unit, args.profile)
    except (ValueError, KeyError) as error:
        parser.error(str(error))
    if args.print_command:
        print("Working directory:", ROOT)
        if args.unit:
            print("Preview environment: PHYSICS_PREVIEW_UNIT=" + args.unit)
        print(subprocess.list2cmdline(command) if os.name == "nt" else shlex.join(command))
        print("Informational only: printing a command does not confirm the unit is implemented.")
        return 0
    # ONLY running this launcher without --print-command invokes rendering.
    # The project assistant must not execute this branch.
    return subprocess.run(command, cwd=ROOT, env=env, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
