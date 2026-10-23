---
name: neon-engine-open-world
description: A code-only WebGL engine for open-world browser shooters: no asset files, every texture/mesh/sound generated at runtime, ES modules with a vendored three.js, so a full game ships under 1 MB.
metadata:
  title: "Neon Engine — code-only open-world engine"
---

# Neon Engine — code-only open-world engine

Neon Engine is a code-only open-world game engine for the browser. There are no asset files: every texture, mesh and sound is generated at runtime, so a complete open-world shooter ships under ~1 MB and runs offline. It uses a vendored three.js (r160) plus ES modules, and powers two shipped games (Dead Zone, Neon Police). A new game is mostly a config object plus modules.

## When to use

- You want to build a browser 3D game with no binary assets.
- You need a procedural texture/mesh/audio generation layer.
- You want an ES-module engine that runs offline from static hosting.

## Method

1. Structure the engine as small ES modules (AI, allies, ambience, audio, base/entities, …) loaded together; a new game is a config object plus a few modules.
2. Generate everything procedurally at runtime — textures (canvas), meshes and audio — so no asset pipeline is needed.
3. Vendor three.js (r160) into the repo (`BufferGeometryUtils.js`, etc.) rather than loading it from a CDN, preserving the offline/no-dependency promise.
4. Keep a test workflow (`.github/workflows/test.yml`) and document the engine in `README.md`, `ROADMAP.md`, `CONTRIBUTING.md`.
5. Ship games as separate deployment repos (`neon-games`) built on top of the engine.

## Key files / entry points

- Engine modules at the repo root (`ai.js`, `ally.js`, `ambience.js`, `audio.js`, `base.js`, …).
- Vendored three.js files (`BufferGeometryUtils.js`, …).
- `.github/workflows/test.yml`, `README.md`, `ROADMAP.md`.

## Gotchas

- 'No dependencies' here means *no runtime download*: three.js is vendored in-tree. Do not swap it for a CDN import.
- Procedural generation must be deterministic per seed or saves and tests become unstable.
- Keep the engine MIT so others can build commercial games, separate from any game's licence.
- WebGL2 is required — feature-detect and message gracefully.

## Source projects

- [neon-engine](https://github.com/drsamonline/neon-engine) — MIT, three.js r160 vendored, ES modules.

