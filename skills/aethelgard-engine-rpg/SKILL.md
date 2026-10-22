---
name: Aethelgard Engine — vanilla-JS RPG engine
description: The vanilla-JavaScript engine behind Aethelgard: Chronicles of Fate — small modules loaded in script order behind one global (window.Game), no build step, no dependencies, fully offline, moddable.
---

# Aethelgard Engine — vanilla-JS RPG engine

Aethelgard Engine is the vanilla-JavaScript engine behind *Aethelgard: Chronicles of Fate*, a deep single-player browser RPG. Small modules are loaded in script order behind one global (`window.Game`); there is no build step, no dependencies, and it is fully offline. Mods are drop-in JS files, and the art is separately licensed from the MIT code.

## When to use

- You want an RPG engine with no build step and a single global namespace.
- You need a drop-in mod loading pattern for a browser game.
- You want a reference for a large game kept as ordered plain-script modules.

## Method

1. Keep the engine as many small plain-script modules loaded in a fixed order; everything hangs off one global (`window.Game`) rather than ES imports, so it runs from `file://` and static hosting alike.
2. Model the RPG systems as modules: classes, races, branching story, crafting, settlement building, an underworld/crime layer, an endless dungeon, and a hover wiki.
3. Support drop-in mods (plain JS files) documented in `mods/README.md`.
4. Make it PWA-installable and offline-first; no server, no build step.
5. Test with `.github/workflows/ci.yml` and build EXE + APK with `.github/workflows/build-apps.yml`.
6. Keep the code MIT and the art under a separate reserved licence (`LICENSE-ASSETS.md`); keep AI art prompts (`*_ICON_PROMPTS.md`) alongside.

## Key files / entry points

- Ordered engine modules behind `window.Game`; `index.html` loader.
- `mods/README.md`, `HOW_TO_PLAY.md`, `CHANGELOG.md`.
- `LICENSE` (MIT code) and `LICENSE-ASSETS.md` (art reserved).
- `.github/workflows/ci.yml`, `.github/workflows/build-apps.yml`.

## Gotchas

- Script load order is the module system — a reordered tag silently breaks the engine.
- One global namespace is deliberate (works from `file://`); keep names namespaced under `window.Game` to avoid collisions.
- Code licence (MIT) and art licence (reserved) are different — do not conflate them.
- Mods run in the same context as the game; document that trust boundary.

## Source projects

- [Aethelgard-Engine](https://github.com/drsamonline/Aethelgard-Engine) — MIT code, art reserved.

