---
name: materia-medica-builder
description: An offline, no-dependency PWA that lets a practitioner build a personal materia medica and repertory — remedies, symptoms, rubrics, a custom marking scale — and export it in eight formats.
metadata:
  title: "Materia Medica Builder"
---

# Materia Medica Builder

Materia Medica Builder is a single self-contained PWA: no server, no account, no tracking, no CDN. It helps any practitioner assemble a personal materia medica and repertory — every remedy, symptom, rubric and grade defined and edited by hand — with a custom marking scale, a guided first-run tour, and export/import in eight formats (JSON, CSV, XLSX, PDF, HTML, SQL, SQLite).

## When to use

- You are building an offline authoring app whose output must be portable across many formats.
- You need a pattern for a multi-tab PWA (materia medica, repertory, marking, data, help, about) with a first-run tour.
- You want a client-side exporter for structured health data.

## Method

1. Keep the app self-contained under `docs/play/` with plain JS modules: `app.js`, `builders.js`, `db.js`, `diagrams.js`, `docs.js`, `exporters.js`, `importers.js`, `tour.js`, plus `css/styles.css`.
2. Persist everything locally (`db.js` over IndexedDB); no server, no account, no tracking, no CDN.
3. Model two builders — materia medica (remedy → symptoms → chapters/grades) and repertory (rubric → graded remedies) — with a user-defined marking scale.
4. Provide a first-run guided tour (`tour.js`) that can be replayed from the Help tab.
5. Implement exporters/importers for eight formats (JSON, CSV, XLSX, PDF, HTML, SQL, SQLite) so the user owns and can move their data.
6. Support light/dark/system themes and i18n-ready copy.
7. Ship a landing page at `docs/index.html` and build EXE + APK with `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/index.html`, `docs/play/js/*` (app, builders, db, exporters, importers, tour, diagrams, docs), `docs/play/css/styles.css`.
- `docs/index.html` — landing page; `docs/architecture.svg`, `docs/workflow.svg`, `docs/marking-scale.svg`, screenshots.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Export must be lossless and re-importable — round-trip each format in tests.
- SQLite/XLSX export in the browser needs a library; if you avoid dependencies, emit SQL text and CSV/XLSX via minimal writers rather than pulling a heavy bundle.
- Keep the data model aligned with the open JSON schema so exports interoperate with the datasets.
- Licence: free with attribution — state it in the landing page and app.

## Source projects

- [MATERIA-MEDICA-BUILDER](https://github.com/drsamonline/MATERIA-MEDICA-BUILDER) — offline PWA, vanilla JS, eight export formats.

