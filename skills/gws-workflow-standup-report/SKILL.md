---
name: gws-workflow-standup-report
description: Google Workflow: Today's meetings + open tasks as a standup summary.
license: Apache-2.0
metadata:
  title: "gws workflow standup report"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-workflow-standup-report/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# workflow +standup-report

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Today's meetings + open tasks as a standup summary

## Usage

```bash
gws workflow +standup-report
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--format` | — | — | Output format: json (default), table, yaml, csv |

## Examples

```bash
gws workflow +standup-report
gws workflow +standup-report --format table
```

## Tips

- Read-only — never modifies data.
- Combines calendar agenda (today) with tasks list.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-workflow](../gws-workflow/SKILL.md) — All cross-service productivity workflows commands

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-workflow-standup-report/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
