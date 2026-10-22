---
name: Dance Fight — rhythm fighting game
description: A single-file browser rhythm game where every fight move is a dance move: the track's beat is analysed up front into an offline beat grid, and on-beat hits score PERFECT for 60% extra damage.
---

# Dance Fight — rhythm fighting game

Dance Fight is a single-file browser rhythm game: load your own track, the beat is analysed up front into an offline beat grid, the arena pulses on the beat, and every attack is a dance move — land it in time and it becomes a PERFECT hit worth 60% extra damage. No dependencies, no build step, mobile touch-ready.

## When to use

- You need an offline beat-detection / beat-grid approach for a music-driven game.
- You want a single-file game that loads a user's own audio file.
- You want a rhythm mechanic tied to combat scoring.

## Method

1. Let the player load a local audio file; decode it and analyse the beat **up front** into a beat grid (offline analysis, not live FFT at play time).
2. Drive the arena pulse and hit windows from that grid so gameplay stays in sync even on modest devices.
3. Score attacks against the grid: on-beat = PERFECT (+60% damage), with graded falloff off-beat.
4. Keep everything in one HTML file (Web Audio + canvas), no dependencies, no build step; touch controls for mobile.
5. Publish a play copy at `docs/play/index.html` and a landing page at `docs/index.html`.
6. Build the portable EXE + APK with `.github/workflows/build-apps.yml`.

## Key files / entry points

- `index.html` — the game (root) and `docs/play/index.html` (published copy).
- `docs/index.html` — landing page; `screenshot.jpg`.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Pre-analysing the beat is what keeps sync reliable; live analysis drifts on slow machines.
- Audio needs a user gesture to start — the 'load a track' flow provides it.
- `file://` can block loading a local audio file in some browsers; Pages over https is the reliable path.

## Source projects

- [dance-fight](https://github.com/drsamonline/dance-fight) — MIT, single HTML file.

