---
name: recipe-find-free-time
description: Query Google Calendar free/busy status for multiple users to find a meeting slot.
license: Apache-2.0
metadata:
  title: "recipe find free time"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-find-free-time/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Find Free Time Across Calendars

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Query Google Calendar free/busy status for multiple users to find a meeting slot.

## Steps

1. Query free/busy: `gws calendar freebusy query --json '{"timeMin": "2024-03-18T08:00:00Z", "timeMax": "2024-03-18T18:00:00Z", "items": [{"id": "user1@company.com"}, {"id": "user2@company.com"}]}'`
2. Review the output to find overlapping free slots
3. Create event in the free slot: `gws calendar +insert --summary 'Meeting' --attendee user1@company.com --attendee user2@company.com --start '2024-03-18T14:00:00' --end '2024-03-18T14:30:00'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-find-free-time/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
