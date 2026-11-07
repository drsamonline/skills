---
name: excel-workbooks
description: "Route any spreadsheet job by the workbook state that must survive: create, clean, extract, analyse, build a dashboard, audit, repair, or automate — in Excel, WPS, LibreOffice Calc or Numbers. Use when the user asks what can be done with a spreadsheet, hands over a workbook, or needs formulas, a pivot, a template or a repair."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Excel and spreadsheet playbooks"
  category: "office-docs"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "excel-playbooks"
---

# Excel and spreadsheet playbooks

A routing skill rather than a single technique: the first decision is which engine owns the workbook, because that decides what is safe to touch. A standalone file can be rebuilt; a workbook open in someone's Excel session must be edited through live control and never re-saved underneath them.

## When to use

- A spreadsheet must be created, cleaned, merged, analysed or repaired.
- A workbook that is currently open must be edited without disturbing the user's session.
- A finance or reporting method is needed on top of a spreadsheet.
- Spreadsheet work must be automated or made repeatable.

## Method

1. Run the routing step first, in order, first match wins: is the workbook a standalone file or a live session? Is the output a new file or an in-place change? Is a finance method needed? Does it need an app-side integration?
2. If the user says 'don't touch my original', read the input only and write a new output file.
3. Never load the standalone authoring stack while the live-control route is active — two writers on one workbook is how work gets lost.
4. Every deliverable containing formulas must pass the route's recalculation and inspection contract before delivery: recalculate, read back the computed values, and confirm nothing evaluates to an error.
5. Never hardcode a result into a formula; annotate every assumption and every hardcoded number with its source, in place.
6. When editing an existing file, match its conventions, change only the declared area, and deliver a change list.
7. Verify the semantic preservation set before recalculating, and never claim package-level integrity you did not check.
8. State the engine used and the cell range touched in the delivery note.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`excel-playbooks`](references/excel-playbooks/) | The routing map and the card library: creation, cleanup, extraction, analysis, dashboards, audits, repair, automation, plus the output gate. |

## Key files / entry points

- `references/excel-playbooks/` — the routing map, the numbered cards (creation, cleanup, extraction, analysis, dashboards, audits, repair, automation) and the output gate.

## Gotchas

- Live control exists to protect an open session — using the standalone stack instead overwrites the user's unsaved work.
- A formula that returns a value because it was pasted as a value is not a formula.
- Hardcoded numbers without a stated source make the workbook unauditable.
- Recalculation is not verification; read the computed values back.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `excel-playbooks` — no licence file shipped with the source
