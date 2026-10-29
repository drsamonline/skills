---
name: recipe-sync-contacts-to-sheet
description: Export Google Contacts directory to a Google Sheets spreadsheet.
license: Apache-2.0
metadata:
  title: "recipe sync contacts to sheet"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-sync-contacts-to-sheet/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Export Google Contacts to Sheets

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-people`, `gws-sheets`

Export Google Contacts directory to a Google Sheets spreadsheet.

## Steps

1. List contacts: `gws people people listDirectoryPeople --params '{"readMask": "names,emailAddresses,phoneNumbers", "sources": ["DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"], "pageSize": 100}' --format json`
2. Create a sheet: `gws sheets +append --spreadsheet SHEET_ID --range 'Contacts' --values '["Name", "Email", "Phone"]'`
3. Append each contact row: `gws sheets +append --spreadsheet SHEET_ID --range 'Contacts' --values '["Jane Doe", "jane@company.com", "+1-555-0100"]'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-sync-contacts-to-sheet/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
