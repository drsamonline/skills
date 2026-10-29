---
name: recipe-share-event-materials
description: Share Google Drive files with all attendees of a Google Calendar event.
license: Apache-2.0
metadata:
  title: "recipe share event materials"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-share-event-materials/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Share Files with Meeting Attendees

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`, `gws-drive`

Share Google Drive files with all attendees of a Google Calendar event.

## Steps

1. Get event attendees: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
2. Share file with each attendee: `gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "attendee@company.com"}'`
3. Verify sharing: `gws drive permissions list --params '{"fileId": "FILE_ID"}' --format table`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-share-event-materials/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
