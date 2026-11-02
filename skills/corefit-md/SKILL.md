---
name: corefit-md
description: A five-minute, video-guided morning core routine as a static offline app: every set opens on the demonstration frame, a six-week progression, streaks and a trilingual UI, with no backend.
metadata:
  title: "CoreFit MD — clip-accurate video routine"
---

# CoreFit MD — clip-accurate video routine

A five-minute morning core routine delivered as a static app under `docs/play/`. The distinctive rule is in the playback, not the exercise list: **every set opens on the demonstration frame**, not on an intro card, so the user never waits through a title to see the movement. The app carries a six-week progression, streaks, and a UI in three languages, with no backend and no build step.

## When to use

- You are building a guided video routine where the *timing* of the clip is the product.
- You need an offline routine tracker with progression and streaks that runs from `file://` or Pages.
- You want a small app split into plain script files on one namespace instead of one giant HTML file.

## Method

1. Keep the app at `docs/play/` as eight small scripts sharing one namespace: `config.js`, `data.js`, `i18n.js`, `media.js`, `session.js`, `store.js`, `ui.js`, `video.js`, with `main.js` wiring them.
2. Encode the clip offsets in `config.js`/`data.js` so a set seeks to its demonstration frame before it plays — the offset is data, not a literal in the play handler.
3. Model the six-week progression in `data.js` and persist the current week, completed sets and streak in `store.js`.
4. Put every user-facing string in `assets/i18n/strings.js` and resolve it through `i18n.js`; the same file feeds the landing page strings where they overlap.
5. Ship `manifest.webmanifest` + `sw.js` so the app installs and works offline, and a landing page at `docs/index.html` that is visually its own thing.
6. Generate the landing badges with `scripts/badges.py` and keep the fonts local under `docs/assets/fonts/`.

## Key files / entry points

- `docs/play/index.html` — the app shell; `docs/play/assets/js/*.js` — the eight modules.
- `docs/play/assets/i18n/strings.js` — every string, in all three languages.
- `docs/play/sw.js`, `docs/play/manifest.webmanifest` — offline + install.
- `docs/index.html` — landing page; `scripts/badges.py` — the badge SVGs.

## Gotchas

- Seeking a video element before `loadedmetadata` fires silently does nothing; set the offset only once metadata is available.
- A progression that lives in memory is a progression lost on a phone reload — persist every set completion immediately.
- Video is the largest asset in the app; the "offline" promise depends on it being cached by the service worker, not merely referenced.
- Trilingual UI triples the string surface: a missing key must fall back to English rather than render blank.

## Source projects

- [corefit-md](https://github.com/drsamonline/corefit-md) — the eight-module `docs/play/` layout, clip offsets and six-week progression.
