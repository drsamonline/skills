---
name: Open Materia Medica
description: A plain-language homeopathic materia medica — 344 remedy portraits, each beside the substance's real pharmacology and toxicology — as a static web edition plus a hand-written Android companion app.
---

# Open Materia Medica

Open Materia Medica is the classical homeopathic materia medica in plain language: 344 remedy portraits, each set beside the real pharmacology and toxicology of the substance it is made from. It ships as a static web edition (the full library at `/play/`, source in `docs/play/`) and as an offline Android companion app built from a hand-written Gradle project.

## When to use

- You are publishing a book's web edition as a static site plus a mobile companion.
- You want a hand-written Android WebView project (as opposed to the shared `app-builder` kit) with an asset-sync script.
- You need a layout that separates a landing page from a large served library.

## Method

1. Serve the landing page at `docs/index.html` and the full library at `docs/play/` (source in `docs/play/`). The site is a static, offline-capable build.
2. Build the Android app from the hand-written `android/` Gradle project (`app/build.gradle`, `MainActivity.java`, `com.matneo.omm`), with `android/sync-assets.sh` copying the web edition into the app's assets.
3. Document the Android specifics in `android/README.md` and `android/ANDROID_NOTES.md`.
4. Also wire the shared build workflow (`.github/workflows/build-apps.yml`) for the portable EXE + APK release assets.
5. Link downloads to the stable release URLs (`…/releases/latest/download/open-materia-medica-portable.exe`, `…apk`).
6. State the licence clearly: (c) 2026, all rights reserved.

## Key files / entry points

- `docs/index.html` (landing), `docs/play/` (the library).
- `android/` — Gradle project, `MainActivity.java`, `sync-assets.sh`, `ANDROID_NOTES.md`.
- `.github/workflows/build-apps.yml`.
- `assets/` — icon, og image, author image.

## Gotchas

- Keep the served library (`docs/play/`) separate from the landing page so the landing page stays light.
- A hand-written Android project needs its asset sync run before a build — automate it or it drifts.
- The licence is all-rights-reserved; the web edition is free to read, not to reuse.
- The medical content is study material, not advice — keep the disclaimer.

## Source projects

- [open-materia-medica](https://github.com/drsamonline/open-materia-medica) — 344 portraits, all rights reserved.

