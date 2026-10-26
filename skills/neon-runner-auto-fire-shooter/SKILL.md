---
name: neon-runner-auto-fire-shooter
description: A retro auto-fire side-scrolling shooter in one self-contained HTML file (vanilla JS + canvas): move, jump, duck — the gun fires itself — with 60+ assertions, minified to ~176 KB.
metadata:
  title: "Neon Runner — auto-fire shooter"
---

# Neon Runner — auto-fire shooter

Neon Runner is a retro auto-fire side-scrolling shooter where you never press fire: move, jump, duck, and the gun shoots anything in range. It is one self-contained HTML file (vanilla JS + canvas, Web Audio), ~176 KB minified / ~61 KB gzipped, works offline, and has 60+ test assertions. PolyForm Noncommercial licensed.

## When to use

- You want to build or extend a single-file canvas action game.
- You need a reference for an auto-fire control scheme and upgrade-card loop.
- You want a game that also ships as a portable EXE and an APK.

## Method

1. Keep the game in one HTML file with a canvas and an update/render loop; no dependencies, no build step for the source (a minified build exists in `dist/`).
2. Auto-fire: the weapon fires on a timer at the nearest target in range; the player only moves, jumps and ducks, which keeps mobile controls simple.
3. Use pixel-art upgrade cards and a codex; balance lives in `docs/BALANCE.md`, architecture in `docs/ARCHITECTURE.md`.
4. Add 60+ assertions (`docs/AUDIT.md`) and run them in `.github/workflows/ci.yml`.
5. Publish the playable copy at `docs/play/index.html` and a landing page at `docs/index.html` (with `robots.txt`, `sitemap.xml`, `404.html`, `.nojekyll`).
6. Build the portable EXE + APK with `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/index.html` — the playable game; `docs/index.html` — landing page.
- `docs/ARCHITECTURE.md`, `docs/BALANCE.md`, `docs/AUDIT.md`.
- `.github/workflows/ci.yml`, `.github/workflows/build-apps.yml`.

## Gotchas

- Auto-fire must not make the game trivial — the challenge is positioning and timing, not aiming.
- Mobile needs touch controls; test at phone sizes.
- Keep the single file self-contained so it still works offline and inside the EXE/APK wrappers.

## Source projects

- [neon-runner](https://github.com/drsamonline/neon-runner) — MIT, v3.0.1.

