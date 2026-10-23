---
name: retro-strike-software-3d
description: A complete retro third-person shooter in one HTML file with a custom software 3D renderer, a live chiptune synth and procedural arenas — no engine, no build step, no dependencies.
metadata:
  title: "Retro Strike — software 3D shooter"
---

# Retro Strike — software 3D shooter

Retro Strike is a complete retro-styled third-person shooter that lives inside a single HTML file. It has a **custom software 3D renderer** (no WebGL), a live chiptune synthesiser and procedural arenas — no engine, no build step, no dependencies. ~99 KB minified. MIT licensed.

## When to use

- You want to build a 3D game without a 3D library or WebGL.
- You need a reference software rasteriser and a procedural arena generator.
- You want a single-file game that ships as EXE + APK.

## Method

1. Write a software 3D renderer (project → transform → rasterise to canvas) inside one HTML file; no WebGL and no engine.
2. Generate arenas procedurally so no level assets ship.
3. Synthesise chiptune audio at runtime with the Web Audio API.
4. Support desktop, mobile and gamepad input; document controls in the README.
5. Keep a minified single-file build (`dist/retro-strike.min.html`) and a landing page + play copy in `docs/`.
6. Build the portable EXE + APK with `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/index.html` — the playable game; `docs/index.html` — landing page.
- `dist/retro-strike.min.html` — minified single-file build.
- `assets/` — banner, logo, screenshots.
- `.github/workflows/build-apps.yml`.

## Gotchas

- A software renderer is fill-rate bound — keep the canvas resolution modest and cap the polygon budget.
- Touch and gamepad support must be designed in, not bolted on.
- Keep it dependency-free: no three.js, no engine, to preserve the single-file/offline promise.

## Source projects

- [retro-strike](https://github.com/drsamonline/retro-strike) — MIT, v1.4.0.

