---
name: ponytail-debt
description: Every deliberate ponytail shortcut is marked with a shortcut: comment naming its ceiling and upgrade path (older code may say ponytail:). This collects them into one ledger so a deferral can't quietly become permanent.
license: MIT
metadata:
  title: "ponytail debt"
  origin: "DietrichGebert/ponytail"
  upstream-path: "skills/ponytail-debt/SKILL.md"
  upstream-commit: "96608e078b2d5ea607c5c3b8b5a54d1c1fba6846"
  category: "engineering-workflow"
  description-source: "derived from the body — upstream ships an empty description"
---

Every deliberate ponytail shortcut is marked with a `shortcut:` comment naming
its ceiling and upgrade path (older code may say `ponytail:`). This collects them into one ledger so a deferral
can't quietly become permanent.

## Scan

Grep the repo for comment markers, skipping `.git` and everything the
`.gitignore` files ignore (dependencies, build output, caches, in any stack):

`git grep --no-index --exclude-standard -nE '(#|//|/[*]) ?(shortcut|ponytail):'`  (add other comment prefixes if your stack uses them)

If the user names their own marker word (`/ponytail-debt TODO`), grep for that word instead.

Each hit is one ledger row. The comment prefix keeps prose that merely mentions
the convention out of the ledger. Skip hits that are not a deferral, like a note
about a keyboard shortcut.

## Output

One row per marker, grouped by file:

`<file>:<line>, <what was simplified>. ceiling: <the limit named>. upgrade: <the trigger to revisit>.`

The convention is `shortcut: <ceiling>, <upgrade path>`, so pull the ceiling
and the trigger straight from the comment. Want an owner per row too? add
`git blame -L<line>,<line>`.

Flag the rot risk: any marker comment that names no upgrade path or
trigger gets a `no-trigger` tag, those are the ones that silently rot.

End with `<N> markers, <M> with no trigger.` Nothing found: `No shortcut debt. Clean ledger.`

## Boundaries

Reads and reports only, changes nothing. To persist it, ask and it writes the
ledger to a file (e.g. `PONYTAIL-DEBT.md`). One-shot.

## Provenance

Imported from [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) at commit `96608e0`, path `skills/ponytail-debt/SKILL.md`. Licensed MIT by its authors — the full text is in `LICENSE`.
