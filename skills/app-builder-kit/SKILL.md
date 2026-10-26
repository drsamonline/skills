---
name: app-builder-kit
description: The shared kit that turns a static web app into a single-file portable Windows EXE (PyInstaller) and an Android WebView APK (Gradle), consumed by app repos through one reusable GitHub Actions workflow.
metadata:
  title: "app-builder — shared build kit"
---

# app-builder — shared build kit

app-builder is a small, reusable kit that turns a static web app into two double-clickable, offline deliverables: a single-file portable Windows EXE (a tiny Python launcher bundled with the app) and an Android APK (a dependency-free WebView wrapper of the same app). A consuming repo adds one workflow file and gets freshly-built artefacts on a GitHub Release on every push, with stable `/releases/latest/download/<asset>` URLs.

## When to use

- You are shipping a static web app to Windows and/or Android and want the shared build logic.
- You want one workflow file per app repo rather than duplicated build code.
- You need permanent download URLs for a landing page.

## Method

1. Consume it by copying `examples/build-apps.yml` to `.github/workflows/build-apps.yml` and setting `APP_NAME` and `APP_SRC` (the folder holding `index.html`).
2. The `exe` job stages `APP_SRC` into `exe/app/` and runs `exe/build.py` (PyInstaller `--onefile`) on `windows-latest`.
3. The `apk` job stages `APP_SRC` into `apk/app/src/main/assets/www/` and runs `gradle assembleRelease` on `ubuntu-latest`.
4. The `release` job deletes and recreates the fixed-tag release (`app-latest`) so `/releases/latest` always points at the newest build.
5. Keep the keystore story honest: the committed `keystore/debug.keystore` is debug-grade and public; pass repository secrets (`KEYSTORE_FILE`, `KEYSTORE_PASSWORD`, `KEY_ALIAS`, `KEY_PASSWORD`) for a real key.
6. Maintain the kit's own landing page in `docs/` (with the standard SEO files) and document the caveats (unsigned EXE, debug-signed APK).

7. Know what the pipeline puts in the tree. In the estate as measured, 33
   repos carry a `docs/play/` mirror of the app beside the source: the source
   `index.html` and the built `docs/play/index.html` are byte-identical, so one
   app occupies two paths and the repository carries the payload twice (805 KB
   twice in `boericke-repertory`, 2,027 KB twice in `offline-pdf-toolkit`). It is
   a build output that is committed on purpose so Pages can serve it — not junk,
   and never something a cleanup pass may delete.

## What consumers vendor

A consuming repo does not only take the workflow. In the estate as measured it
also vendors the kit's shared files, and every copy is a byte-identical duplicate
of the kit's own file:

- `web-kit.js` — present in 17 apps (plus the built mirror where the app has one).
- `export-kit.js` — 7 apps; `frame-kit.js` and `optical-kit.js` — 3 apps each;
  `crypto-kit.js` — 2; `case-kit.js`, `search-kit.js`, `astro-kit.js`,
  `lan-kit.js` — 1 each.

A kit fix therefore has to be re-vendored in every consumer; that is the real
cost of vendoring rather than fetching at build time.

## Key files / entry points

- `exe/launcher.py`, `exe/build.py`, `exe/requirements.txt` — the portable EXE side.
- `apk/` — the Gradle project (settings, build, app module, manifest, `MainActivity.kt`, `strings.xml`, `assets/www/`).
- `keystore/debug.keystore` — shared debug-grade signing key.
- `examples/build-apps.yml` — the workflow a consuming repo drops in.
- `docs/` — the kit's landing page + SEO files.

## Gotchas

- The kit is public: never put a real signing key in it. Only the debug key belongs here.
- Keep `APP_NAME` consistent across jobs or the release asset names mismatch.
- The kit is checked out alongside the app repo in CI, so a change here affects every consumer at once — treat it as a released interface.
- Document the SmartScreen/Play-Protect warnings; unsigned EXE and debug-signed APK are expected.
- The demo check is hard-coded. `build.yml` compares the built app with
  `docs/play/index.html`, so any app whose public page *is* the app (a repo with
  no `docs/play` at all) fails that job however correct it is. The estate's own
  run log records the consequence: `today-card` failed "Build + deploy" five
  times, and `aethelgard-games` fails "The demo must be the app". The choice
  between an explicit `demo_path` input and deriving the demo from `app_src` is
  the owner's, because the workflow is shared by every consumer.

## Source projects

- [app-builder](https://github.com/drsamonline/app-builder) — the shared build kit behind the portable EXE and Android APK releases.

