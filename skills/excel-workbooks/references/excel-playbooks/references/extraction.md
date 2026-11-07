# Extraction (Card 3 image/PDF transcription / Card 19 text field extraction)

## Card 3: image / PDF / scan -> Excel

**Route contract**
- **Primary channel**: Manus image/document extraction for field capture, then `Spreadsheets` for the standalone workbook.
- **Escalation trigger**: if the extracted rows must enter an already connected workbook, switch only the write stage to `excel-live-control` after confirming the target sheet/range.
- **Hybrid handoff**: keep extraction provenance and confidence flags in a structured intermediate, then write that exact data through the selected workbook surface.
- **Fallback**: deliver CSV plus a low-confidence and failed-page list when workbook authoring or reliable extraction is unavailable.
- **Verification**: input/output item counts match, each row retains source identity, sampled key fields match the answer source, and every ambiguity is flagged rather than inferred.
- **CU display / reason**: `no`; visual extraction and workbook construction do not require Excel-native GUI state.

**Trigger phrases**: "type these receipts into a sheet" / "turn the table in this image into Excel" / "digitize these scans"
**Input contract**: the set of images or PDFs plus the target column structure; if missing, propose a default schema and ask for confirmation.
**Steps**:
1. Visually extract tables and fields, one item at a time
2. Map values onto the schema columns; ⚠ any ambiguous character -> mark it low-confidence (use the warning color from visual_standards for the highlight)
3. Keep filenames in strict one-to-one correspondence across the batch (follow the user's naming requirement exactly when they have one)
4. Sampling check: pull 1 item in every 10 and compare every field by hand
5. Deliver the xlsx plus the low-confidence list
↯ A page that is entirely unreadable -> put it on a single "failed" list. Do not invent content.
**Output assertions**: file count matches one-to-one; the key amount columns match the sampled baseline 100% (any mismatch must already be flagged low-confidence).
**Demo data**: fake receipts at three quality tiers - sharp, blurry, skewed.

## Card 19: extract fields from documents / text into a table

**Route contract**
- **Primary channel**: Manus document/text extraction followed by `Spreadsheets` for a standalone table.
- **Escalation trigger**: use `excel-live-control` only when the user explicitly targets a registered open workbook; finance filings and earnings workflows defer to `finance-pro-playbooks` before extraction begins.
- **Hybrid handoff**: preserve field-level source excerpts and confidence in a structured intermediate, then write those values through the chosen workbook surface.
- **Fallback**: return the schema, extracted CSV, provenance, and unresolved-field list when a workbook cannot be produced.
- **Verification**: every non-empty value has source provenance, missing fields remain missing, and a sampled set matches the answer key at field level.
- **CU display / reason**: `no`; the retained value is a traceable table, not Excel app state.

**Trigger phrases**: "pull the key terms out of these contracts into a table" / "summarize these survey responses" / "make me a list from this pile of resumes"
**Scope note**: extraction from financial statements or quarterly filings -> defer to finance-pro-playbooks (Earnings Update); this card covers non-finance documents.
**Input contract**: the document set plus the field schema; if missing, propose a default field list for that document type and ask for confirmation.
**Steps**:
1. ⚠ Confirm the schema (field names, types, what to write when a value is missing)
2. Extract document by document; **attach a provenance for every value** (page number, clause number, a column with the verbatim source sentence)
3. Summary table plus low-confidence flags
↯ A field missing from a given document -> leave it blank with "not found". Do not infer it.
**Output assertions**: field-level accuracy on the sampled documents meets the bar (compared against a hand-built baseline); every non-empty value has a provenance.
**Demo data**: 3 fake contracts with different structures.
