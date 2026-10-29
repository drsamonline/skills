---
name: recipe-sheets
description: Sheets recipes — read, compare, duplicate, export, track. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "Sheets recipes — read, compare, duplicate, export, track"
  origin: "googleworkspace/cli"
  merged-from: "5 skills"
  category: "google-workspace"
---

# Sheets recipes — read, compare, duplicate, export, track

A merge of 5 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- Sheets recipes — read, compare, duplicate, export, track. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `recipe-backup-sheet-as-csv` | Export a Google Sheets spreadsheet as a CSV file for local backup or processing. |
| `recipe-compare-sheet-tabs` | Read data from two tabs in a Google Sheet to compare and identify differences. |
| `recipe-copy-sheet-for-new-month` | Duplicate a Google Sheets template tab for a new month of tracking. |
| `recipe-generate-report-from-sheet` | Read data from a Google Sheet and create a formatted Google Docs report. |
| `recipe-sync-contacts-to-sheet` | Export Google Contacts directory to a Google Sheets spreadsheet. |

## recipe-backup-sheet-as-csv

### Export a Google Sheet as CSV

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Export a Google Sheets spreadsheet as a CSV file for local backup or processing.

#### Steps

1. Get spreadsheet details: `gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'`
2. Export as CSV: `gws drive files export --params '{"fileId": "SHEET_ID", "mimeType": "text/csv"}'`
3. Or read values directly: `gws sheets +read --spreadsheet SHEET_ID --range 'Sheet1' --format csv`

## recipe-compare-sheet-tabs

### Compare Two Google Sheets Tabs

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`

Read data from two tabs in a Google Sheet to compare and identify differences.

#### Steps

1. Read the first tab: `gws sheets +read --spreadsheet SHEET_ID --range "January!A1:D"`
2. Read the second tab: `gws sheets +read --spreadsheet SHEET_ID --range "February!A1:D"`
3. Compare the data and identify changes

## recipe-copy-sheet-for-new-month

### Copy a Google Sheet for a New Month

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`

Duplicate a Google Sheets template tab for a new month of tracking.

#### Steps

1. Get spreadsheet details: `gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'`
2. Copy the template sheet: `gws sheets spreadsheets sheets copyTo --params '{"spreadsheetId": "SHEET_ID", "sheetId": 0}' --json '{"destinationSpreadsheetId": "SHEET_ID"}'`
3. Rename the new tab: `gws sheets spreadsheets batchUpdate --params '{"spreadsheetId": "SHEET_ID"}' --json '{"requests": [{"updateSheetProperties": {"properties": {"sheetId": 123, "title": "February 2025"}, "fields": "title"}}]}'`

## recipe-generate-report-from-sheet

### Generate a Google Docs Report from Sheet Data

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-docs`, `gws-drive`

Read data from a Google Sheet and create a formatted Google Docs report.

#### Steps

1. Read the data: `gws sheets +read --spreadsheet SHEET_ID --range "Sales!A1:D"`
2. Create the report doc: `gws docs documents create --json '{"title": "Sales Report - January 2025"}'`
3. Write the report: `gws docs +write --document-id DOC_ID --text '## Sales Report - January 2025

##### Summary
Total deals: 45
Revenue: $125,000

##### Top Deals
1. Acme Corp - $25,000
2. Widget Inc - $18,000'`
4. Share with stakeholders: `gws drive permissions create --params '{"fileId": "DOC_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "cfo@company.com"}'`

## recipe-sync-contacts-to-sheet

### Export Google Contacts to Sheets

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-people`, `gws-sheets`

Export Google Contacts directory to a Google Sheets spreadsheet.

#### Steps

1. List contacts: `gws people people listDirectoryPeople --params '{"readMask": "names,emailAddresses,phoneNumbers", "sources": ["DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"], "pageSize": 100}' --format json`
2. Create a sheet: `gws sheets +append --spreadsheet SHEET_ID --range 'Contacts' --values '["Name", "Email", "Phone"]'`
3. Append each contact row: `gws sheets +append --spreadsheet SHEET_ID --range 'Contacts' --values '["Jane Doe", "jane@company.com", "+1-555-0100"]'`

## Provenance

Merged from 5 skills of [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`. Licence Apache-2.0 — the source text of every variant is preserved above.
