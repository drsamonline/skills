# Data Preparation (Card 1 merge / Card 2 clean / Card 7 compare)

## Card 1: merge multiple files into one master table

**Route contract**
- **Primary channel**: `Spreadsheets` for a standalone merged workbook; authorized Desktop files are inputs, not a CU route.
- **Escalation trigger**: if the result must be written into an already open and connected workbook, switch to `excel-live-control` and use only advertised commands.
- **Hybrid handoff**: inspect and normalize source files without mutating them, then either export one standalone workbook through `Spreadsheets` or write the verified result into the selected live workbook. Do not run both authoring stacks on the same workbook.
- **Fallback**: deliver normalized CSV files plus the column-mapping and skipped-file report when workbook authoring is unavailable.
- **Verification**: source inventory matches; source rows minus confirmed duplicates equal output rows; sampled control totals match; originals are unchanged.
- **CU display / reason**: `no`; no Excel-native retained state is required, and a GUI loop would be slower and less auditable.

**Trigger phrases**: "combine these sheets into one" / "merge these 15 CSVs" / "roll up the monthly sheets from each region"
**Input contract**: a set of files (a directory or a multi-select) plus the key column or the aggregation basis; if missing, ask "which column do we align on, and what happens to duplicates?"
**Steps**:
1. Collect and confirm the inventory (count, formats; more than 20 files, or any legacy .xls, means warn that it runs in batches)
2. Probe each file's structure -> ⚠ present the column mapping table for the user to confirm (header row count, normalizing column-name variants)
3. Normalize the schema -> merge -> dedupe (⚠ the definition of a duplicate must be confirmed)
4. Two checks: row-count conservation (sum of source rows minus duplicates = total rows) plus a spot-check on summed amounts
5. Deliver the master table plus a "Merge Notes" sheet (source -> row-count mapping)
↯ A file is empty or corrupt -> skip it, log it, and keep the batch running; ambiguous column mapping -> stop and ask.
**Output assertions**: the row-count conservation equation holds; sampled amounts match the source sheets.
**Demo data**: 3 fake sales CSVs with mutually inconsistent column names.

## Card 2: clean and standardize a single table

**Route contract**
- **Primary channel**: `Spreadsheets` for diagnosis and a cleaned standalone copy.
- **Escalation trigger**: if the user targets an open, connected workbook, switch to `excel-live-control`; if the target is merely locked but not connected, ask the user to close it or approve a copy.
- **Hybrid handoff**: produce the diagnostic/rule plan first, then apply the approved rules in exactly one selected authoring surface.
- **Fallback**: return the diagnostic report and proposed rules without modifying data when cleanup rules or an execution surface are unresolved.
- **Verification**: the stated change count equals the actual semantic diff, skipped columns are listed, and the original remains unchanged.
- **CU display / reason**: `no`; cleanup does not require app-native state, and CU is not a substitute for a connected workbook route.

**Trigger phrases**: "this sheet is a mess" / "dedupe it" / "the date formats are all over the place"
**Input contract**: the table plus optional rules; with no rules given, produce a Diagnostic Report first and let the user pick what to fix.
**Steps**:
1. Diagnose: duplicates / blanks / mixed types / date corruption (text coerced into dates, scientific notation) / merged cells / hidden rows and columns
2. ⚠ Confirm the rules: what counts as a duplicate? target date format? how are blanks handled?
3. Execute (original untouched, write a new file)
4. Deliver the cleaned version plus a before/after report (rows changed, with examples)
↯ Any column whose rule is unclear -> skip it conservatively and flag it. Never guess.
**Output assertions**: the change count you state equals the actual diff count; the original is unchanged.
**Demo data**: one dirty table carrying all five problem classes (UTF-8 mojibake / text dates / duplicates / blanks / merged cells).

## Card 7: compare two tables for differences

**Route contract**
- **Primary channel**: `Spreadsheets` for a standalone reconciliation workbook and difference list.
- **Escalation trigger**: if one or both targets are active connected workbooks and the live schema can read the required ranges, switch to `excel-live-control` for those reads and any requested in-workbook annotations.
- **Hybrid handoff**: read the verified ranges, perform the keyed comparison, then write results either to a new standalone workbook or the selected live workbook, never an unverified third file.
- **Fallback**: return a key-quality report and candidate-key list when a stable key cannot be confirmed.
- **Verification**: A-only plus shared equals A total, B-only plus shared equals B total, duplicate-key handling matches the approved rule, and sampled differences trace to source rows.
- **CU display / reason**: `no`; reconciliation is a deterministic data task and does not need Excel GUI state.

**Trigger phrases**: "reconcile these" / "what's different between these two versions" / "who registered but didn't show up"
**Input contract**: two tables plus the key column; if missing, propose candidate keys and ask the user to confirm.
**Steps**:
1. ⚠ Confirm the key (what counts as the same record; if the key column has duplicates, report that first, then choose a strategy: aggregate then compare, or compare row by row)
2. Three difference classes: A only / B only / same key but different values
3. Deliver a highlighted version plus a difference list plus the counts
**Output assertion**: set conservation — A only plus shared equals A's total, B only plus shared equals B's total.
**Demo data**: two versions of a name list containing case differences, trailing spaces, and duplicate keys.
