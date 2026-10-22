---
name: Ambient Sound Studio
description: A private, offline ambient sound mixer in a single HTML file: 25 synthesised layers, 36 presets, EN/HI/GU, WAV and Opus export, installable PWA.
---

# Ambient Sound Studio

Ambient Sound Studio is a private, offline ambient sound mixer that lives in a single HTML file. Layer rain, thunder, fire, café murmur, ocean and wind chimes across 25 synthesised layers and 36 presets, then export the mix as WAV or Opus. English/Hindi/Gujarati, installable PWA, no tracking.

## When to use

- You are building a Web Audio synthesis app with no samples.
- You need client-side WAV/Opus export of a live audio graph.
- You want a single-file PWA with a trilingual UI.

## Method

1. Keep everything in one HTML file (inline CSS/JS, inline SVG); no dependencies, no build step.
2. Synthesise all 25 layers with the Web Audio API (noise + filters + modulation) rather than loading samples.
3. Offer 36 presets and per-layer volume/pan controls; mix live.
4. Export the mix to WAV (encode the rendered buffer) and Opus (via `MediaRecorder`/`AudioEncoder` where available).
5. Provide the trilingual UI (English / Hindi / Gujarati).
6. Make it an installable PWA (`docs/play/manifest.json`, `sw.js`); publish at `docs/play/` and a landing page at `docs/index.html`; build EXE + APK with `.github/workflows/build-apps.yml`.
7. Licence: personal use only; commercial use needs a licence.

## Key files / entry points

- `docs/play/index.html` — the studio; `docs/play/manifest.json`, `docs/play/sw.js`.
- `docs/index.html` — landing page; `assets/banner.svg`, screenshots; `docs/ARCHITECTURE.md`, `docs/BUILD.md`.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Web Audio needs a user gesture to start; the play button provides it.
- Offline rendering for export is CPU-heavy — render in chunks or off the main thread.
- Opus export is not available in every browser; fall back to WAV and say so.
- Keep it sample-free so the single file stays self-contained and offline.

## Source projects

- [ambient-sound-studio](https://github.com/drsamonline/ambient-sound-studio) — v1.5, personal-use licence, single HTML file.

