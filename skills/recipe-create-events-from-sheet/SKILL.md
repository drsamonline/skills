---
name: recipe-create-events-from-sheet
description: Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row.
license: Apache-2.0
metadata:
  title: "recipe create events from sheet"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-events-from-sheet/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create Google Calendar Events from a Sheet

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-calendar`

Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row.

## Steps

1. Read event data: `gws sheets +read --spreadsheet SHEET_ID --range "Events!A2:D"`
2. For each row, create a calendar event: `gws calendar +insert --summary 'Team Standup' --start '2026-01-20T09:00:00' --end '2026-01-20T09:30:00' --attendee alice@company.com --attendee bob@company.com`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-events-from-sheet/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
