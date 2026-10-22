---
name: AethelgardVN — Saga visual-novel engine
description: Saga: a small, dependency-free visual-novel engine for the browser — plain JavaScript, one stylesheet, no build step, works offline — built to make Aethelgard: The Books.
---

# AethelgardVN — Saga visual-novel engine

Saga is a small, dependency-free visual-novel engine for the browser: plain JavaScript, one stylesheet, no build step, works offline from a static file server. It was built to make *Aethelgard — The Books* and released on its own so others can make something else with it. Sprites and backgrounds live in `assets/sprites/` with an `index.json` manifest.

## When to use

- You want to build a visual novel with no engine dependency and no build step.
- You need a small script/choice system with sprite and background management.
- You want a reference for an asset manifest-driven browser VN.

## Method

1. Keep the engine to plain JS modules plus one stylesheet (`css/style.css`); no build step, run from a static server.
2. Drive the story from a script/scene format; track choices and route to endings (the shipped game uses four hidden counters whose *shape* picks the ending).
3. Load art from `assets/sprites/` through an `index.json` manifest so scenes reference named sprites/backgrounds.
4. Publish a play copy at `docs/play/` and a landing page at `docs/index.html`.
5. Build the portable EXE + APK with `.github/workflows/build-apps.yml`.

## Key files / entry points

- `css/style.css`, engine JS modules, the story/script data.
- `assets/sprites/index.json`, `assets/sprites/index.js`, `*.webp` backgrounds/sprites.
- `docs/play/` — play copy; `docs/index.html` — landing page.
- `.github/workflows/build-apps.yml`.

## Gotchas

- No build step means the browser loads raw modules — keep the file count and import graph tidy.
- Sprite manifests must stay in sync with the files or scenes break silently.
- The engine is MIT; the *game* art and story may be separately licensed — keep the distinction.

## Source projects

- [AethelgardVN](https://github.com/drsamonline/AethelgardVN) — MIT, v1.0.1.

