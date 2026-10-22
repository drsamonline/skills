---
name: Gentle Pediatrics — home companion
description: A triage-first offline companion app for a parent at the cot side: nine common childhood situations, an always-visible red-flag check, and gentle remedy orientation from the book Gentle Pediatrics.
---

# Gentle Pediatrics — home companion

Gentle Pediatrics — Home Companion is a small, offline phone app for a parent at the cot side: nine common childhood situations, a **red-flag check that is always visible**, and gentle remedy orientation from the book *Gentle Pediatrics* by Dr. Sohil Momin. Single file, no dependencies, PWA/offline-ready. Explicitly not a medical device.

## When to use

- You are building a safety-first consumer health companion where triage must precede advice.
- You want a single-file PWA with an always-visible safety check.
- You are turning a book's practical content into an offline app.

## Method

1. Keep the app single-file, offline, with no dependencies; publish at `docs/play/` and a landing page at `docs/index.html`.
2. Lead with triage: put a red-flag check that is always visible above any remedy orientation, and route urgent cases to emergency numbers.
3. Cover nine common childhood situations with plain-language guidance and remedy orientation drawn from the book.
4. Use the shared badges (`docs/badges/*.svg`) and state 'not a medical device / educational aid only' in the app and README.
5. Build EXE + APK with `.github/workflows/build-apps.yml`; keep the brief in `docs/Companion_App_Brief.md`.

## Key files / entry points

- `docs/play/index.html` — the app; `docs/index.html` — landing page.
- `docs/badges/*.svg`, `banner.svg`, `docs/Companion_App_Brief.md`.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Safety first: never present remedy orientation without the red-flag check and emergency guidance.
- Keep the 'not a medical device' disclaimer prominent in both the app and the README.
- Emergency numbers must be locale-appropriate (India: 112/108).
- The content is copyrighted — free to use, not to reuse.

## Source projects

- [gentle-pediatrics-companion](https://github.com/drsamonline/gentle-pediatrics-companion) — free to use, copyright retained.

