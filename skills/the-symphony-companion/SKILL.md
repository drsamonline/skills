---
name: the-symphony-companion
description: A pocket PWA companion to The Symphony of the Present: the book's ideas as cards, its practices as a checklist, a breathing timer, a gratitude journal and attributed quotations — pure CSS tabs, offline.
metadata:
  title: "The Symphony Companion"
---

# The Symphony Companion

The Symphony Companion is a pocket companion to *The Symphony of the Present: Waking Up from the Illusion of Tomorrow*. Not the book — a companion: the book's ideas as cards, its practices as a checklist, a breathing timer, a gratitude journal and its attributed quotations. Installable PWA, works offline, no accounts, no tracking. Notable for its pure-CSS tabs.

## When to use

- You are building a lightweight book companion PWA.
- You want a pure-CSS tab pattern with no JS framework.
- You need a breathing timer and a local gratitude journal.

## Method

1. Keep the app offline and installable; publish at `docs/play/` with a `manifest.webmanifest` and `sw.js`; landing page at `docs/index.html`.
2. Organise content as tabs implemented in pure CSS (no JS framework): Today, Chapters, Breathe, Journal and quotations.
3. Implement a breathing timer and a gratitude journal persisted locally.
4. Attribute every quotation to its source.
5. Build EXE + APK with `.github/workflows/build-apps.yml`; document in `DOCUMENTATION.md`.
6. Licence: personal, non-commercial use only.

## Key files / entry points

- `docs/play/index.html`, `docs/play/sw.js`, `docs/play/manifest.webmanifest`.
- `docs/index.html` — landing page; `docs/screenshot-*.png`.
- `.github/workflows/build-apps.yml`, `DOCUMENTATION.md`.

## Gotchas

- Pure-CSS tabs need careful focus/ARIA handling to stay accessible.
- Quotations must be attributed — never present them unattributed.
- Keep it offline-first; no analytics, no accounts.
- The licence is personal/non-commercial — state it clearly.

## Source projects

- [the-symphony-companion](https://github.com/drsamonline/the-symphony-companion) — personal-use licence, PWA.

