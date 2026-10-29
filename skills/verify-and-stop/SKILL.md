---
name: verify-and-stop
description: Prove existing work meets acceptance conditions without expanding scope. Use for validation-only tasks, completion checks, focused gate runs, and last-mile proof.
license: Apache-2.0
metadata:
  title: "verify and stop"
  origin: "JuliusBrussee/caveman"
  upstream-path: "skills/verify-and-stop/SKILL.md"
  upstream-commit: "9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4"
  category: "engineering-workflow"
---

# Verify and stop

Translate acceptance conditions into smallest sufficient proof set.

- Reuse still-current results with matching repository state.
- Run focused checks before wider gates.
- Distinguish pass, fail, unavailable, and blocked exactly.
- Do not edit product code unless verification request includes fixes.
- Do not add polish, cleanup, or unrelated tests after criteria pass.

Stop immediately when acceptance proof is complete. Report commands, results, and unresolved risk only.

## Provenance

Imported from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) at commit `9b68f7e`, path `skills/verify-and-stop/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
