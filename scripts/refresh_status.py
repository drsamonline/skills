#!/usr/bin/env python3
"""Rewrite the generated status block in any skill that declares a `status_source`.

A skill's prose is a judgement call and this script does not touch it. What it does touch is
the handful of facts a source repository can publish itself — version, size, counts — which
otherwise get copied in by hand and then quietly go stale. The NEO skill claimed v0.6.0 for a
week after v0.7.0 shipped exactly that way.

Declare the source in `skills/<id>/meta.json`:

    "status_source": { "repo": "NEO", "path": "docs/status.json", "branch": "master" }

and put the block in `SKILL.md` where the facts belong:

    <!-- status:begin -->
    ...generated...
    <!-- status:end -->

Anything between the markers is replaced. Nothing else is touched. A skill with no
`status_source`, or no markers, is left alone — the script never creates the block, because
where it goes is an editorial decision.

    python3 scripts/refresh_status.py            # rewrite in place
    python3 scripts/refresh_status.py --check    # exit 1 if any block is stale

No dependencies beyond the standard library, matching the repository's house rule.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
OWNER = "drsamonline"
BEGIN = "<!-- status:begin -->"
END = "<!-- status:end -->"

BLOCK_RE = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)


def fetch(repo: str, path: str, branch: str) -> dict | None:
    url = f"https://raw.githubusercontent.com/{OWNER}/{repo}/{branch}/{path}"
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, TimeoutError) as error:
        print(f"  ! could not read {url}: {error}")
        return None


def render(status: dict) -> str:
    """The block, as markdown, from whatever the source published."""
    rows: list[tuple[str, str]] = []

    if "version" in status:
        rows.append(("Version", f"`{status['version']}`"))

    loc = status.get("loc") or {}
    if "compiler_src" in loc and "workspace" in loc:
        rows.append(
            ("Rust", f"{loc['compiler_src']:,} lines in `compiler/src`, {loc['workspace']:,} across the workspace")
        )

    if "adrs" in status:
        rows.append(("ADRs", str(status["adrs"])))

    if status.get("gates"):
        rows.append(("Gates (no toolchain)", ", ".join(f"`{gate}`" for gate in status["gates"])))

    stdlib = status.get("stdlib") or {}
    if "modules" in stdlib:
        listed = stdlib.get("listed_as_not_compiling", 0)
        rows.append(
            ("Standard library", f"{stdlib['modules']} modules, {listed} listed as not compiling")
        )

    body = "\n".join(f"| {left} | {right} |" for left, right in rows)
    return f"{BEGIN}\n| | |\n|---|---|\n{body}\n{END}"


def refresh(check_only: bool) -> int:
    stale = 0
    updated = 0
    considered = 0

    for meta_path in sorted(SKILLS.glob("*/meta.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        source = meta.get("status_source")
        if not source:
            continue
        considered += 1

        skill_path = meta_path.parent / "SKILL.md"
        if not skill_path.is_file():
            continue
        text = skill_path.read_text(encoding="utf-8")
        if not BLOCK_RE.search(text):
            print(f"  ! {meta['id']}: declares a status_source but SKILL.md has no {BEGIN} block")
            continue

        status = fetch(source["repo"], source["path"], source.get("branch", "main"))
        if status is None:
            continue

        new_text = BLOCK_RE.sub(lambda _: render(status), text, count=1)
        if new_text == text:
            continue

        stale += 1
        if check_only:
            print(f"  {meta['id']}: block is stale")
        else:
            skill_path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(f"  {meta['id']}: block refreshed")

    if check_only:
        if stale:
            print(f"{stale} stale block(s) — run python3 scripts/refresh_status.py")
            return 1
        print(f"status blocks current ({considered} skill(s) declare a source)")
        return 0

    if updated == 0:
        print(f"status blocks already current ({considered} skill(s) declare a source)")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    return refresh(parser.parse_args(argv).check)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
