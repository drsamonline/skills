---
name: recipe-post-mortem-setup
description: Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat.
license: Apache-2.0
metadata:
  title: "recipe post mortem setup"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-post-mortem-setup/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Set Up Post-Mortem

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-docs`, `gws-calendar`, `gws-chat`

Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat.

## Steps

1. Create post-mortem doc: `gws docs +write --title 'Post-Mortem: [Incident]' --body '## Summary\n\n## Timeline\n\n## Root Cause\n\n## Action Items'`
2. Schedule review meeting: `gws calendar +insert --summary 'Post-Mortem Review: [Incident]' --attendee team@company.com --start '2026-03-16T14:00:00' --end '2026-03-16T15:00:00'`
3. Notify in Chat: `gws chat +send --space spaces/ENG_SPACE --text '🔍 Post-mortem scheduled for [Incident].'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-post-mortem-setup/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
