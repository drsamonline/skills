---
name: gws-workflow-meeting-prep
description: Google Workflow: Prepare for your next meeting: agenda, attendees, and linked docs.
license: Apache-2.0
metadata:
  title: "gws workflow meeting prep"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-workflow-meeting-prep/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# workflow +meeting-prep

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Prepare for your next meeting: agenda, attendees, and linked docs

## Usage

```bash
gws workflow +meeting-prep
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--calendar` | — | primary | Calendar ID (default: primary) |
| `--format` | — | — | Output format: json (default), table, yaml, csv |

## Examples

```bash
gws workflow +meeting-prep
gws workflow +meeting-prep --calendar Work
```

## Tips

- Read-only — never modifies data.
- Shows the next upcoming event with attendees and description.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-workflow](../gws-workflow/SKILL.md) — All cross-service productivity workflows commands

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-workflow-meeting-prep/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
