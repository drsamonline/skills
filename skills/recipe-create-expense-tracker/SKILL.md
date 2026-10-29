---
name: recipe-create-expense-tracker
description: Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries.
license: Apache-2.0
metadata:
  title: "recipe create expense tracker"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-expense-tracker/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create a Google Sheets Expense Tracker

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries.

## Steps

1. Create spreadsheet: `gws drive files create --json '{"name": "Expense Tracker 2025", "mimeType": "application/vnd.google-apps.spreadsheet"}'`
2. Add headers: `gws sheets +append --spreadsheet SHEET_ID --range 'Sheet1' --values '["Date", "Category", "Description", "Amount"]'`
3. Add first entry: `gws sheets +append --spreadsheet SHEET_ID --range 'Sheet1' --values '["2025-01-15", "Travel", "Flight to NYC", "450.00"]'`
4. Share with manager: `gws drive permissions create --params '{"fileId": "SHEET_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "manager@company.com"}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-expense-tracker/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
