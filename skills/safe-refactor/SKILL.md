---
name: safe-refactor
description: Restructure code while preserving behavior. Use for extraction, consolidation, ownership moves, or cleanup where verification must bracket structural edits.
license: Apache-2.0
metadata:
  title: "safe refactor"
  origin: "JuliusBrussee/caveman"
  upstream-path: "skills/safe-refactor/SKILL.md"
  upstream-commit: "9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4"
  category: "engineering-workflow"
---

# Safe refactor

Define behavior-preservation boundary and establish verification before structural edits.

- Keep feature changes outside refactor.
- Move one ownership boundary at a time.
- Preserve public interfaces, failure behavior, ordering, and compatibility unless explicitly scoped.
- Keep intermediate states buildable and testable.
- Avoid dependency or configuration growth without correctness need.

Run same proof after change. Stop when behavior matches and requested structure is achieved.

## Provenance

Imported from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) at commit `9b68f7e`, path `skills/safe-refactor/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
