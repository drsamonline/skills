---
name: app-thermals
description: What each classical homeopathic source actually says about a remedy's thermal reaction, quoted in its own words with the source named, and where the sources disagree — with a documented extraction and repair pipeline.
metadata:
  title: "Thermals — quoted-source remedy comparison"
---

# Thermals — quoted-source remedy comparison

The app answers a narrow question — what does each classical source say about a remedy's thermal reaction — and answers it with **quotations and attributions**, not with a synthesised summary. Where the sources do not say the same thing, the app shows the disagreement instead of resolving it.

## When to use

- You are presenting primary-source material and the disagreement between sources is the content.
- You need an extraction pipeline whose corrections are recorded as data, not as edits.
- You want a comparison view over several editions of the same reference work.

## Method

1. Keep every source as data: `data/bell-1906-index.json`, `data/bell-pages.json`, `data/bell-second-scan.json`, `data/bell-alignment.json` for the extraction and alignment of the Bell material, plus `data/rows.json` and `data/remedies.json` for the derived view.
2. Record name corrections as data — `data/name-map.json`, `data/name-overrides.json`, `data/name-crosscheck.json`, `data/reference-names.json` — so a wrong name is a fixable row, not a code change.
3. Record text repairs in `data/text-repairs.json`, and state the extraction rule in the README so a reader can judge the pipeline.
4. Bundle with `tools/make-bundle.py` into `docs/play/data/bundle.js` and render with `docs/play/thermals.js`; `tools/extract.py` is the extraction entry point.
5. Test with `node test-node.js` (`npm test`) and build with `npm run build`; release through `.github/workflows/build-apps.yml`.
6. Declare what the app must not do — it quotes; it does not prescribe.

## Key files / entry points

- `data/*.json` — sources, alignment, name maps, repairs.
- `tools/extract.py`, `tools/make-bundle.py` — extraction and bundling.
- `docs/play/thermals.js`, `docs/play/data/bundle.js` — the app and its data.
- `test-node.js`.

## Gotchas

- Aligning two scans of the same edition is a page-level problem; a paragraph-level diff will report thousands of false disagreements.
- A name map applied silently hides the original text — keep the raw name beside the corrected one.
- "Quoted in its own words" fails the moment a modern paraphrase enters the dataset; the extraction rule has to say what is allowed.
- A bundle regenerated from stale JSON looks exactly like a correct one; make the build part of the release, not a manual step.

## Source projects

- [app-thermals](https://github.com/drsamonline/app-thermals) — the source/alignment/name-map/repair data model and its bundle pipeline.
