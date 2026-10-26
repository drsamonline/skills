---
name: repertory-kit-repertorisation
description: Grade-weighted homeopathic repertorisation in one zero-dependency file: rubric grading 1/2/3, remedy scoring, must-have and exclude filters, ranked results.
metadata:
  title: "Repertorisation with grade-weighted scoring"
---

# Repertorisation with grade-weighted scoring

`Repertory` is the homeopath's arithmetic, in one file: take the rubrics a case
produced, weight every remedy by the grade it carries in each rubric, and return
a ranked list. Grades follow the classical 1/2/3 (plain, italics, bold). Zero
dependencies.

## When to use

- An app lets a practitioner pick rubrics and wants the remedy ranking.
- You are porting a repertory (Kent, Boericke, a personal one) into an offline app.
- You need `mustHave` / `exclude` filters rather than a plain sum.

## Method

1. Build rubrics with `Repertory.rubric(name, remedies)`. A remedy may be
   `["Bell", 3]` or `{ remedy: "Bell", grade: 3 }`; a missing grade counts as 1.
2. Analyse them: `Repertory.analyse(rubrics, { minGrade, mustHave, exclude, limit })`.
   `minGrade` drops weak links, `mustHave` keeps only remedies present in
   **every** rubric, `exclude` removes named remedies, `limit` caps the list.
3. Read the ranked result — `rk.remedies[0].remedy` is the top-scoring remedy —
   and show the per-rubric contribution so the practitioner can see why.
4. Feed it from the open dataset (`homoeopathic-materia-medica-repertory-json`,
   ~108k rubrics across 13 books) rather than scraping a repertory at runtime.
5. Keep the result on screen a ranking, not a prescription: the apps in this
   estate present repertorisation as a study and orientation aid.

## Key files

- `repertory-kit.js` — `rubric`, `analyse`, grade handling, filters.
- `test-node.js` — the scoring behaviour, including the filter cases.

## Gotchas

- The grade is the classical 1–3. Feeding a 0–10 severity scale produces a
  ranking that looks plausible and means nothing.
- `mustHave` is an intersection over every rubric — stricter than "has a high
  grade somewhere". It is the filter that silently empties a result.
- `boericke-repertory` and `kent-repertory-explorer` still score inside their
  own bundles and do not vendor the kit, so their numbers are not comparable
  with the kit's until they adopt it.
- Duplicate rubrics inflate a remedy twice; merge them before analysing.
- The kit is the arithmetic only. Rubric text, grades and provenance come from
  the dataset, and their licences are the dataset's.

## Source projects

- [repertory-kit](https://github.com/drsamonline/repertory-kit) — the scoring core.
- [boericke-repertory](https://github.com/drsamonline/boericke-repertory) — 6,110 rubrics over 1,461 remedies in one HTML file.
- [kent-repertory-explorer](https://github.com/drsamonline/kent-repertory-explorer) — Kent 1897, 74,667 rubrics.
- [homoeopathic-materia-medica-repertory-json](https://github.com/drsamonline/homoeopathic-materia-medica-repertory-json) — the CC0 rubric data the apps read.
