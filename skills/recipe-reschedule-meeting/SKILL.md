---
name: recipe-reschedule-meeting
description: Move a Google Calendar event to a new time and automatically notify all attendees.
license: Apache-2.0
metadata:
  title: "recipe reschedule meeting"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-reschedule-meeting/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Reschedule a Google Calendar Meeting

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Move a Google Calendar event to a new time and automatically notify all attendees.

## Steps

1. Find the event: `gws calendar +agenda`
2. Get event details: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
3. Update the time: `gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{"start": {"dateTime": "2025-01-22T14:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2025-01-22T15:00:00", "timeZone": "America/New_York"}}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-reschedule-meeting/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
