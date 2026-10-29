---
name: surgical-patch
description: Fix bugs and small behavior changes at the narrowest responsible layer. Use when regression proof, preserved surrounding behavior, and task-relevant tests matter.
license: Apache-2.0
metadata:
  title: "surgical patch"
  origin: "JuliusBrussee/caveman"
  upstream-path: "skills/surgical-patch/SKILL.md"
  upstream-commit: "9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4"
  category: "engineering-workflow"
---

# Surgical patch

Reproduce failure first when economical; otherwise capture strongest available evidence.

- Trace symptom to responsible mechanism.
- Change narrowest layer that owns incorrect behavior.
- Preserve unrelated behavior and user changes.
- Avoid cleanup, renaming, and abstraction outside fix.
- Add only regression proof relevant to task.

Run focused proof plus nearest affected gate. Stop when failure is fixed and regression proof passes.

## Provenance

Imported from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) at commit `9b68f7e`, path `skills/surgical-patch/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
