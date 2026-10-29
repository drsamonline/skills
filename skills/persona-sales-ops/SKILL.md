---
name: persona-sales-ops
description: Manage sales workflows — track deals, schedule calls, client comms.
license: Apache-2.0
metadata:
  title: "persona sales ops"
  origin: "googleworkspace/cli"
  upstream-path: "skills/persona-sales-ops/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Sales Operations

> **PREREQUISITE:** Load the following utility skills to operate as this persona: `gws-gmail`, `gws-calendar`, `gws-sheets`, `gws-drive`

Manage sales workflows — track deals, schedule calls, client comms.

## Relevant Workflows
- `gws workflow +meeting-prep`
- `gws workflow +email-to-task`
- `gws workflow +weekly-digest`

## Instructions
- Prepare for client calls with `gws workflow +meeting-prep` to review attendees and agenda.
- Log deal updates in a tracking spreadsheet with `gws sheets +append`.
- Convert follow-up emails into tasks with `gws workflow +email-to-task`.
- Share proposals by uploading to Drive with `gws drive +upload`.
- Get a weekly sales pipeline summary with `gws workflow +weekly-digest`.

## Tips
- Use `gws gmail +triage --query 'from:client-domain.com'` to filter client emails.
- Schedule follow-up calls immediately after meetings to maintain momentum.
- Keep all client-facing documents in a dedicated shared Drive folder.

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/persona-sales-ops/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
