---
name: recipe-copy-sheet-for-new-month
description: Duplicate a Google Sheets template tab for a new month of tracking.
license: Apache-2.0
metadata:
  title: "recipe copy sheet for new month"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-copy-sheet-for-new-month/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Copy a Google Sheet for a New Month

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`

Duplicate a Google Sheets template tab for a new month of tracking.

## Steps

1. Get spreadsheet details: `gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'`
2. Copy the template sheet: `gws sheets spreadsheets sheets copyTo --params '{"spreadsheetId": "SHEET_ID", "sheetId": 0}' --json '{"destinationSpreadsheetId": "SHEET_ID"}'`
3. Rename the new tab: `gws sheets spreadsheets batchUpdate --params '{"spreadsheetId": "SHEET_ID"}' --json '{"requests": [{"updateSheetProperties": {"properties": {"sheetId": 123, "title": "February 2025"}, "fields": "title"}}]}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-copy-sheet-for-new-month/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
