---
name: boericke-repertory
description: A free, offline digital edition of Boericke's Repertory in one HTML file: instant search across 6,110 rubrics, a repertorisation chart over 1,461 remedies, a remedy browser, cases and print/export.
metadata:
  title: "Boericke's Repertory (offline app)"
---

# Boericke's Repertory (offline app)

Boericke's Repertory is a free, offline digital edition — clinical repertory and repertorisation in one HTML file. It offers instant search across 6,110 rubrics (with matched-term highlighting and a chapter filter), a repertorisation chart that scores 1,461 remedies across selected rubrics, a remedy browser, saved cases, and print/export. No server, no build step, no dependencies.

## When to use

- You are building an offline reference/search app over a structured corpus.
- You need a repertorisation/scoring chart over graded data.
- You want a keyboard-first search UI in a single file.

## Method

1. Keep the whole app in one HTML file (root `index.html`, published at `docs/play/index.html`) with the data embedded.
2. Search: instant results across rubrics by symptom, path or remedy name, with highlighting and a chapter filter; full keyboard control (`/` focus, arrows, Enter to add).
3. Repertorise: tap rubrics to build a chart scoring every remedy (italic grade-2 = 2 points, plain grade-1 = 1) ranked by total, with top-10 bars and sorting.
4. Remedy browser: from any rubric, see every rubric listing that remedy with its grade.
5. Cases: save patient details, notes and the rubric selection + chart; reload, print, export/import as JSON.
6. Themes: light/dark/auto and five accent colours; responsive; print the chart without pop-ups.
7. Ship a landing page (`docs/index.html`) with the full SEO block, plus `robots.txt`, `sitemap.xml`, `404.html`, `.nojekyll`.

## Key files / entry points

- `index.html` — the app (root) and `docs/play/index.html` (published copy).
- `docs/index.html` — landing page; `docs/assets/search.png`, `chart.png`; `screenshots/`.
- `docs/404.html`, `docs/robots.txt`, `docs/sitemap.xml`, `docs/.nojekyll`.

## Gotchas

- Grading matters: a wrong default grade corrupts the chart. Follow the source exactly.
- Attribution is compulsory — credit Oscar E. Boericke and the app author.
- Embedding a large corpus in one file is fine but keep search indexed in memory, not by re-scanning the DOM.
- The content is study material, not medical advice.

## Source projects

- [boericke-repertory](https://github.com/drsamonline/boericke-repertory) — 6,110 rubrics, 1,461 remedies, 25 chapters.

