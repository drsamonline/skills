# Engineering Standards (the engineering gate, shared by every card that writes formulas or touches files)

## 1. Recalculation and preservation (route-specific)

Follow the recalculation, inspection, render, and export contract of the execution skill that owns the workbook. `Spreadsheets` owns standalone artifacts; `excel-live-control` owns a connected live workbook. Do not replace either stack with this package's legacy helper.

The helper below exists only for a legacy standalone OOXML fallback that has already been selected and tested. Run it on a staged output copy, never on the user's original or on a connected live workbook:

```bash
python scripts/recalc.py output.xlsx [timeout_seconds]   # default 60
```

The script recalculates formulas through headless LibreOffice, **rewrites the workbook package in place**, and returns JSON. That rewrite may change cached values, metadata, and XML serialization even when workbook meaning is preserved. Rules:

- Keep the original and any preservation baseline separate. Do not use this rewritten file to prove XML or byte identity.
- Do not ship the legacy-fallback output until `errors_found` is cleared to zero; fix the named cells and run it again.
- An `error` key in the JSON (instead of `status`) means nothing was recalculated at all — debug the environment.
- **Passing recalculation is not the same as correct numbers**: an off-by-one reference comes back just as "clean". So hand-check the values of 2-3 formulas first, then fill the grid.
- If LibreOffice is unavailable, report that this fallback did not recalculate. Do not convert a manual spot-check into a recalc pass.

## 2. Formula compatibility (scope to the selected writer/runtime)

- Use the active writer's documented formula surface and verify formulas through that route. Do not apply an openpyxl-specific prefix or dynamic-array rule to `Spreadsheets` or `excel-live-control`.
- In the legacy openpyxl fallback only, prefer formula families already reproduced by that stack, such as SUMIFS, INDEX/MATCH, IFERROR, SUMPRODUCT, and COUNTIFS. Treat newer or spill formulas as unsupported until the exact writer/recalculator fixture passes.
- Cross-sheet references: a sheet name containing a space must be quoted, `='Assumptions Inputs'!$B$5`.

## 3. Legacy openpyxl fallback traps

This section does not authorize openpyxl when `Spreadsheets` or `excel-live-control` owns the task. Apply it only when the user has selected or supplied that implementation and the current runtime supports it.

| Trap | Rule |
|---|---|
| Reading a model | Load twice: the default load gives formula strings, `data_only=True` gives cached values. One load cannot give both |
| Saving after `data_only=True` | **Destructive**: every formula is replaced by its literal value — never save that handle |
| Merged cells | Write only the top-left anchor cell; the rest are read-only MergedCell objects |
| .xlsm | Only `load_workbook(path, keep_vba=True)` preserves macros; **openpyxl cannot create a vbaProject** (new macro source follows Card 10; any Excel import/run step remains O1-gated) |
| **External links** | When the book holds cross-file references like `='[1]Sheet'!B2`: saving through openpyxl strips the cached values, recalculation fails to resolve them, and you get #NAME? plus every link dead. **Copy those cell values out before saving**; recalc.py refuses to run when it detects this state |
| Number formats | Every numeric cell, formula cells included, needs an explicit `number_format`; same precision down a column |

## 4. Auditable changes (cards that edit existing files: 17 / 18 / 14)

- Keep a copy of the original before touching anything (non-negotiable).
- Write only the input area. Identify it in this order: user instruction > color convention (blue font, distinctive fill) > named ranges > the legend. If you cannot identify it, ask. Do not guess.
- Deliver a change list: which cells changed, old value -> new value, and why.
- Before recalculation, compare a declared semantic preservation set outside the allowed edit range: cell values and formulas, sheet names/order, named ranges, tables, validations, and other objects relevant to that workbook. After recalculation, verify formula results and rendered output separately. Do not assert package-wide XML equality after LibreOffice or another calculation engine rewrites the file.

## 5. Source and assumption notes

Annotate every hardcoded number with its source somewhere visible (adjacent cell or cell comment): `Source: <document name>, <period>, <page/table>, <source URL if any>`. If it came from the user verbally, write "per user input". Finance-domain work follows the comment scheme in finance-pro-playbooks.
