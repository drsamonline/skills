---
name: recipe-plan-weekly-schedule
description: Review your Google Calendar week, identify gaps, and add events to fill them.
license: Apache-2.0
metadata:
  title: "recipe plan weekly schedule"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-plan-weekly-schedule/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Plan Your Weekly Google Calendar Schedule

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Review your Google Calendar week, identify gaps, and add events to fill them.

## Steps

1. Check this week's agenda: `gws calendar +agenda`
2. Check free/busy for the week: `gws calendar freebusy query --json '{"timeMin": "2025-01-20T00:00:00Z", "timeMax": "2025-01-25T00:00:00Z", "items": [{"id": "primary"}]}'`
3. Add a new event: `gws calendar +insert --summary 'Deep Work Block' --start '2026-01-21T14:00:00' --end '2026-01-21T16:00:00'`
4. Review updated schedule: `gws calendar +agenda`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-plan-weekly-schedule/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
