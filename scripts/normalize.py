#!/usr/bin/env python3
"""Normalise every SKILL.md to the Agent Skills specification.

The spec requires `name` to be a lowercase slug equal to the folder name:
  https://agentskills.io/specification

Our skills historically put a human title in `name`. This rewrites

    name: Aethelgard Engine — vanilla-JS RPG engine

to

    name: aethelgard-engine-rpg
    metadata:
      title: Aethelgard Engine — vanilla-JS RPG engine

so the skill is spec-conformant AND the human title survives. Idempotent: a file
that already conforms is left untouched.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "skills"))
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def split(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end], text[end + 4:]


def main():
    changed = 0
    for entry in sorted(os.listdir(ROOT)):
        d = os.path.join(ROOT, entry)
        md = os.path.join(d, "SKILL.md")
        if not (os.path.isdir(d) and os.path.exists(md)):
            continue
        text = open(md, encoding="utf-8").read()
        parts = split(text)
        if not parts:
            print("skip (no frontmatter): %s" % entry)
            continue
        fm, body = parts
        lines = fm.strip("\n").splitlines()

        old_title, name_idx, has_title = None, None, False
        for i, ln in enumerate(lines):
            s = ln.strip()
            if s.startswith("name:"):
                name_idx = i
                old_title = s.split(":", 1)[1].strip().strip('"')
            if s.startswith("title:"):
                has_title = True

        if name_idx is None:
            lines.insert(0, "name: " + entry)
        else:
            lines[name_idx] = "name: " + entry

        if old_title and old_title != entry and not has_title:
            if not any(l.strip() == "metadata:" for l in lines):
                lines.append("metadata:")
            lines.append('  title: "%s"' % old_title.replace('"', '\\"'))

        new = "---\n" + "\n".join(lines) + "\n---" + body
        if new != text:
            with open(md, "w", encoding="utf-8") as f:
                f.write(new)
            changed += 1

    print("normalised %d skill(s)" % changed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
