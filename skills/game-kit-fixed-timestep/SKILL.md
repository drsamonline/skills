---
name: game-kit-fixed-timestep
description: A fixed-timestep game loop with input, scenes and save/load in one dependency-free file — the shared game core the browser games should run on.
metadata:
  title: "Fixed-timestep game loop"
---

# Fixed-timestep game loop

`Game` is the core every browser game needs and every one of ours rewrites: a
loop that steps the simulation at a fixed rate whatever the display does, an
input map, scenes, and save/load. One file, zero dependencies.

## When to use

- You are starting a browser game and want the loop solved before the fun part.
- An existing game's physics change with the refresh rate (fast on a 120 Hz
  phone, slow on a laptop).
- You need input state, scene switching and a save slot without a framework.

## Method

1. `Game.create({ ... })` for the state, then `Game.start(update, render)` — the
   loop calls `update(dt)` at the fixed step and `render()` once per frame.
2. Read input through the kit's axis/`isDown` map instead of binding
   `keydown` in the game file; that is what makes a mobile and a desktop control
   scheme possible from one place.
3. Switch screens with scenes rather than boolean flags.
4. Persist with `Game.save` / the read side, and keep the save versioned — a
   changed state shape must not corrupt a player's save.
5. Draw with `art-kit` and sound with `audio-kit`; the loop does neither.

## Key files

- `game-kit.js` — `create`, `start`, `tick`, input, scenes, save.
- `test-node.js` — the loop and input behaviour.

## Gotchas

- **Six game repos hand-roll this loop**, each with its own clamp: 0.05 s in
  `retro-strike` and `dance-fight`, a ~13 ms frame cap in `retro-strike`, a
  15 ms gate in `idle-city-ages-of-growth`. Adopting the kit changes how the
  game feels — port one game, compare, then batch.
- `neon-engine` and `aethelgard-rpg-engine` are whole engines (WebGL open world,
  RPG with mods). They are not candidates for this kit and should not be
  rewritten onto it.
- The kit has no renderer and no audio: `art-kit` and `audio-kit` are the
  siblings, and neither has an adopter yet either.
- A fixed step with no accumulator cap spirals after a tab has been in the
  background; keep the cap the kit gives you.

## Source projects

- [game-kit](https://github.com/drsamonline/game-kit) — the loop, input, scenes, save.
- [neon-runner](https://github.com/drsamonline/neon-runner) — auto-fire shooter, own rAF loop.
- [retro-strike](https://github.com/drsamonline/retro-strike) — software-3D shooter with its own frame cap.
- [dance-fight](https://github.com/drsamonline/dance-fight) — rhythm fighting on an offline beat grid.
- [Scrap-and-Gun](https://github.com/drsamonline/Scrap-and-Gun) — arena defence with tactical construction.
- [idle-city-ages-of-growth](https://github.com/drsamonline/idle-city-ages-of-growth) — idle city-builder, Stone Age to Fusion Age.
- [neon-games](https://github.com/drsamonline/neon-games) — Dead Zone and Neon Police on the Neon Engine.
