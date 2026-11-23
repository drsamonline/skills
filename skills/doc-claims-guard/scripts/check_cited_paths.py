#!/usr/bin/env python3
"""Every tree-qualified path a document names must exist.

A document that points at `src/lexora/ingest.py` is making a checkable claim. A renamed or deleted
file leaves a citation that reads perfectly and leads nowhere — which is how a README kept saying
"ingestion is not implemented yet" long after `src/…/ingest.py` shipped with 15 tests.

Dependency-free, and deliberately narrow: only paths in trees the repository owns are checked, so a
bare filename in prose (`pyproject.toml`, illustrative snippets) does not turn this into a
spell-checker for the whole document.

    python check_cited_paths.py --root . README.md docs/ROADMAP.md docs/STATUS.md
    python check_cited_paths.py --root . --prefixes src tests packages benchmarks scripts docs

Exit 0 when every citation resolves, 1 otherwise, with one line per miss.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

DEFAULT_PREFIXES = ("src", "tests", "packages", "benchmarks", "scripts")

# `path/in/a/tree.ext` inside backticks. The extension matters: it keeps `src/…/` directory
# references and prose fragments out of the check.
CITED = re.compile(r"`((?:{prefixes})/[A-Za-z0-9_./-]+\.[A-Za-z0-9]+)`")


def find_missing(root: pathlib.Path, documents: list[pathlib.Path],
                 prefixes: tuple[str, ...]) -> list[str]:
    pattern = re.compile(CITED.pattern.format(prefixes="|".join(re.escape(p) for p in prefixes)))
    missing: list[str] = []
    for doc in documents:
        text = doc.read_text(encoding="utf-8", errors="replace")
        for cited in sorted(set(pattern.findall(text))):
            if not (root / cited).exists():
                try:
                    shown = doc.relative_to(root)
                except ValueError:
                    shown = doc
                missing.append(f"{shown} cites `{cited}`, which does not exist")
    return missing


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path("."))
    ap.add_argument("--prefixes", nargs="+", default=list(DEFAULT_PREFIXES),
                    help="tree prefixes to treat as citations (default: src tests packages benchmarks scripts)")
    ap.add_argument("documents", nargs="+", type=pathlib.Path)
    args = ap.parse_args(argv)

    root = args.root.resolve()
    docs = [(d if d.is_absolute() else root / d) for d in args.documents]
    absent = [str(d) for d in docs if not d.is_file()]
    if absent:
        print("refused: these documents do not exist: " + ", ".join(absent), file=sys.stderr)
        return 2

    missing = find_missing(root, docs, tuple(args.prefixes))
    if missing:
        print(f"{len(missing)} citation(s) lead nowhere:")
        for line in missing:
            print(f"  {line}")
        print("\nA citation that does not resolve reads fine and is a lie. Fix the path, or "
              "remove the claim it supports.")
        return 1
    print(f"ok: {len(docs)} document(s), every cited path exists")
    return 0


if __name__ == "__main__":
    sys.exit(main())
