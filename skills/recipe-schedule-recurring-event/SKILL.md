---
name: recipe-schedule-recurring-event
description: Create a recurring Google Calendar event with attendees.
license: Apache-2.0
metadata:
  title: "recipe schedule recurring event"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-schedule-recurring-event/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Schedule a Recurring Meeting

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Create a recurring Google Calendar event with attendees.

## Steps

1. Create recurring event: `gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Weekly Standup", "start": {"dateTime": "2024-03-18T09:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2024-03-18T09:30:00", "timeZone": "America/New_York"}, "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO"], "attendees": [{"email": "team@company.com"}]}'`
2. Verify it was created: `gws calendar +agenda --days 14 --format table`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-schedule-recurring-event/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
