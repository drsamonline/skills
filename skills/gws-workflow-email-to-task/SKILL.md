---
name: gws-workflow-email-to-task
description: Google Workflow: Convert a Gmail message into a Google Tasks entry.
license: Apache-2.0
metadata:
  title: "gws workflow email to task"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-workflow-email-to-task/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# workflow +email-to-task

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Convert a Gmail message into a Google Tasks entry

## Usage

```bash
gws workflow +email-to-task --message-id <ID>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--message-id` | ✓ | — | Gmail message ID to convert |
| `--tasklist` | — | @default | Task list ID (default: @default) |

## Examples

```bash
gws workflow +email-to-task --message-id MSG_ID
gws workflow +email-to-task --message-id MSG_ID --tasklist LIST_ID
```

## Tips

- Reads the email subject as the task title and snippet as notes.
- Creates a new task — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-workflow](../gws-workflow/SKILL.md) — All cross-service productivity workflows commands

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-workflow-email-to-task/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
