---
name: saga-vn-engine
description: Build a browser visual novel with no build step: a small set of plain-JS modules, scenes authored as `.scene` text, and the story kept out of the engine repository so the two can be licensed separately.
metadata:
  title: "Saga"
---

# Saga — a visual-novel engine that reads plain-text scene files

A small, dependency-free visual-novel engine for the browser: plain JavaScript, one stylesheet, no build step, works offline. It ships no story and no artwork — you bring your own — and it powers *Aethelgard — The Books* (36 chapters, seven endings).

## When to use

- You want a visual novel in the browser with no bundler and no framework.
- Writers should author in a text format, not in code.
- The engine is public but the story is not, so they must live in different repositories.

## Method

1. Split the runtime into named modules under `js/`: `boot`, `core`, `script`, `play`, `ui`, `chars`, `graphics`, `music`, `endings`, `mods`.
2. Author content as `.scene` files in `scenes/`, with `scenes/manifest.js` listing them; the engine reads text, so a writer never touches JavaScript.
3. Bundle assets with `tools/make-bundle.py` and index sprites with `tools/make-sprite-index.py` — the two build steps that exist are for assets, not for code.
4. Keep endings in `endings.js` as data the script can reach, so a branch is authored, not coded.
5. Support `mods/` from the start: a mod is content in the same shape as the game's own scenes.
6. Licence the engine (MIT) separately from the story and artwork, and keep the latter out of the repository.

## Key files / entry points

- `js/boot.js`, `js/core.js` — the runtime.
- `js/script.js`, `js/play.js` — the script interpreter and the play loop.
- `scenes/*.scene`, `scenes/manifest.js` — the content format.
- `tools/make-bundle.py`, `tools/make-sprite-index.py` — asset preparation.
- `mods/`, `assets/`, `css/` — content and presentation.

## Gotchas

- No build step for code means load order in the page is the dependency graph; a new module has to be added there, not just to the directory.
- Scene text is the API: changing the `.scene` grammar breaks every existing story, so extend it rather than redefining it.
- A visual novel engine that ships with a story is a game, not an engine — the empty default scene is deliberate.
- Sprite indexes are generated; a hand-edited index drifts from the assets on the next run.

## Source projects

- [saga-vn-engine](https://github.com/drsamonline/saga-vn-engine) — the module split, the `.scene` format and the asset tooling.
- [aethelgard-games](https://github.com/drsamonline/aethelgard-games) — the game it powers.
