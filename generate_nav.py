#!/usr/bin/env python3
"""Auto-generate the nav section of mkdocs.yml from the docs/ directory structure.

Rules:
- docs/index.md is always the "Home" entry.
- Each subdirectory of docs/ becomes a nav section, titled by converting the
  directory name to title case (hyphens/underscores become spaces).
- Files within a section are sorted alphabetically (numeric prefixes like
  "01-" keep them in order without appearing in the title).
- The page title is taken from the first H1 heading in the file; if none is
  found, the filename is used as a fallback.
"""

import os
import re
import yaml

DOCS_DIR = "docs"
MKDOCS_FILE = "mkdocs.yml"


def get_title(filepath: str) -> str:
    """Return the first H1 heading in a Markdown file, or a derived fallback."""
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    # Fallback: strip numeric prefix, replace separators, title-case
    name = os.path.splitext(os.path.basename(filepath))[0]
    name = re.sub(r"^\d+-", "", name)
    return name.replace("-", " ").replace("_", " ").title()


def section_title(dirname: str) -> str:
    return dirname.replace("-", " ").replace("_", " ").title()


def build_nav() -> list:
    nav = [{"Home": "index.md"}]

    subdirs = sorted(
        d for d in os.listdir(DOCS_DIR)
        if os.path.isdir(os.path.join(DOCS_DIR, d)) and not d.startswith(".")
    )

    for subdir in subdirs:
        subdir_path = os.path.join(DOCS_DIR, subdir)
        md_files = sorted(
            f for f in os.listdir(subdir_path)
            if f.endswith(".md") and not f.startswith(".")
        )

        if not md_files:
            continue

        entries = [
            {get_title(os.path.join(subdir_path, f)): f"{subdir}/{f}"}
            for f in md_files
        ]
        nav.append({section_title(subdir): entries})

    return nav


def main() -> None:
    with open(MKDOCS_FILE, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    config["nav"] = build_nav()

    with open(MKDOCS_FILE, "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print(f"Updated nav in {MKDOCS_FILE}.")


if __name__ == "__main__":
    main()