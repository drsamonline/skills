---
name: hellgate-procedural-arena-fps
description: Build a Doom-style 2.5D shooter in a browser tab where every texture, mesh and sound is generated at runtime from a seed string — sector maps, three weapons, two enemy types, no images, no models, no audio files, no build step.
metadata:
  title: "Hellgate"
---

# Hellgate — a procedural 2.5D arena FPS with zero external assets

A complete little game and a reference for how far Three.js gets you without loading a single
image, model or audio file. Every texture is painted onto a `<canvas>` at boot, every enemy is a
compound of boxes and cones, every sound is a WebAudio oscillator or noise burst, and the level is
a 40×40 grid of sectors generated from whatever seed string you type.

## When to use

- A game has to ship as one file with no asset pipeline, and "no assets" is a hard rule rather than an aspiration.
- You want a 2.5D look (Doom, Wolfenstein) without a level editor: sectors and a seed instead of hand-built geometry.
- The demo must run from `file://` or Pages with no build step.

## Method

1. Generate the map from a **seed string**, not a random number, so the same string always rebuilds the same arena and a bug is reproducible by sharing the seed.
2. Build geometry from a sector grid; keep walls axis-aligned and let the renderer handle the rest — a 2.5D arena does not need real 3D modelling.
3. Paint every texture procedurally into an offscreen canvas at boot (brick, metal, blood), then reuse those canvases as materials.
4. Compose enemies from primitives (boxes, cones) with a shared hitbox, so collision and rendering stay independent of the model.
5. Synthesise audio at runtime: an oscillator for the shot, a noise burst for the impact. Nothing to download, nothing to license.
6. Keep the roadmap in `ENHANCEMENTS.md` and the architecture notes in `documentation/architecture.md` — the "no assets" rule is documented there, which is what makes it enforceable in review.

## Key files / entry points

- `play/` — the game page.
- `documentation/architecture.md` — including the `#no-assets` section the badge links to.
- `ENHANCEMENTS.md` — the ordered roadmap (63 items at the time of writing).
- `assets/` — banner and screenshot only; these are documentation, not game content.

## Gotchas

- **"No external assets" has to mean documentation too.** The only files in `assets/` are the banner and the screenshot; the moment a font or a sprite lands there the claim is false.
- A seed string is not a seed number: hash the string yourself so a typo produces a different arena rather than the same one.
- Canvas textures are cheap to make and expensive to make *per frame* — paint once at boot, reuse the canvas.

## Source projects

- [Hellgate](https://github.com/drsamonline/Hellgate)
