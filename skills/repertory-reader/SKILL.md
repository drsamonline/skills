---
name: repertory-reader
description: Read a large open corpus the way it was printed — chapters in printed order, remedies beside their rubrics, treatises rendered as prose — and be explicit that a reader which starts guessing stops being evidence.
metadata:
  title: "Repertory Desk"
---

# Repertory Desk — a reader that shows the book and refuses to score it

A quiet reading room for sixteen classical homoeopathic repertories, six materia medicas and forty public-domain treatises — 352,063 rubrics, 1,429,263 remedy links (751,907 graded) and 5,392 sections of prose — read straight from the open JSON library. No account, no server, no tracking, no build step.

## When to use

- You are presenting a scholarly corpus where the presentation itself is a claim about accuracy.
- Volumes differ in kind (repertory, materia medica, treatise) and must not be flattened into one shape.
- You need offline reading over a large corpus in the browser.

## Method

1. Open a volume on its own contents and keep the printed order: Knerr's 43 chapters, Kent's 34, Gentry's A–Z; a single-file volume builds its contents from the sections inside the file.
2. Render each kind of volume its own way — a numbered treatise (the Organon) shows a § against each paragraph, a chaptered one shows its chapter title, and no volume is merged with another.
3. Make every remedy a door: a chip filters the volume to the rubrics that list it, and the rail can list a volume by its drugs instead of its chapters.
4. Search in three scopes — the open chapter, the volume, then every volume already on the device — including remedy abbreviations and resolved names.
5. Keep chapters in IndexedDB and serve them with a service worker, but keep **HTML network-first** so a release is never hidden behind a stale cache.
6. Carry the source with each passage: a paragraph records the edition it was read from and the fraction of its 12-letter sequences found verbatim in OCR scans of that edition.

## Key files / entry points

- `docs/play/` — the reader (a committed page; the repository has no build step).
- `docs/index.html` — the landing page; `docs/assets/` — its images and badges.
- `docs/AUDIT-2026-11-02-deep.md`, `docs/AUDIT-2026-11-02-reader.md` — the audits of the reader.
- `MANIFEST.json`, `LOCKED.md` — provenance and the lock state.

## Gotchas

- **A reader that repertorises has stopped being evidence.** This repository does not score, rank, correct or complete anything, and that restraint is the product.
- Network-first for HTML and cache-first for chapters is the combination that keeps offline reading from pinning an old release.
- Two editions of the same book are two books: the two Organons differ in 74 paragraphs and §292–§294 exist only in the fifth, so merging them destroys exactly the evidence the reader exists to show.
- The app is committed under `docs/play/`; there is no build in this repository, so an edit to the page is a direct edit to the shipped artefact.

## Source projects

- [repertory-reader](https://github.com/drsamonline/repertory-reader) — the reader, the volume kinds and the provenance display.
