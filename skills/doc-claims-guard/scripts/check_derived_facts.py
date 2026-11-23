#!/usr/bin/env python3
"""Read a fact from its source of truth, then assert the prose agrees with it.

This is the guard that catches the expensive ones. A landing page said "no releases yet" while the
CHANGELOG held two release headings, and nothing noticed for weeks — because the *fact* lived in one
file and the *sentence about it* lived in another, and no command compared them.

The rule it implements is deliberately small, so it can be explained in one line:

    if <pattern> appears in <source>, then <pattern> must (not) appear in <document>

A tiny config is more honest than a clever heuristic: every guard states its own fact, and the fact
is visible in the diff that adds it.

    python check_derived_facts.py --root . --config .doc-claims.json

`.doc-claims.json`:

    {
      "facts": [
        {
          "why": "two alpha tags are published",
          "source": "CHANGELOG.md",
          "source_pattern": "^## \\[?\\d+\\.\\d+\\.\\d+",
          "document": "docs/index.html",
          "forbidden": "no releases yet"
        },
        {
          "why": "the shipped default is quoted from a revision the register publishes",
          "source": "benchmarks/results-r5-heldout.json",
          "source_pattern": "\\"benchmark_revision\\": 5",
          "document": "README.md",
          "required": "0.3360"
        }
      ]
    }

`forbidden` and `required` are both optional; a fact may use either or both. Dependency-free.
Exit 0 when every fact agrees, 1 otherwise, 2 on a broken config.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys


def check(root: pathlib.Path, config: dict) -> tuple[list[str], list[str]]:
    problems: list[str] = []
    notes: list[str] = []
    for fact in config.get("facts", []):
        why = fact.get("why", "unnamed fact")
        source = root / fact["source"]
        document = root / fact["document"]
        if not source.is_file() or not document.is_file():
            problems.append(f"{why}: missing file ({fact['source']} or {fact['document']})")
            continue

        source_text = source.read_text(encoding="utf-8", errors="replace")
        doc_text = document.read_text(encoding="utf-8", errors="replace")
        pattern = fact.get("source_pattern")
        if pattern and not re.search(pattern, source_text, re.MULTILINE):
            notes.append(f"skipped: {why} — the fact is not present in {fact['source']}")
            continue

        for phrase in [fact["forbidden"]] if fact.get("forbidden") else []:
            if phrase.lower() in doc_text.lower():
                problems.append(
                    f"{why}: {fact['document']} still says {phrase!r} while {fact['source']} "
                    f"says otherwise"
                )
        for phrase in [fact["required"]] if fact.get("required") else []:
            if phrase not in doc_text:
                problems.append(
                    f"{why}: {fact['document']} does not contain {phrase!r}, which "
                    f"{fact['source']} says it should"
                )
    return problems, notes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path("."))
    ap.add_argument("--config", type=pathlib.Path, required=True)
    args = ap.parse_args(argv)

    try:
        config = json.loads(args.config.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"refused: cannot read {args.config}: {exc}", file=sys.stderr)
        return 2
    if not isinstance(config.get("facts"), list):
        print("refused: config has no 'facts' list", file=sys.stderr)
        return 2

    problems, notes = check(args.root.resolve(), config)
    for note in notes:
        print(note)
    if problems:
        print(f"\n{len(problems)} fact(s) disagree with the documents:")
        for line in problems:
            print(f"  {line}")
        print("\nThe fact is the authority. Fix the document, or fix the fact — but not by "
              "deleting the guard.")
        return 1
    print(f"ok: {len(config['facts'])} fact(s) agree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
