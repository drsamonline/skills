---
name: app-image-toolkit
description: Compress, resize, convert, crop and strip GPS metadata from photos entirely on the device — no upload, no account, with the app split into small scripts and the whole build driven by scripts.
metadata:
  title: "On-device image toolkit"
---

# On-device image toolkit

Every other "compress my image" page uploads the photo first. This one cannot: there is no server, no account and no network request. The work happens on a canvas in `docs/play/`, and the privacy claim is a property of the architecture rather than a promise in the copy.

## When to use

- You need image processing that provably never leaves the device.
- You are stripping metadata (notably GPS) before a photo is shared.
- You want a small multi-script app with a scripted release, not a bundled framework app.

## Method

1. Split the app under `docs/play/` by concern: `imgtool.js` (decode, transform, encode), `app.js` (UI), `i18n.js` (strings), `sample.js` (the demo image), `version.js` (the displayed version), with `export-kit.js` and `web-kit.js` vendored alongside.
2. Do the transforms on a canvas and re-encode; **re-encoding is what drops EXIF**, so state that the metadata strip is a consequence of the pipeline, not a separate scrubber.
3. Keep the strings in `i18n.js` and the sample asset small enough that the page still opens fast offline.
4. Drive the build from `scripts/`: `badges.py` (SVG badges), `icons.py` (icons), `bundle.py` (the single-file bundle), `shot.py` (screenshots). Nothing is hand-drawn twice.
5. Test with `test-node.js` and release through `.github/workflows/build-apps.yml`; keep `RELEASING.md` and `NOTICE.md` current.
6. Declare what the app refuses to do in the README — it is the reason someone trusts the page.

## Key files / entry points

- `docs/play/imgtool.js` — the pipeline; `docs/play/app.js` — the UI.
- `docs/play/export-kit.js`, `docs/play/web-kit.js` — vendored kits.
- `scripts/badges.py`, `scripts/icons.py`, `scripts/bundle.py`, `scripts/shot.py`.
- `RELEASING.md`, `NOTICE.md`, `VERSION`.

## Gotchas

- Canvas re-encode drops EXIF — that is the mechanism, and it also means orientation can be lost unless you apply it before drawing.
- `toBlob` quality is a suggestion, not a guarantee; verify the output size rather than trusting the argument.
- A huge photo will exceed canvas limits on mobile; downscale in steps rather than one giant draw.
- Vendored kit copies go stale — pin the version and re-copy deliberately.

## Source projects

- [app-image-toolkit](https://github.com/drsamonline/app-image-toolkit) — the canvas pipeline, the scripted build and the refusal list.
