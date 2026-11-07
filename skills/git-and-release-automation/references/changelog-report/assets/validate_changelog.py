#!/usr/bin/env python3
"""Pre-flight checks for a rendered changelog HTML file.

Usage: python validate_changelog.py report.html

Exits 1 and prints every failure when the report would render wrong.
"""
import re
import sys

SECTIONS = {"new", "improved", "fixed", "removed", "hood"}


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s).strip()


def main(path: str) -> int:
    html = open(path, encoding="utf-8").read()
    fails = []

    # 1. unfilled placeholders
    leftover = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", html)))
    if leftover:
        fails.append(f"unfilled placeholders: {', '.join(leftover)}")

    # 2. section classes
    for cls in re.findall(r'<section class="([^"]+)"', html):
        mods = [c for c in cls.split() if c.startswith("changelog-section--")]
        if len(mods) != 1:
            fails.append(f"section needs exactly one modifier, got {mods or 'none'}")
        for m in mods:
            if m.replace("changelog-section--", "") not in SECTIONS:
                fails.append(f"unknown section modifier: {m!r}")

    # 3. entries
    blocks = re.findall(
        r'<div class="changelog-entry">(.*?)(?=<div class="changelog-entry">|</section>)',
        html,
        re.S,
    )
    if not blocks:
        fails.append("no entries found")

    for i, block in enumerate(blocks, 1):
        title = re.search(r'class="changelog-entry__title">(.*?)</h3>', block, re.S)
        if not title or not strip_tags(title.group(1)):
            fails.append(f"entry {i}: missing title")

        link = re.search(
            r'<a href="(https://github\.com/[^/]+/[^/]+/pull/\d+)">#(\d+)</a>', block
        )
        if not link:
            fails.append(f"entry {i}: missing or malformed PR link")
        elif link.group(2) not in link.group(1):
            fails.append(f"entry {i}: link text #{link.group(2)} does not match URL")

        date = re.search(r'class="changelog-entry__date">(.*?)</span>', block)
        if not date or not re.fullmatch(r"\d{1,2} [A-Z][a-z]{2}", strip_tags(date.group(1))):
            fails.append(f"entry {i}: merge date not in 'dd Mon' form")

        body = re.search(r'class="changelog-entry__text">(.*?)</p>', block, re.S)
        if not body or len(strip_tags(body.group(1))) < 40:
            fails.append(f"entry {i}: details missing or too short")
        elif len(re.findall(r"[.!?](\s|$)", strip_tags(body.group(1)))) > 3:
            fails.append(f"entry {i}: details exceed 3 sentences")

    # 4. template leakage
    for bad in ("org/repo", ">contributor<", "{{", "example.com"):
        if bad in html:
            fails.append(f"literal {bad!r} left in output")

    # 5. summary count agrees with entries
    summary = re.search(r'<div class="summary">(.*?)</div>', html, re.S)
    if not summary:
        fails.append("summary block missing")
    else:
        text = strip_tags(summary.group(1))
        nums = re.findall(r"\b(\d+)\b", text)
        if nums and int(nums[0]) != len(blocks):
            fails.append(
                f"summary says {nums[0]} PRs but {len(blocks)} entries rendered"
            )
        if "–" not in text and " - " not in text and "August" not in text:
            fails.append("summary does not state the window period")

    # 6. empty sections
    for section in re.findall(r"<section.*?</section>", html, re.S):
        if "changelog-entry" not in section:
            head = re.search(r'__heading">(.*?)</h2>', section)
            fails.append(f"empty section rendered: {strip_tags(head.group(1)) if head else '?'}")

    if fails:
        print(f"FAIL {path}")
        for f in fails:
            print("  -", f)
        return 1

    print(f"PASS {path} — {len(blocks)} entries, all checks clean")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_changelog.py report.html")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
