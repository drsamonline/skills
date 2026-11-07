---
name: omm-json-builder
description: "Convert raw homeopathic source texts — OCR text, DjVu XML, or a typed transcription — into clean, app-ready JSON, one file per book, for a materia medica / repertory reader. Use to add a book to the OMM collection, rebuild a volume whose headings OCR destroyed, validate or repair an extraction, or work with the homeopathy JSON schema. It structures text that already exists; it never generates homeopathic content."
license: "per source — see references/*/LICENSE"
metadata:
  title: "OMM JSON builder (materia medica and repertory extraction)"
  category: "data-and-schema"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "omm-json-builder"
---

# OMM JSON builder (materia medica and repertory extraction)

One rule governs everything: **no fabricated data**. Every rubric and symptom string must trace back into the source file, and missing values are `null` rather than guessed. An earlier version of this project produced template JSON that looked structured and contained none of the book — that is the failure mode this skill exists to prevent.

## When to use

- A materia medica or repertory must become structured JSON.
- A new volume is being added to the OMM collection.
- An existing extraction must be validated, repaired, or rebuilt after bad OCR.

## Method

1. Check the collection first: search `catalog.json` for title and author before parsing anything. Duplicate volumes have been built because this was skipped.
2. Screen rights before parsing: read the title page, not the item metadata. An old text behind a modern reprint is still in copyright.
3. Choose the medium: OCR text, DjVu XML, or a typed transcription — each has its own extraction path and its own failure modes.
4. Classify the book (repertory: chapter → rubric → remedies; materia medica: remedy → symptoms) before extracting, because the schema differs.
5. Extract, then normalise remedy names against the existing collection's naming, then validate — validation must report zero errors before anything is promoted.
6. Ship the smallest faithful form the tool offers, and never hand-edit JSON to raise a score.
7. Count from the files, never by hand: walk the JSON and sum the sections, rubrics and graded links.
8. Record identity, source and extraction date with the book so a later run can tell whether it is already present.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`omm-json-builder`](references/omm-json-builder/) | The extraction pipeline: rights screen, medium selection, classification, extract/normalise/validate/promote, honest metrics. |

## Key files / entry points

- `references/omm-json-builder/` — the pipeline, the JSON schema, extraction and validation commands, remedy-name normalisation, the quality bar.
- `references/omm-json-builder/references/` — DjVu XML handling, the OCR playbook, and the workflow notes.

## Gotchas

- Never regenerate from a template — parse a real file.
- Volumes have been identified by height instead of spelling; verify identity from the title page.
- Hand-edited counts are wrong counts.
- Missing data is `null`, not a plausible guess.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `omm-json-builder` — no licence file shipped with the source
