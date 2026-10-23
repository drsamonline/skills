#!/usr/bin/env python3
"""Validate every skill against the Agent Skills specification.

    python3 scripts/validate.py

Spec: https://agentskills.io/specification

Checks, per skills/<dir>/SKILL.md:
  * SKILL.md exists and starts with YAML frontmatter
  * name: present, 1-64 chars, [a-z0-9] and single hyphens only,
          no leading/trailing/consecutive hyphen, and equals the folder name
  * description: present, 1-1024 chars
  * compatibility: if present, 1-500 chars
Exits 1 if anything fails, so CI can gate on it.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "skills"))
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm = {}
    for line in text[3:end].splitlines():
        s = line.strip()
        if not s or s.startswith("#") or ":" not in s:
            continue
        k, v = s.split(":", 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def main():
    if not os.path.isdir(ROOT):
        print("no skills/ directory at %s" % ROOT)
        return 1
    errors, checked = [], 0
    for entry in sorted(os.listdir(ROOT)):
        d = os.path.join(ROOT, entry)
        if not os.path.isdir(d) or entry.startswith("."):
            continue
        md = os.path.join(d, "SKILL.md")
        if not os.path.exists(md):
            errors.append("%s: no SKILL.md" % entry)
            continue
        checked += 1
        fm = frontmatter(open(md, encoding="utf-8").read())
        if fm is None:
            errors.append("%s: SKILL.md has no YAML frontmatter" % entry)
            continue
        name = fm.get("name", "")
        desc = fm.get("description", "")
        comp = fm.get("compatibility", "")
        if not name:
            errors.append("%s: missing 'name'" % entry)
        elif name != entry:
            errors.append("%s: name is '%s' but must equal the folder name" % (entry, name))
        elif not NAME_RE.match(name) or len(name) > 64:
            errors.append("%s: name must be lowercase alnum with single hyphens, <=64 chars" % entry)
        if not desc:
            errors.append("%s: missing 'description'" % entry)
        elif len(desc) > 1024:
            errors.append("%s: description is %d chars (max 1024)" % (entry, len(desc)))
        if comp and len(comp) > 500:
            errors.append("%s: compatibility is %d chars (max 500)" % (entry, len(comp)))

    print("checked %d skill(s)" % checked)
    if errors:
        print("\n%d problem(s):" % len(errors))
        for e in errors:
            print("  -", e)
        return 1
    print("all skills conform to the Agent Skills specification")
    return 0


if __name__ == "__main__":
    sys.exit(main())
