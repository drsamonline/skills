# Update Existing (Card 18 fill and update / Card 17 audit / Card 14 repair / Card 15 rebuild; Card 11 template generation is a sub-branch of 18)

Non-negotiable across this group: keep a copy of the original before touching anything. For Card 18, write only the approved input area and deliver a change list; the audit, repair, and rebuild cards follow their own declared mutation scope.

## Card 18: fill and update a template or model (the main card of this group)

**Trigger phrases**: "update this model with the new data" / "put the Q3 numbers in" / "produce one following this template"
**Domain gate**: updating or auditing a finance model -> defer to finance-pro-playbooks (Model Audit / Live Model Editing); this card covers non-finance workbooks.
**Route contract**:
- **Primary channel**: `Spreadsheets` for a standalone non-finance workbook; `excel-live-control` for a selected connected workbook, using only advertised commands.
- **Escalation trigger**: external links, add-ins, locks, or retained native state may require an app route. Use Desktop CU only when the exact operation, build, fixture, recovery path, and postcondition have current O1 evidence.
- **Hybrid handoff**: inspect and map inputs read-only, then perform all writes through exactly one authoring surface. Never alternate between standalone and live writers on the same output.
- **Fallback**: write a new standalone copy, provide a change plan, or ask the user to resolve the app-bound dependency. Do not claim that an unresolved external link or add-in was refreshed.
- **Verification**: compare the semantic preservation set before recalculation, verify every intended input change, then inspect recalculated values and a rendered or reopened output through the selected route.
- **CU display / reason**: `no` by default; an O1-gated CU tail is justified only by retained Excel-native state that the standalone and connected-document routes cannot preserve or operate.
**Steps**:
1. Identify the input area: user instruction > color convention > named ranges > the legend; if you cannot tell, ask
2. ⚠ Map the new data and align the basis (units, periods)
3. Write input cells only; do not touch a single formula cell
4. Run the selected route's recalculation and verification contract -> deliver, plus the change list (cell address, old value -> new value)
Variant a: **there is no existing template** (formerly Card 11) -> generate a formula-bearing template per visual_standards (budget, invoice, schedule, Gantt), ask which fields to customize, and demonstrate with a sample row.
Variant b: **bolt on a scenario panel or sensitivity table** -> add a lever block onto the existing model without touching its formulas.
↯ The book contains external links -> follow the external-link trap procedure in engineering section 3; if the link must stay live, use an advertised live command or an exact O1-gated app route, otherwise stop and explain the limitation.
**Output assertions**: intended inputs changed; formulas, names, validations, styles, merges, drawings, and VBA payload outside the approved scope remain semantically preserved; output values and render pass the selected route's verification contract.
**Demo data**: a golden template plus a new quarter's dataset.

### Card 11 route contract: generate a reusable template

- **Primary channel**: `Spreadsheets` for a new formula-bearing standalone template.
- **Escalation trigger**: an active connected workbook routes to `excel-live-control` only when the required write and formatting commands are advertised.
- **Hybrid handoff**: collect fields, rules, and sample rows first, then create and verify the template through one authoring surface.
- **Fallback**: deliver a simpler table/formula template when the selected route cannot reproduce a requested native control.
- **Verification**: test formulas, validations, editable-input conventions, one sample row, and rendered usability.
- **CU display / reason**: `no`; reusable templates are artifacts and do not inherently require Excel GUI state.

## Card 17: workbook audit

**Trigger phrases**: "check whether there's anything wrong with this sheet" / "I inherited an old model, give it a checkup"
**Route contract**:
- **Primary channel**: `Spreadsheets` for a read-only standalone audit; `excel-live-control` for a connected workbook when its advertised reads expose the required formulas and values.
- **Escalation trigger**: a finance-model audit defers to `finance-pro-playbooks`; unexposed add-in or external-link state is reported as an audit limitation rather than inferred.
- **Hybrid handoff**: collect evidence without mutation, then deliver a separate findings report; apply fixes only as a separately approved task through one authoring surface.
- **Fallback**: provide a partial audit with an explicit coverage map and unresolved checks.
- **Verification**: every finding cites a sheet/range or workbook object, severity, detection rule, and reproducible check; supplied tie-outs are tested individually.
- **CU display / reason**: `no`; audit evidence should come from workbook structure or connected-document reads, not GUI observation.
**Steps**: unpack and scan -> report graded by severity (critical / warning / note):
- Formula errors (#REF! / #NAME? / circular references) - named hardcoded numbers embedded inside formulas - external-link risk list - leftover spill functions - inconsistent precision within a column - ⚠ verify each tie-out identity the user gives you, one by one (for example, assets = liabilities + equity)
**Output assertion**: all five classes of planted defects are detected.
**Demo data**: a set of defective workbooks, one for each of the five defects.

## Card 14: repair a corrupted file

**Trigger phrases**: "the file won't open any more" / "it says corrupt"
**Route contract**:
- **Primary channel**: file-level diagnosis and a repaired copy through the standalone artifact route; never modify the only original.
- **Escalation trigger**: opening the repaired copy in Excel is allowed through CU only when that exact open/recovery flow has current O1 evidence; otherwise ask the user to open it or provide guidance.
- **Hybrid handoff**: preserve the source, diagnose the evidenced defect, repair a copy, then verify the readable data and workbook structure before any optional app-open check.
- **Fallback**: extract recoverable tables into a new workbook and label lost or uncertain structures.
- **Verification**: the copy passes package checks, opens through an available verified reader, and preserves at least the readable source rows; any app-native verification is separately O1-gated.
- **CU display / reason**: `no` by default; an O1-gated open check verifies Excel compatibility but is not the repair mechanism.
**Steps**: (1) back up the original (2) unpack and diagnose the package parts (3) repair only the defect supported by the diagnosis (4) repack as a copy (5) verify through an available reader; use Excel itself only under the route contract above.
↯ Unrepairable -> extract as much data as possible into a new file (a degraded deliverable — say so honestly).
**Output assertions**: the repaired file opens; its data row count is greater than or equal to the readable area of the original.

## Card 15: rebuild after a destructive mistake

**Trigger phrases**: "I wrecked my sheet / deleted a few thousand rows by accident"
**Route contract**:
- **Primary channel**: extraction from surviving sources followed by `Spreadsheets` for a new standalone reconstruction.
- **Escalation trigger**: if the user selects a connected recovery target, use `excel-live-control` only for advertised writes after the reconstructed dataset is verified.
- **Hybrid handoff**: inventory sources read-only, reconcile them into a confidence-scored dataset, then create the replacement workbook through one authoring surface.
- **Fallback**: deliver the recoverable subset with missing blocks and confidence explicitly marked.
- **Verification**: reconcile rebuilt rows and key totals to every surviving source, report conflicts, and never infer missing values.
- **CU display / reason**: `no`; recovery is a source-reconciliation and artifact task, not an Excel GUI task.
**Steps**: (1) inventory what survives (older versions with the same name, the mail attachment directory, the trash, PDF reports, screenshots) (2) cross-rebuild from multiple sources (reuse the visual capability from Card 3) (3) confidence flags (4) advice on preventing a repeat (versioning habits).
↯ Not enough surviving sources -> report honestly what fraction is recoverable. Do not invent the rest.
**Output assertions**: the rebuilt area matches the surviving-source baseline; missing blocks are explicitly flagged.
