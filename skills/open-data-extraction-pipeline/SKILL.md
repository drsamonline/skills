---
name: Open data-extraction pipeline and JSON schema
description: Turn raw OCR'd source texts into clean, app-ready JSON with a verbatim-fidelity rule: nothing invented, unknowns null, per-book QC, a self-describing schema and a reproducible pipeline.
---

# Open data-extraction pipeline and JSON schema

The `homoeopathic-materia-medica-repertory-json` dataset and the `omm-json-builder` skill define how drsamonline publishes open data: parse raw OCR text with a grammar-aware pipeline, keep every rubric/symptom string **verbatim**, never guess (unknowns are `null`), and report a per-book verbatim-fidelity rate. Two self-describing JSON shapes (`repertory`, `materia_medica`) are used, and the pipeline is fully reproducible from the committed source text.

## When to use

- You are extracting structured data from scanned/OCR'd books for use in apps or AI.
- You need a schema that apps can consume without bespoke parsing.
- Fidelity and provenance matter more than filling every field.

## Method

1. Classify each source text as `repertory` (rubric → remedies) or `materia_medica` (remedy → symptoms), either by a `classify` heuristic or explicitly.
2. Clean OCR lightly and only in agreed ways: fix ligatures (ﬁ→fi, ﬀ→ff…), normalise quotes, rejoin words hyphen-broken across a line break (only when the next line starts lower-case), collapse runs of spaces, and drop running heads / standalone page numbers. Preserve wording otherwise. Do **not** flatten em/en dashes in chaptered materia medicas — they are the symptom separator.
3. Parse with the right grammar per book into the target shape. Emit ids (`<slug>-sN` sections, `<slug>-rNNNNN` rubrics), and keep `parent` for sub-rubrics (`null` at top level).
4. Apply the schema rules: `text` is verbatim; `grade` is an integer 1–3 **only if the source prints one**, else `null`; canonical remedy names are resolved best-effort or `null`; keep a `remedy_index` mapping every printed token → `{ name, resolved }`.
5. Validate every file against the schema (zero errors) and compute a verbatim-fidelity rate: the share of strings found character-for-character in the source. Report it per book in the QC output.
6. Emit **compact JSON** (no indentation) — ~40% smaller than pretty-printed and parses identically, which matters for shipping inside an app.
7. Split large books that exceed GitHub's per-file limit into parts (e.g. Kent by chapter + `index.json`; big files as `…-2.json`) and document how to concatenate.
8. Make it reproducible: commit the pipeline (`pipeline/omm_pipeline.py`), the source text and the remedy alias/master CSVs, and document the exact command. Wrap it as a reusable skill (`skill/omm-json-builder/`) so the same pipeline can be driven end-to-end.
9. State the data-quality caveats honestly in the README (OCR fragments, damaged abbreviations, books that did not parse) and require attribution of both the book authors and the compiler.

## Key files / entry points

- `pipeline/omm_pipeline.py` — `extract-repertory` / `extract-mm` / `validate` / `classify` subcommands.
- `pipeline/remedy_aliases.csv`, `pipeline/remedy_master.csv` — name normalisation vocabularies.
- `SCHEMA.md` — field-by-field data model and rules.
- `repertory/*.json`, `materia_medica/*.json` — the shipped datasets (`type` = `repertory` / `materia_medica`).
- `skill/omm-json-builder/` — the packaged extraction skill (SKILL.md + references + scripts).
- `MATERIA-MEDICA-BUILDER` — the app-side counterpart that lets a practitioner build/edit their own materia medica and export it to JSON/CSV/XLSX/PDF/HTML/SQL/SQLite.

## Gotchas

- Never fill an unknown with a guess. `grade: null` means 'the source did not print a grade' — a defaulted grade is a factual error.
- Verbatim means verbatim: do not paraphrase, expand abbreviations, or 'fix' the author's wording. Corrections belong in a separate field or a PR.
- OCR damage is real (Vilas, Lippe, Clarke, Pulford, Bryant; Bell's names are OCR-mangled). Report it per book; do not silently smooth it.
- Compact JSON saves ~40% and is what the apps expect — do not pretty-print the shipped files.
- GitHub rejects files over its upload limit; split them and say how the parts rejoin.
- Historical medical texts are study material, not advice — carry the disclaimer and the attribution requirement.

## Source projects

- [homoeopathic-materia-medica-repertory-json](https://github.com/drsamonline/homoeopathic-materia-medica-repertory-json) — 13 books, ~108k rubrics, CC0, with `pipeline/omm_pipeline.py`, `SCHEMA.md` and the `omm-json-builder` skill.
- [MATERIA-MEDICA-BUILDER](https://github.com/drsamonline/MATERIA-MEDICA-BUILDER) — the offline PWA that authors and exports materia medica/repertory content in eight formats.

