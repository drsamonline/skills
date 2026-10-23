---
name: blinkcode-ai-spectracode
description: Optical file transfer as a vanilla-JS PWA: a file becomes a 'File DNA' container painted as SpectraCode colour matrices, decoded by camera with marker detection, homography and Reed-Solomon error correction.
metadata:
  title: "BlinkCode AI — SpectraCode optical transfer"
---

# BlinkCode AI — SpectraCode optical transfer

BlinkCode AI compresses a file into a compact 'File DNA' container, paints it as SpectraCode colour matrices (36 reference colours, bullseye markers, a calibration strip), and recovers it by pointing a camera at the sender's screen. Small payloads fit one static frame; larger ones loop as numbered frames the receiver collects. Vanilla JS, no build step, workers for model/compression/decode, and a one-time model download cached for full offline use.

## When to use

- You want a high-density optical transfer (colour matrices rather than QR).
- You need a reference for arithmetic coding, Reed-Solomon and homography-based decoding in the browser.
- You want a no-build-step PWA with web workers and an offline model bundle.

## Method

1. Run it with `npm run serve` (localhost:8080), `npm test` (codec + optical loopback), `npm run build:model` (rebuild the downloadable model bundle).
2. Encode: order-1 context model + arithmetic coder for lossless general compression (`src/lib/arith.js`, `codec.js`, `format.js`), and a perceptual image mode (64-value latent, 8-bit quantised) for lossy extremes (`image-codec.js`).
3. Render: pack symbols into SpectraCode grids (`spectracode.js`) using a 36-colour palette (`palette.js`) with bullseye markers, a calibration strip and two densities (120×80 / 60×40) signalled by a density patch.
4. Protect: Reed-Solomon `RS(255,223)` (`rs.js`) corrects 16 bytes per block; a stream layer (`stream.js`) carries a frame header, CRC-32 and out-of-order collection.
5. Decode: marker detection → homography (`geometry.js`) → 3×4 colour correction → cell classification → payload bytes (`spectra-decode.js`); continuous camera auto-scan with wake lock.
6. Move heavy work into workers (`src/workers/`): model loading, compression, decompression and optical decode.
7. Cache the one-time model download in Cache Storage + IndexedDB (`storage.js`) so the app is fully offline afterwards; precache the shell with `sw.js`.
8. Keep a loopback self-test that pushes every rendered frame back through the real optical decoder, and validate in simulation (perspective tilt, colour cast, vignetting).

## Key files / entry points

- `src/lib/arith.js`, `codec.js`, `format.js`, `image-codec.js`, `geometry.js`, `palette.js`, `rs.js`, `spectracode.js`, `spectra-decode.js`, `storage.js`, `stream.js`, `surface.js`.
- `src/workers/*` — model loader, compression, decompression, optical decode.
- `src/models/ucg-v1.bin` — the downloadable model bundle; `tools/build-model.js`, `tools/serve.js`.
- `docs/play/` (published app), `docs/index.html` (landing page).
- `tests/` — codec + end-to-end optical loopback.

## Gotchas

- Be honest about limits: one frame holds 5,111 payload bytes (1,097 in robust density); throughput ≈ 5 KB × frame rate (~15 KB/s at 3 FPS).
- Lossless 1000:1 is impossible; measured ratios are ~2–4× on text and ~1× on already-compressed data. Extreme ratios exist only in the lossy perceptual mode.
- The 'neural' model is a mock with a real interface (order-1 byte statistics + DCT quantiser scales, ~129 KB) — the bundle format and offline caching are production-shaped, the weights are not.
- TensorFlow.js is intentionally not bundled: no runtime CDN dependency is allowed, and a placeholder network would add megabytes without helping.
- Camera decoding is validated in simulation, not against physical optics — real glare/blur may need per-cell voting and multi-frame averaging.

## Source projects

- [blinkcode-ai](https://github.com/drsamonline/blinkcode-ai) — source-available (personal/academic free, commercial by permission), vanilla JS, no build step.

