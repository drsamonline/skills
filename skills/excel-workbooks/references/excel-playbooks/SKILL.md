---
name: excel-playbooks
description: "Use when the user asks what Manus can do with Microsoft Excel, WPS Spreadsheets, LibreOffice Calc, or Numbers, or needs a spreadsheet workflow routed by the workbook state that must survive. Covers creation, cleanup, extraction, analysis, dashboards, audits, repair, and automation; routes standalone files to Spreadsheets, open Excel workbooks to excel-live-control, finance methods to finance-pro-playbooks, and app-specific state only after capability and runtime checks."
---

# Excel Playbooks (Manus for Excel)

Route spreadsheet requests such as "merge these 15 CSVs" or "update this open workbook" to the mechanism that preserves the required state. This skill owns Excel-specific scene selection and routing. It does not replace the execution contracts of `Spreadsheets`, `excel-live-control`, or `finance-pro-playbooks`.

## Step 0: Unified Routing (run every task through this, in order, first match wins)

```
R0 Domain and target-state ownership
   Finance, valuation, investment banking, or professional finance-model work -> finance-pro-playbooks
   A standalone file or a request to create a new workbook artifact              -> Spreadsheets
   An open/active workbook, tagged Excel app, selected range, or established
      connected Excel follow-up                                                  -> excel-live-control
   Do not load the standalone authoring stack while the live-control route is active.
R1 Explicit surface preference
   "don't touch my original / give me a new file" -> Spreadsheets, input read-only, new output
   "do it online / in the web version"            -> My Browser only if it is exposed in the
      current session and the signed-in plan/source supports the required state
   "show me in Excel / use Computer Use"           -> respect the preference, but execute an
      app-native path only when that exact operation has current O1 evidence for the detected
      OS, Excel edition, version, and retained state; otherwise explain the limitation and use
      connected live control, version-aware guidance, or a standalone artifact as agreed
R2 File reachability and locks
   File is not in the shared folder -> walk the user through moving it in (see
      formats/desktop_runtime.md section 2), or have them upload it
   File is open (locked)            -> use excel-live-control when the workbook is registered and
      the required command is advertised; otherwise ask the user to close it or work on a copy
R3 When the requested output must open in the user's preferred spreadsheet app, or the task needs
   an app runtime, detect the default app (see formats/desktop_runtime.md section 1) -> choose the
   execution matrix
   Excel -> Excel branches may be considered | Numbers -> deliver xlsx, reroute the macro/PQ cards | WPS -> xlsx
      compatible, note macro-engine differences
   LibreOffice -> xlsx/ODS, reroute PQ | no spreadsheet app -> standalone artifact delivery
   The detected default is a delivery and compatibility signal, not proof that its GUI is required
      or that any app-native procedure is authorized.
R4 App-native escalation: the five narrow areas in desktop_runtime.md identify where Excel state may
   matter; they do not authorize Computer Use. Prefer advertised live-control tools. Use CU only
   when the exact operation passes the O1 gate; otherwise use guidance or a safe artifact fallback.
R5 Delivery: follow the selected execution skill's output contract. For file routes, preserve the
   original and use an explicit output path; if the default app is not Excel, add a compatibility note.
```

**Neighbor boundaries**:

- `Spreadsheets` owns standalone spreadsheet creation, editing, analysis, rendering, recalculation, and export. When selected, follow its current tool stack and verification rules rather than this package's legacy implementation examples.
- `excel-live-control` owns an open or connected Microsoft Excel workbook. It uses Computer Use only for setup, target confirmation, and focus; workbook reads and writes use the commands advertised by that live session. Do not claim an unadvertised command.
- `finance-pro-playbooks` owns finance and valuation methodology and its Excel formatting standard for DCF, LBO, comps, three-statement models, diligence trackers, and finance-model audits or edits.
- `word-playbooks` owns WPS Writer and LibreOffice Writer requests; `powerpoint-playbooks` owns WPS Presentation and LibreOffice Impress requests. WPS Office and LibreOffice are decomposed by component rather than receiving a duplicate generic suite package.

## Step 1: ROUTING MAP (intent -> card -> which file to read)

| The user wants... | Card | Read reference | Also read formats | Channel |
|---|---|---|---|---|
| Combine this pile of files into one master table | 1 Merge | `references/data-preparation.md` | engineering | Spreadsheets; live control only for an active target |
| This sheet is a mess / dedupe / fix the formatting | 2 Clean | `references/data-preparation.md` | engineering | Spreadsheets; live control only for an active target |
| Compare two tables for differences / reconcile | 7 Compare | `references/data-preparation.md` | engineering | Spreadsheets; live control only for an active target |
| Turn an image / PDF / scan into a table | 3 Transcribe | `references/extraction.md` | engineering | Extraction + Spreadsheets |
| Extract a table out of contracts / documents / surveys | 19 Text extraction | `references/extraction.md` | engineering | Extraction + Spreadsheets |
| An analysis report out of this data | 4 Report | `references/deliverables.md` | engineering+visual | Spreadsheets; live control only for an active target |
| Build an interactive dashboard | 5 Dashboard | `references/deliverables.md` | engineering+visual | Spreadsheets or advertised live tools; O1-gated CU tail |
| Build an ordinary business model outside the finance domain | 6 Model | `references/deliverables.md` | engineering+visual | Spreadsheets |
| A ledger / entry sheet that calculates on its own | 8 Workbook | `references/deliverables.md` | engineering+visual | Spreadsheets |
| Give me a template (budget, invoice, ...) | 11 (sub-branch of 18) | `references/update-existing.md` | visual | Spreadsheets |
| Update a non-finance workbook with new data / fill a template | **18 Fill and update** | `references/update-existing.md` | engineering | Spreadsheets or excel-live-control by target state |
| Check non-finance workbook health / formulas | 17 Audit | `references/update-existing.md` | engineering | Spreadsheets or excel-live-control by target state |
| The file won't open / it's corrupted | 14 Repair | `references/update-existing.md` | engineering | Standalone file repair; app reopen is O1-gated |
| I deleted it by mistake, get it back | 15 Rebuild | `references/update-existing.md` | — | Extraction + Spreadsheets |
| Freeze the monthly repeat work into a pipeline | **9 PQ pipeline** | `references/automation.md` | desktop_runtime | Spreadsheets, My Browser, or O1-gated Excel state by retained state |
| Write / fix a VBA macro | 10 Macro | `references/automation.md` | engineering+desktop_runtime | Source drafting; app import/run is O1-gated |
| Produce this report automatically on a schedule | 16 Recurring | `references/automation.md` | desktop_runtime | Spreadsheets + an exposed scheduler with reachable sources |
| How do I do this (teach me) | **12 how-to** | `references/desktop-interactive.md` | desktop_runtime | Guidance, live control, or O1-gated CU by requested outcome |
| Refresh the data connection / PQ is erroring | 13 Refresh | `references/desktop-interactive.md` | desktop_runtime | My Browser, advertised live tools, or O1-gated CU by source/state |

**Channel vocabulary**: *Spreadsheets* = the installed standalone-workbook artifact skill. *excel-live-control* = commands advertised by a selected connected Excel session. *Computer Use* = semantic operation of the real desktop app, allowed here only for an exact O1-verified app-native tail. *My Browser* = the user's own logged-in browser, not Computer Use. *Guidance* = version-aware instructions when execution is unproved or user-operated.

**CU display markers**: a marker is eligible only after an O1 event for the exact operation, OS, Excel edition/version, fixture, retained state, and postcondition. Card 12 may become `highlight`; Card 9 may become `conditional-highlight`; Cards 10 and 13 may become `yes`. Until those events exist, each remains conditional and the package must route to live tools, guidance, My Browser, or a standalone artifact instead of promising CU execution.

## Step 2: Output gate (applies to every card)

1. **Any deliverable containing formulas must pass the selected route's recalculation and inspection contract.** Follow `Spreadsheets` or `excel-live-control` when either owns execution. Use `python scripts/recalc.py out.xlsx` only for the documented legacy standalone-file fallback; it rewrites the workbook package and is not a preservation oracle (details in formats/engineering_standards.md section 1).
2. **Incremental verification**: write 2-3 formulas and confirm the values are right before filling the whole grid.
3. **Never hardcode a result into a formula**; annotate every assumption and every hardcoded number with its source, in place.
4. **Editing an existing file**: match its conventions, change only the declared area, and deliver a change list. Verify a semantic preservation set before recalculation; never claim package-wide XML identity after a rewriting calculation engine runs.
5. General-domain visuals follow formats/visual_standards.md; number formats follow its Layer 2 section (every numeric cell needs an explicit `number_format`).
