# Deliverables (Card 4 report / Card 5 dashboard / Card 6 model / Card 8 workbook)

Shared: standalone workbooks route to `Spreadsheets`; open connected workbooks route to `excel-live-control`. This file defines Excel-specific outcome and verification contracts, not a competing authoring stack. General-domain visuals may use formats/visual_standards.md only when they do not conflict with the selected execution skill, a supplied template, or an existing workbook. Formula verification follows engineering section 1.

## Card 4: data -> analysis report xlsx

**Route contract**
- **Primary channel**: `Spreadsheets` for a standalone analytical workbook.
- **Escalation trigger**: if the report must be built inside an already connected workbook, switch to `excel-live-control`; if the analysis itself is finance/investment work, defer to `finance-pro-playbooks`.
- **Hybrid handoff**: compute the agreed metrics from source data, then write the traceable result once through the selected workbook surface.
- **Fallback**: deliver the analysis table and metric definitions without a workbook when the data cannot support the requested conclusions or authoring is blocked.
- **Verification**: every summary number traces to detail/source data, control totals reconcile, chart ranges bind to the intended cells, and rendered sheets are legible.
- **CU display / reason**: `no`; the deliverable is a verified artifact and does not require Excel GUI state.

**Trigger phrases**: "analyze this and get my boss a report" / "do a first-half comparison"
**Steps**: (1) ⚠ confirm the basis (metric definitions, periods) (2) analyze (aggregates / trends / outliers) (3) assemble the sheets: Overview (readable on its own) -> detail -> charts; (4) give every summary number a source column so the numbers stay traceable; (5) a KEY INSIGHTS block (visual_standards Layer 2).
↯ The data cannot answer the question -> say plainly what is missing. Do not force an answer.
**Delivery variant**: you can add an image-format summary page (easy to paste into a deck or a chat).
**Output assertions**: every summary number traces back to the detail area; chart data ranges are bound correctly.
**Demo data**: a public sales dataset plus the expected conclusions for 3 preset questions.

## Card 5: interactive dashboard

**Route contract**
- **Primary channel**: `Spreadsheets` for a standalone formula/table/chart dashboard; use only features supported by its current schema.
- **Escalation trigger**: use `excel-live-control` when a selected connected workbook advertises the required table, chart, or PivotTable command. A Desktop CU tail is eligible only when the user requires a specific Excel-native object unavailable through live tools and that exact operation has current O1 evidence.
- **Hybrid handoff**: prepare and verify the source/summary ranges first, then create native objects through one advertised live command surface or one O1-scoped CU subflow.
- **Fallback**: deliver a pivot-ready data model and a non-native interactive dashboard or version-aware guidance; do not promise a slicer without retained-state proof.
- **Verification**: selectors change the intended summaries and charts; native objects, when created, appear in the live object inventory and survive save/reopen; layout passes visual inspection.
- **CU display / reason**: `no` by default; the CU tail is optional and remains undisplayable until an O1 event proves the exact object, build, recovery path, and reopen postcondition.

**Trigger phrases**: "build me a dashboard" / "a sales cockpit"
**Legacy fallback boundary**: when an explicitly selected openpyxl fallback cannot create the required native object, use a **pseudo-slicer approach**:
- Data-validation dropdowns (dimension-selector cells) + a summary block driven by `SUMIFS` / `INDEX+MATCH` (all 2007-era functions, FILTER banned) + charts bound to that summary block -> change the dropdown, the charts follow.
**Steps**: (1) ⚠ confirm the dimensions and the metrics they care about (ask for a reference style image if useful, and match its taste) (2) convert to Tables (3) summary block plus charts (4) wire the dropdowns (5) theme colors (the visual_standards theme system) (6) refresh instructions.
If the user requires native PivotTables or slicers, first use an advertised connected-session command. Otherwise deliver a pivot-ready structure or guidance. Use CU only after the exact operation passes the O1 gate in desktop_runtime.md.
↯ More than 100,000 rows -> warn about performance and suggest splitting.
**Output assertion**: change a dropdown value -> recalc -> the summary block and chart data follow and are correct.
**Demo data**: a public sales dataset (region x product x month).

## Card 6: ordinary business model (outside the finance domain)

**Route contract**
- **Primary channel**: `Spreadsheets` for ordinary business math such as a simple budget, forecast, pricing, capacity, or unit-economics model.
- **Escalation trigger**: DCF, LBO, comps, three-statement, investment, valuation, diligence, finance-model audit, or finance-model editing immediately defers to `finance-pro-playbooks`; an active connected non-finance workbook defers to `excel-live-control`.
- **Hybrid handoff**: finance methodology and standards come entirely from `finance-pro-playbooks`; this package may only route the resulting workbook to the selected standalone or live surface.
- **Fallback**: provide a confirmed assumptions table and calculation specification without building when rules or domain ownership are unresolved.
- **Verification**: each output traces through formulas to declared assumptions, edge cases pass, and no calculation embeds an undeclared hardcoded result.
- **CU display / reason**: `no`; ordinary models are formula artifacts, while finance-domain models are owned by the finance skill.

**Domain gate**: professional finance deliverables such as DCF, LBO, comps, or three-statement models -> **switch to finance-pro-playbooks immediately**; this card covers ordinary business math only (unit economics, simple budgets and forecasts).
**Steps**: (1) ⚠ collect and confirm the assumptions (value, basis, direction of impact) (2) the formula chain (never hardcode a result) (3) a sensitivity table (optional) (4) an assumptions page.
↯ A requirement that implies a circular reference -> use iterative calculation or solve it algebraically, and say which.
**Output assertions**: change any assumption and the outputs follow; the formula chain has no #REF!; a full-sheet scan finds no hardcoded numbers embedded in formulas.

## Card 8: formula-driven business workbook

**Route contract**
- **Primary channel**: `Spreadsheets` for a standalone formula-driven workbook.
- **Escalation trigger**: switch to `excel-live-control` only when the user targets a registered open workbook and the required ranges/objects are advertised; finance-domain logic defers to `finance-pro-playbooks`.
- **Hybrid handoff**: confirm rules and test cases first, then build once through the selected workbook surface; do not create a standalone copy and silently overwrite the live target.
- **Fallback**: deliver the rule table, input schema, and expected-output cases when conflicting rules prevent implementation.
- **Verification**: every rule case passes, validation constraints reject planted bad input, protected ranges are confirmed through the selected surface, and rendered instructions are readable.
- **CU display / reason**: `no`; workbook formulas and validation state should use the standalone or connected-document route rather than GUI cell editing.

**Trigger phrases**: "build me a ledger that calculates itself" / "a sheet where I type it in and the answer comes out"
**Steps**: (1) ⚠ interview them on the business rules (what goes in, what gets calculated, who maintains it) (2) structure plus the formula chain (3) data-validation dropdowns / conditional formatting / protected ranges (4) an instructions sheet plus a legend plus one row of sample data (per the visual_standards spec).
↯ Rules that conflict -> lay them out in a table and ask the user to decide.
**Output assertions**: the rule test-case table (input -> expected output, 10 cases) passes in full; protection on the locked ranges is in effect.
**Compatibility note**: when the recipient's default app is not Excel (R2), write the data-validation and conditional-formatting differences into the instructions page.
