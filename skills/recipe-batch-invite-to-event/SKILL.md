---
name: recipe-batch-invite-to-event
description: Add a list of attendees to an existing Google Calendar event and send notifications.
license: Apache-2.0
metadata:
  title: "recipe batch invite to event"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-batch-invite-to-event/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Add Multiple Attendees to a Calendar Event

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Add a list of attendees to an existing Google Calendar event and send notifications.

## Steps

1. Get the event: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
2. Add attendees: `gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{"attendees": [{"email": "alice@company.com"}, {"email": "bob@company.com"}, {"email": "carol@company.com"}]}'`
3. Verify attendees: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-batch-invite-to-event/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
