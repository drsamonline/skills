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

## Source projects

- [app-builder](https://github.com/drsamonline/app-builder) — the shared build kit behind the portable EXE and Android APK releases.

