---
name: Conqueror OS — resilience workspace
description: A private, offline resilience workspace in a single HTML file — read, reflect, journal, track and review — with no server, no account and no dependencies.
---

# Conqueror OS — resilience workspace

Conqueror OS is a private, offline resilience workspace that lives in a single HTML file: read, reflect, journal, track and review — no server, no account, no build step required to run it. It is the reference implementation of the single-file, offline-first app pattern for a personal, data-owning tool.

## When to use

- You are building a personal, private, offline tool where the user owns all data.
- You want the canonical single-file app structure (inline CSS/JS, local storage, export/import).
- You need a habits/journal/spaced-review loop in one file.

## Method

1. Keep everything in one HTML file (inline CSS/JS, inline SVG icons); no dependencies, no build step to run it.
2. Persist all state locally (IndexedDB/localStorage) and provide export/import so the user owns their data.
3. Organise the app around a read → reflect → journal → track → review loop, with a spaced-repetition review of entries.
4. Add a distinct visual theme (this site's palette is its own) and full responsiveness.
5. Ship a landing page (`docs/index.html`) and a play copy (`docs/play/`); build EXE + APK with `.github/workflows/build-apps.yml`; run tests in `.github/workflows/ci.yml`.
6. Version and changelog in `CHANGELOG.md`; MIT for the code.

## Key files / entry points

- `docs/play/index.html` — the app; `docs/index.html` — landing page.
- `.github/workflows/build-apps.yml`, `.github/workflows/ci.yml`.
- `CHANGELOG.md`, `LICENSE`, `CONTRIBUTING.md`, `.ai`/governance docs where present.

## Gotchas

- Privacy is the feature: no telemetry, no account, no network call — do not add an 'optional' sync.
- Local storage can be evicted; export must be easy and prominent.
- Keep the file self-contained so it runs from `file://` as well as Pages.

## Source projects

- [conqueror-os](https://github.com/drsamonline/conqueror-os) — MIT code, single HTML file.

