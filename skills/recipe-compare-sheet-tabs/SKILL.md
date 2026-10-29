---
name: recipe-compare-sheet-tabs
description: Read data from two tabs in a Google Sheet to compare and identify differences.
license: Apache-2.0
metadata:
  title: "recipe compare sheet tabs"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-compare-sheet-tabs/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Compare Two Google Sheets Tabs

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`

Read data from two tabs in a Google Sheet to compare and identify differences.

## Steps

1. Read the first tab: `gws sheets +read --spreadsheet SHEET_ID --range "January!A1:D"`
2. Read the second tab: `gws sheets +read --spreadsheet SHEET_ID --range "February!A1:D"`
3. Compare the data and identify changes

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-compare-sheet-tabs/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
