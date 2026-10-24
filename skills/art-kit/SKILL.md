---
name: art-kit
description: The art primitives for offline apps — an indexed palette, a pixel canvas with nearest-neighbour scaling, draw ops, a delta undo stack, dithering (Bayer + Floyd-Steinberg), median-cut quantisation, sprite sheets, the isometric mapping and a sketch loop. Zero dependencies, single file, no assets.
metadata:
  title: "art-kit — art primitives from scratch"
---

# art-kit — art primitives from scratch

## When to use

Make a sprite, a tile, a posterised photo or a dithered image without an image
editor or an asset file — and drive a live generative sketch. Reach for this
instead of hand-rolling pixel art in each game.

## Method

An **indexed** palette is the key: the canvas stores one palette index per pixel,
so `swap`/`cycle` restyle a whole image and `quantize` reduces a photo to N
colours. Draw ops write through `canvas.onPaint`, which is how `history` records
**deltas, not whole frames**. Scale with `Art.scale` (nearest-neighbour — never
smooth). Compose with `game-kit` for the loop and the sim.

## Key files

- `art-kit.js` — the API: `palette`, `canvas`, `scale`, `history`, `dither`,
  `quantize`, `spriteSheet`/`sliceSprite`, `iso`, `sketch`
- `test-node.js` — 31 verified cases (run it before and after any change)

## Gotchas

- **Never smooth on scale** — nearest-neighbour is the point; smoothing destroys pixel art.
- **No copied code.** Everything is reimplemented from published technique; the
  reference projects are permissive and are named in comments only.
- One file, zero dependencies, UMD (`module.exports` / `Art`), MIT, no assets shipped.

## Source projects

art-kit, game-kit
