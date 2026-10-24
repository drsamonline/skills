#!/usr/bin/env python3
"""Validate every skill against the Agent Skills standard.

    python3 validate.py            # check every skill
    python3 validate.py --quiet    # exit code only

Rules checked, from the published specification at agentskills.io/specification:

  name         1-64 characters; lowercase letters, digits and single hyphens only;
               no leading or trailing hyphen; no consecutive hyphens; and it must
               equal the folder name.
  description  1-1024 characters, present.
  layout       a directory holding SKILL.md with YAML frontmatter.

NON-DIRECTORY ENTRIES ARE SKIPPED, not failed. This repository contains a
.gitkeep, and a validator that reports a placeholder file as a broken skill is a
validator people stop running.

No dependencies beyond the standard library. Zero-dependency is the house rule for
what we ship, and a validator is the last place to break it.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ROOT = Path(__file__).resolve().parent


def frontmatter(text: str) -> dict | None:
    """The YAML frontmatter, parsed just enough for name and description.

    Deliberately not a YAML parser: the two fields we need are single-line strings,
    and importing a parser would add a dependency to the one script that must run
    anywhere.
    """
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def check_skill(d: Path) -> list[str]:
    errs: list[str] = []
    md = d / "SKILL.md"
    if not md.is_file():
        return [f"{d.name}: no SKILL.md"]
    fm = frontmatter(md.read_text(encoding="utf-8", errors="replace"))
    if fm is None:
        return [f"{d.name}: SKILL.md has no YAML frontmatter"]

    name = fm.get("name", "")
    if not name:
        errs.append(f"{d.name}: frontmatter has no name")
    else:
        if not (1 <= len(name) <= 64):
            errs.append(f"{d.name}: name is {len(name)} chars, must be 1-64")
        if not NAME_RE.match(name):
            errs.append(f"{d.name}: name {name!r} must be lowercase letters, digits "
                        "and single hyphens, with no leading, trailing or doubled hyphen")
        if name != d.name:
            errs.append(f"{d.name}: name {name!r} must equal the folder name")

    desc = fm.get("description", "")
    if not desc:
        errs.append(f"{d.name}: frontmatter has no description")
    elif not (1 <= len(desc) <= 1024):
        errs.append(f"{d.name}: description is {len(desc)} chars, must be 1-1024")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    dirs = sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith("."))
    skipped = [p.name for p in ROOT.iterdir() if not p.is_dir()]
    all_errs: list[str] = []
    for d in dirs:
        all_errs.extend(check_skill(d))

    if not a.quiet:
        print(f"skills checked: {len(dirs)}")
        if skipped:
            print(f"skipped (not a directory, so not a skill): {', '.join(sorted(skipped))}")
        if all_errs:
            print(f"\nFAILED {len(all_errs)}:")
            for e in all_errs:
                print("   " + e)
        else:
            print("all conform to the Agent Skills standard (name, description, layout)")
    return 1 if all_errs else 0


if __name__ == "__main__":
    sys.exit(main())
