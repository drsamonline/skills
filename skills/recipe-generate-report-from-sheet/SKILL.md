---
name: recipe-generate-report-from-sheet
description: Read data from a Google Sheet and create a formatted Google Docs report.
license: Apache-2.0
metadata:
  title: "recipe generate report from sheet"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-generate-report-from-sheet/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Generate a Google Docs Report from Sheet Data

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-docs`, `gws-drive`

Read data from a Google Sheet and create a formatted Google Docs report.

## Steps

1. Read the data: `gws sheets +read --spreadsheet SHEET_ID --range "Sales!A1:D"`
2. Create the report doc: `gws docs documents create --json '{"title": "Sales Report - January 2025"}'`
3. Write the report: `gws docs +write --document-id DOC_ID --text '## Sales Report - January 2025

### Summary
Total deals: 45
Revenue: $125,000

### Top Deals
1. Acme Corp - $25,000
2. Widget Inc - $18,000'`
4. Share with stakeholders: `gws drive permissions create --params '{"fileId": "DOC_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "cfo@company.com"}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-generate-report-from-sheet/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
