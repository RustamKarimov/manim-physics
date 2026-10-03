"""Check source/configuration without importing Manim or constructing scenes."""

import ast
import configparser
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    for base in (ROOT / "lessons", ROOT / "shared", ROOT / "tools", ROOT / "tests"):
        for source in base.rglob("*.py"):
            ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
    for source in (ROOT / "pyproject.toml", ROOT / "course.toml", ROOT / ".local/settings.example.toml"):
        tomllib.loads(source.read_text(encoding="utf-8"))
    # Manim directory placeholders use braces; disable ConfigParser interpolation.
    config = configparser.ConfigParser(interpolation=None)
    config.read(ROOT / "manim.cfg", encoding="utf-8")
    required = {"media_dir", "video_dir", "images_dir", "tex_dir", "text_dir", "log_dir", "partial_movie_dir", "sections_dir"}
    missing = required - set(config["CLI"])
    if missing:
        raise ValueError(f"Missing output settings: {sorted(missing)}")
    if config["CLI"].getboolean("save_sections"):
        raise ValueError("Section export should be disabled by default.")
    print("Source syntax, TOML, and Manim output configuration checked. No scenes rendered.")


if __name__ == "__main__":
    main()
