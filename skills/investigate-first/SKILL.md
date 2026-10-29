---
name: investigate-first
description: Diagnose ambiguous failures before editing. Use for unknown causes, intermittent behavior, performance regressions, or investigations needing evidence-ranked hypotheses.
license: Apache-2.0
metadata:
  title: "investigate first"
  origin: "JuliusBrussee/caveman"
  upstream-path: "skills/investigate-first/SKILL.md"
  upstream-commit: "9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4"
  category: "engineering-workflow"
---

# Investigate first

Gather evidence before changing product code.

- Separate observed symptom from inferred cause.
- Trace inputs, state transitions, ownership boundaries, and failure output.
- Rank hypotheses by evidence and cheap falsification value.
- Do not edit until one credible mechanism explains evidence.
- Stop exploration when evidence is sufficient to name cause or exact blocker.

Report cause and proof. Make no fix unless task authorizes implementation.

## Provenance

Imported from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) at commit `9b68f7e`, path `skills/investigate-first/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
