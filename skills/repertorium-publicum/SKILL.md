---
name: repertorium-publicum
description: Turn a GPL-licensed printed repertory into one offline HTML app with its printed grades intact — 74,480 rubrics, 735,460 graded remedy links and grade-weighted repertorisation, built by a reproducible pipeline rather than a hand-made page.
metadata:
  title: "Repertorium Publicum Explorer"
---

# Repertorium Publicum Explorer — a repertory you can search like a ledger

The app ships 74,480 rubrics and 735,460 graded remedy links from **Repertorium Publicum** (Vladimir Polony, 2008) — 669 remedies across 41 chapters — as one HTML file that runs with no server, no account and no network. The printed three grades are kept as grades, not flattened to a yes/no, because a repertory whose grades are lost is a different book.

## When to use

- A printed reference work has to become searchable without losing what the print encodes (grades, chapter order, the printed wording).
- You need the build to be reproducible from the source data, not a page edited by hand.
- You are reusing an open-data corpus whose licence has to travel with the output.

## Method

1. Extract from the source corpus with `pipeline/extract.py`, keeping the chapter structure the source has rather than imposing a familiar one.
2. Build the app from `pipeline/app_template.html` with `pipeline/build_app.py`; the page is generated, so a data fix is a rebuild, not an edit.
3. Keep the three printed grades as three values. Grade-weighted repertorisation and the case builder read those values; collapsing them to present/absent destroys the ranking.
4. Re-compress the payload with `pipeline/recompress.py` — the app is a single ~1.9 MB file and the payload is the reason.
5. Delegate the generic browser work (storage, export) to the vendored `web-kit.js` instead of hand-rolling it; `tests/retrofit-web-kit.test.js` is the check that the delegation happened.
6. Record provenance in `MANIFEST.json` through `tools/manifest.py` and run the tests in `tests/` before a release.

## Key files / entry points

- `pipeline/extract.py`, `pipeline/build_app.py`, `pipeline/recompress.py`, `pipeline/app_template.html` — the build.
- `web-kit.js` — the vendored shared kit.
- `tests/enhancements.test.mjs`, `tests/retrofit-web-kit.test.js` — behaviour and kit-adoption checks.
- `MANIFEST.json`, `VERSION`, `tools/manifest.py` — provenance and version.

## Gotchas

- **The attribution is part of the data.** Earlier releases described this corpus as Kent's *Repertory* 1897; it is not. It has its own chapter structure — separate *Clinical*, *Appetite*, *Blood* and *Heart & Circulation* chapters — and its own additions. That error was corrected in the README, the page, the app's footer and both manifests, and it is the kind of error that survives in a footer for years.
- The source data is **GPL v3**, which constrains what the shipped app may be licensed as; the repository carries both its own licence and `LICENSE-GPL-3.0.txt` for that reason.
- A single-file payload at this size is a deliberate trade: no network, but the first load is the whole book.
- Regenerating the page from a stale extraction silently reverts data corrections — rebuild from the current corpus.

## Source projects

- [Repertorium-Publicum](https://github.com/drsamonline/Repertorium-Publicum) — the extraction pipeline, the generated app and the corrected attribution.
