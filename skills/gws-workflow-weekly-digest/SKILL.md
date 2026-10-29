---
name: gws-workflow-weekly-digest
description: Google Workflow: Weekly summary: this week's meetings + unread email count.
license: Apache-2.0
metadata:
  title: "gws workflow weekly digest"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-workflow-weekly-digest/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# workflow +weekly-digest

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Weekly summary: this week's meetings + unread email count

## Usage

```bash
gws workflow +weekly-digest
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--format` | — | — | Output format: json (default), table, yaml, csv |

## Examples

```bash
gws workflow +weekly-digest
gws workflow +weekly-digest --format table
```

## Tips

- Read-only — never modifies data.
- Combines calendar agenda (week) with gmail triage summary.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-workflow](../gws-workflow/SKILL.md) — All cross-service productivity workflows commands

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-workflow-weekly-digest/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
