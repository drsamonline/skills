---
name: gws-workflow
description: Google Workflow: Cross-service productivity workflows.
license: Apache-2.0
metadata:
  title: "gws workflow"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-workflow/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# workflow (v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws workflow <resource> <method> [flags]
```

## Helper Commands

| Command | Description |
|---------|-------------|
| [`+standup-report`](../gws-workflow-standup-report/SKILL.md) | Today's meetings + open tasks as a standup summary |
| [`+meeting-prep`](../gws-workflow-meeting-prep/SKILL.md) | Prepare for your next meeting: agenda, attendees, and linked docs |
| [`+email-to-task`](../gws-workflow-email-to-task/SKILL.md) | Convert a Gmail message into a Google Tasks entry |
| [`+weekly-digest`](../gws-workflow-weekly-digest/SKILL.md) | Weekly summary: this week's meetings + unread email count |
| [`+file-announce`](../gws-workflow-file-announce/SKILL.md) | Announce a Drive file in a Chat space |

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws workflow --help

# Inspect a method's required params, types, and defaults
gws schema workflow.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-workflow/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
