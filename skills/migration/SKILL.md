---
name: migration
description: Implement reversible compatibility-safe transitions. Use for schema, data, API, protocol, configuration, or dependency migrations requiring rollback and preservation proof.
license: Apache-2.0
metadata:
  title: "migration"
  origin: "JuliusBrussee/caveman"
  upstream-path: "skills/migration/SKILL.md"
  upstream-commit: "9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4"
  category: "engineering-workflow"
---

# Migration

Map current readers, writers, data shape, compatibility window, and ownership before editing.

- Define forward path and rollback path.
- Preserve existing data; make destructive steps explicit and separately authorized.
- Keep mixed-version operation safe where rollout can overlap.
- Sequence expand, migrate, verify, then contract when applicable.
- Make retries idempotent and partial failure observable.
- Verify old and new paths at required transition stages.

Stop after requested stage passes; do not perform later destructive contraction implicitly.

## Provenance

Imported from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) at commit `9b68f7e`, path `skills/migration/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
