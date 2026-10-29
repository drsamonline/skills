---
name: recipe-log-deal-update
description: Append a deal status update to a Google Sheets sales tracking spreadsheet.
license: Apache-2.0
metadata:
  title: "recipe log deal update"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-log-deal-update/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Log Deal Update to Sheet

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Append a deal status update to a Google Sheets sales tracking spreadsheet.

## Steps

1. Find the tracking sheet: `gws drive files list --params '{"q": "name = '\''Sales Pipeline'\'' and mimeType = '\''application/vnd.google-apps.spreadsheet'\''"}'`
2. Read current data: `gws sheets +read --spreadsheet SHEET_ID --range "Pipeline!A1:F"`
3. Append new row: `gws sheets +append --spreadsheet SHEET_ID --range 'Pipeline' --values '["2024-03-15", "Acme Corp", "Proposal Sent", "$50,000", "Q2", "jdoe"]'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-log-deal-update/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
