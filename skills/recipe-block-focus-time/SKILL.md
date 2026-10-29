---
name: recipe-block-focus-time
description: Create recurring focus time blocks on Google Calendar to protect deep work hours.
license: Apache-2.0
metadata:
  title: "recipe block focus time"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-block-focus-time/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Block Focus Time on Google Calendar

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Create recurring focus time blocks on Google Calendar to protect deep work hours.

## Steps

1. Create recurring focus block: `gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Focus Time", "description": "Protected deep work block", "start": {"dateTime": "2025-01-20T09:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2025-01-20T11:00:00", "timeZone": "America/New_York"}, "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"], "transparency": "opaque"}'`
2. Verify it shows as busy: `gws calendar +agenda`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-block-focus-time/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
