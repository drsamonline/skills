---
name: app-organon-reader
description: An offline reader for the Organon of Medicine (6th edition, Boericke 1922 translation): a three-scan extraction pipeline, full-text search, bookmarks and notes, with no network at runtime.
metadata:
  title: "Organon reader — public-domain text pipeline"
---

# Organon reader — public-domain text pipeline

The app is small; the work is the text. *Organon of Medicine*, sixth edition, in Boericke's 1922 translation, was read from **three Internet Archive scans of that printing** and merged into one clean dataset, which is then inlined as `docs/organon-data.js` and read by `docs/reader.js`. At runtime there is no server and no network.

## When to use

- You are turning a public-domain book into an offline reader with search, bookmarks and notes.
- You need to merge several scans of the same printing into one text and keep the disagreements visible.
- You want the reader to be a data file plus a small script, not a framework.

## Method

1. Extract with `tools/extract.py`, one pass per scan, keeping the page boundaries so a quotation can be traced back.
2. Build the merged dataset with `tools/build-data.py`; where the scans disagree, keep the choice in the build step rather than editing the output by hand.
3. Emit `docs/organon-data.js` as a plain script assignment so the reader works from `file://` with no fetch.
4. Implement search, bookmarks and notes in `docs/reader.js` against that data file; store bookmarks and notes locally.
5. Prove the data with `test-node.js` (`node test-node.js`) — chapter counts, verse continuity, no empty paragraphs.
6. Release through `.github/workflows/build-apps.yml` and `test.yml`; bump `VERSION` and `CHANGELOG.md` together.

## Key files / entry points

- `tools/extract.py`, `tools/build-data.py` — the pipeline.
- `docs/organon-data.js` — the merged text; `docs/reader.js` — the reader.
- `docs/index.html` — landing page; `data/README.md` — provenance of the source scans.
- `test-node.js` — the data checks.

## Gotchas

- Two scans of the same printing differ in OCR noise, not in text; a merge rule that picks "the longer paragraph" quietly invents content.
- Inlining the whole book makes the page large — measure the emitted file before adding a second book to it.
- A translation is a separate copyright question from the original work; name the edition and the translator, and check the translation's own status.
- Bookmarks keyed by array index break the moment the dataset is rebuilt; key them by chapter and paragraph id.

## Source projects

- [app-organon-reader](https://github.com/drsamonline/app-organon-reader) — the three-scan pipeline and the data-plus-script reader.
