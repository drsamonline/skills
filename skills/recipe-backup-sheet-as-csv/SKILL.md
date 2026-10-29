---
name: recipe-backup-sheet-as-csv
description: Export a Google Sheets spreadsheet as a CSV file for local backup or processing.
license: Apache-2.0
metadata:
  title: "recipe backup sheet as csv"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-backup-sheet-as-csv/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Export a Google Sheet as CSV

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Export a Google Sheets spreadsheet as a CSV file for local backup or processing.

## Steps

1. Get spreadsheet details: `gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'`
2. Export as CSV: `gws drive files export --params '{"fileId": "SHEET_ID", "mimeType": "text/csv"}'`
3. Or read values directly: `gws sheets +read --spreadsheet SHEET_ID --range 'Sheet1' --format csv`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-backup-sheet-as-csv/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
