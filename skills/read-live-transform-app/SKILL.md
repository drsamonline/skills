---
name: Read. Live. Transform. — companion
description: An offline PWA companion to the book Read. Live. Transform. — a practical reading of the Qur'an in 74 chapters: read the verse, live the practice, keep the change.
---

# Read. Live. Transform. — companion

Read. Live. Transform. is the companion app to the book of the same name by Dr Sohil Momin — a practical reading of the Qur'an. Read the verse, live the practice, keep the change. It is an offline PWA with no dependencies, covering 74 chapters in ~292 KB, with all rights reserved.

## When to use

- You are building an offline reading + practice PWA over a fixed text.
- You want a chapter-by-chapter reader with a practice/journal step.
- You need the fully-documented companion-app layout (architecture, features, install, credits).

## Method

1. Keep the app offline and installable; publish at `docs/play/` with a manifest and service worker; landing page at `docs/index.html`.
2. Structure the reader as 74 chapters: read the verse, then a practice step, then a keep-the-change reflection.
3. Persist reflections locally; no accounts, no tracking.
4. Document thoroughly in `docs/ARCHITECTURE.md`, `FEATURES.md`, `INSTALL.md`, `AUDIT.md`, `CREDITS.md`.
5. Build EXE + APK with `.github/workflows/build-apps.yml`.
6. State the licence: all rights reserved, permission required to reuse.

## Key files / entry points

- `docs/play/index.html` — the app; `docs/index.html` — landing page.
- `docs/ARCHITECTURE.md`, `FEATURES.md`, `INSTALL.md`, `AUDIT.md`, `CREDITS.md`.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Sacred text must be reproduced exactly — no paraphrase, no truncation.
- The licence is all-rights-reserved; the app is free to use, not to reuse.
- Keep it offline-first and dependency-free.

## Source projects

- [read-live-transform-app](https://github.com/drsamonline/read-live-transform-app) — all rights reserved, offline PWA, 74 chapters.

