---
name: Neon Games — open-world browser arcade
description: A deployment repo holding two open-world games built on the Neon Engine — Dead Zone (zombie survival) and Neon Police (crime response) — each a self-contained playable folder with a mod loader.
---

# Neon Games — open-world browser arcade

Neon Games is a **deployment repo**: it holds the built, playable copies of two open-world browser games built on the Neon Engine — *Dead Zone* (endless zombie survival) and *Neon Police* (crime response, arrests pay better than kills). Each game is its own self-contained folder with an `index.html`, a service worker, a web manifest and a `mods/` loader. No install, no account, no backend.

## When to use

- You are shipping a game built on the Neon Engine and want the deployment layout.
- You need a mod-loading pattern (drop-in JS files) for a browser game.
- You want a landing page (arcade lobby) that links multiple games.

## Method

1. Keep each game in its own folder (`dead-zone/`, `neon-police/`-style) with `index.html`, `hud.css`, a game JS file, `manifest.webmanifest`, `sw.js` and `icons/`.
2. Ship a mod loader: a `mods/` folder with an `example-pack.js` and a `MODDING.md` describing the drop-in contract.
3. Provide a local `serve.py` so a contributor can run the games offline.
4. Publish an arcade lobby landing page at `docs/index.html` linking each game at `docs/play/<game>/`.
5. Build the portable EXE + APK for each game with `.github/workflows/build-apps.yml` (asset names like `neon-games-dead-zone-portable.exe`).
6. Licence the games CC BY-NC-SA 4.0 while the underlying engine stays MIT.

## Key files / entry points

- `dead-zone/index.html`, `dead-zone/survival.game.js`, `dead-zone/sw.js`, `dead-zone/manifest.webmanifest`, `dead-zone/mods/example-pack.js`, `dead-zone/MODDING.md`.
- `docs/index.html` — the arcade lobby landing page.
- `.github/workflows/build-apps.yml`.

## Gotchas

- This repo holds *built* copies — the engine source lives in `neon-engine`, so a fix belongs there.
- Keep the game licence (CC BY-NC-SA) distinct from the engine licence (MIT).
- Asset names in the release must be per-game (`neon-games-<game>-portable.exe`) so downloads are unambiguous.
- Service workers and mods both need a real http origin for local testing — `serve.py` exists for that.

## Source projects

- [neon-games](https://github.com/drsamonline/neon-games) — deployment repo, CC BY-NC-SA 4.0.

