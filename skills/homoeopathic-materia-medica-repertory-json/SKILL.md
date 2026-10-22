---
name: Homoeopathic Materia Medica & Repertory JSON
description: 13 public-domain homoeopathic classics (1840–1906, ~108k rubrics) extracted into clean, app-ready, verbatim JSON with a self-describing schema, per-book QC and a reproducible pipeline (CC0).
---

# Homoeopathic Materia Medica & Repertory JSON

A curated collection of 13 public-domain homoeopathic Materia Medica and Repertory classics (1840–1906), extracted from scanned page images into structured JSON ready for apps, search tools, study aids and AI. Every rubric/symptom string is kept **verbatim**; unknowns are `null`. Two self-describing shapes (`repertory`, `materia_medica`), a per-book verbatim-fidelity report, and a fully reproducible pipeline. CC0 1.0.

## When to use

- You need open homeopathy data as clean JSON for an app or model.
- You want the canonical schema for repertory/materia-medica content.
- You are adding a new book to the corpus or fixing an OCR token.

## Method

1. Extract with `pipeline/omm_pipeline.py` (`extract-repertory` / `extract-mm` / `validate` / `classify`), using `pipeline/remedy_aliases.csv` and `remedy_master.csv` for name resolution.
2. Follow the schema in `SCHEMA.md`: top-level `type` (`repertory`/`materia_medica`), a `book` object with counts, `sections[].rubrics[]` (or `remedies[].symptoms[]`), ids, `parent`, graded remedies and a `remedy_index`.
3. Enforce the rules: verbatim `text`, `grade` only if printed (else `null`), best-effort canonical names, no invention.
4. Validate every file (zero errors) and record a per-book verbatim-fidelity rate in the QC report.
5. Emit compact JSON; split books that exceed GitHub's per-file limit (Kent by chapter + `index.json`; big files as `…-2.json`) and document how the parts rejoin.
6. Package the pipeline as the `omm-json-builder` skill (`skill/omm-json-builder/`) so it can be driven end-to-end by an agent.
7. Ship a dataset landing page at `docs/index.html`; credit the book authors and the compiler (`CREDITS.md`); invite corrections via `CONTRIBUTING.md`.

## Key files / entry points

- `repertory/*.json`, `repertory/kent-1897/` (34 chapters + `index.json`), `materia_medica/*.json`.
- `pipeline/omm_pipeline.py`, `pipeline/remedy_aliases.csv`, `pipeline/remedy_master.csv`.
- `SCHEMA.md`, `CREDITS.md`, `CONTRIBUTING.md`, `LICENSE` (CC0).
- `skill/omm-json-builder/` — SKILL.md + references + scripts.

## Gotchas

- Never default a grade or invent a name — `null` is the correct value for 'not in the source'.
- OCR damage is real in several books; report it per book rather than smoothing it away.
- Compact JSON (~40% smaller) is what ships; do not pretty-print the dataset files.
- Respect the per-file size limit by splitting, and document the split so consumers can reassemble.
- Require attribution of the book authors and the compiler even though the data is CC0.

## Source projects

- [homoeopathic-materia-medica-repertory-json](https://github.com/drsamonline/homoeopathic-materia-medica-repertory-json) — 13 books, ~108k rubrics, CC0 1.0.

