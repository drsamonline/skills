---
name: aethelgard-rpg-engine
description: Build a deep single-player browser RPG with no build step and no dependencies: small modules loaded in script order behind window.Game, with the story and artwork kept out of the engine repository.
metadata:
  title: "Aethelgard RPG Engine"
---

# Aethelgard RPG Engine — a vanilla-JS RPG engine behind one global

A dependency-free engine for deep single-player browser RPGs: no build step, no dependencies, works offline, and everything hangs off one global (`window.Game`). It ships as **engine only** — a small generic sample world — because the games built on it are a separate work.

## When to use

- You want an RPG in the browser without a bundler, a framework or a package manager.
- You are publishing an engine and a game as two different things with two different licences.
- You need a module layout where load order is the dependency graph.

## Method

1. Load the modules in script order; each one attaches to `window.Game`, so the order in `index.html` is the dependency declaration and there is nothing else to resolve.
2. Keep the split the repository uses: `js/core.js` and `js/boot.js` for the loop and lifecycle, then one module per system — `combat`, `companions`, `maps`, `quests`, `world`, `late-game`, `ui`, `views`, `music`, `mods`, `graphics`, `wiki`, `diagnostics`, `validate`.
3. Put world data in `js/data/` rather than inside the systems, so a new world is data, not code.
4. Validate content with `js/validate.js` and run the two test files (`test8.js`, `test9.js`) before a release.
5. Keep the engine's licence (MIT) separate from the game's content licence, and keep the content out of the repository entirely.

## Key files / entry points

- `js/boot.js`, `js/core.js` — the loop and the global.
- `js/*.js` — one system per module.
- `js/data/` — the sample world.
- `test8.js`, `test9.js`, `js/validate.js` — checks.
- `ARCHIVED.md` — the signpost for material moved to `drsamonline/audit`.

## Gotchas

- **Script order is the dependency graph.** A module that reads another's global before it is defined fails only at runtime, in the browser, in the one code path you did not test.
- Reference material that is not part of the project belongs in the archive repository, not in the engine tree — `ARCHIVED.md` is how that move is recorded without deleting history (`audit/archive/<repo>/<original path>`).
- The engine and the game must not share a licence file; shipping the story under the engine's MIT is the mistake this split exists to prevent.
- `manifest.json`, `sw.js` and `style.css` at the root are the page's own; a second copy of any of them in a subdirectory is drift.

## Source projects

- [aethelgard-rpg-engine](https://github.com/drsamonline/aethelgard-rpg-engine) — the module layout, the sample world and the engine/content licence split.
- [aethelgard-games](https://github.com/drsamonline/aethelgard-games) — the games the engine powers.
