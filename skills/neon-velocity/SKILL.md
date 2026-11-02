---
name: neon-velocity
description: A procedural retro side-scrolling shooter for Godot 4.3 where every sprite and sound is generated at runtime — no binary assets in the repository at all.
metadata:
  title: "Neon Velocity — a zero-asset Godot shooter"
---

# Neon Velocity — a zero-asset Godot shooter

A retro side-scrolling shooter for Godot 4.3 where **every sprite and every sound is generated at runtime**. The repository contains no binary art or audio: the sprites are drawn by code, the sounds are synthesised, and the scenes are text. That is what makes the project reviewable in a diff.

## When to use

- You want a Godot game whose repository has no binary assets.
- You need procedural art and audio generated at startup instead of authored.
- You want export presets and a build workflow kept in the same tree as the game.

## Method

1. Keep generation in `scripts/core/Art.gd` and `scripts/core/AudioManager.gd`; scenes (`scenes/Main.tscn`, `scenes/MainMenu.tscn`) are text files that reference those scripts, not imported textures.
2. Use `scenes/tools/DumpSprites.tscn` to dump the generated sprites when you need to *look* at what the code produced — a generator you cannot see is a generator you cannot tune.
3. Use `scenes/tools/SoakTest.tscn` for the long run, and `scripts/core/ObjectPool.gd` for the things spawned per frame.
4. Keep the shared plumbing in small autoloads: `EventBus.gd`, `SaveSystem.gd`, `TouchInput.gd`.
5. Ship the web export via `export_presets.cfg` and `.github/workflows/build.yml`; it installs as a PWA and works offline after the first load.
6. Record the review and the spec in `docs/REVIEW.md`, `docs/SPEC.md` and `AUDIT.md` — the audit is part of the tree.

## Key files / entry points

- `project.godot`, `export_presets.cfg` — the project and the exports.
- `scripts/core/Art.gd`, `scripts/core/AudioManager.gd` — generation.
- `scenes/tools/DumpSprites.tscn`, `scenes/tools/SoakTest.tscn` — the inspection and soak tools.
- `.github/workflows/build.yml`, `docs/SPEC.md`, `AUDIT.md`.

## Gotchas

- A `.import` file with no source asset (or the reverse) breaks a clean checkout — keep imports consistent with generated content.
- Generating art every frame is expensive; generate once into a texture and reuse it.
- Web exports need the PWA path to actually cache the wasm and pack files, or "offline" is only true for the first page.
- Godot version drift changes generated APIs quietly — pin 4.3 and say so.

## Source projects

- [neon-velocity](https://github.com/drsamonline/neon-velocity) — procedural art/audio, the dump and soak tools, and the web export.
