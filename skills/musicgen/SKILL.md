---
name: musicgen
description: A pocket generative composer that writes, synthesises, masters and exports a finished track in the browser from a seed — no server, no samples, with LUFS metering and a determinism lint.
metadata:
  title: "MusicGen — offline generative composer"
---

# MusicGen — offline generative composer

One tap produces a finished-sounding track — harmony, melody, drums, mix and master — from six presets and a twelve-character seed. Everything is synthesised at runtime: there are no samples and no network calls. The audio engine lives in `app/src/audio/`, one module per concern, and the project treats *determinism* as a testable property.

## When to use

- You need generated music with no assets, in the browser, offline.
- You are building a Web Audio graph serious enough to need mastering, metering and a render path.
- You want a seed → identical output guarantee you can test.

## Method

1. Split the engine by concern under `app/src/audio/`: `engine.js` and `graph.js` for the context and routing, `instruments.js`, `drums.js`, `textures.js` for voices, `scheduler.js` for timing, `fx.js`, `render.js`, `player.js`, `transitions.js`, `lufs.js` and `mastering.js` for the mix and loudness.
2. Run the clock in an `AudioWorklet` (`app/src/audio/worklets/clock.js`) rather than on `setTimeout`, so scheduling survives a busy main thread.
3. Derive every musical decision from the seed through one PRNG; `npm run lint` (`scripts/lint-determinism.mjs`) fails the build if a module reaches for `Math.random()` or `Date.now()`.
4. Master to a loudness target with `lufs.js` + `mastering.js` rather than by ear, and check the budget with `npm run budget` (`scripts/budget.mjs`).
5. Test at three levels: unit (`npm test` → `tests/unit/run.js`), browser (`npm run test:browser`), and measurement (`npm run spectral`, `npm run visual`).
6. Ship `app/` as the installable PWA with `app/manifest.webmanifest`; `npm start` serves it with `python3 -m http.server`.

## Key files / entry points

- `app/src/audio/` — the whole engine, one file per concern, plus `worklets/clock.js`.
- `app/index.html`, `app/manifest.webmanifest` — the PWA.
- `scripts/lint-determinism.mjs`, `scripts/budget.mjs`, `scripts/spectral.mjs`, `scripts/audit.mjs`.
- `tests/unit/run.js`, `tests/browser/test.mjs`.

## Gotchas

- `Math.random()` anywhere in the musical path destroys seed reproducibility — hence the lint, not a code review.
- Web Audio scheduling on the main thread drifts under load; the worklet clock exists because of that.
- A "no samples" promise is only true if every layer is an oscillator or noise source — adding one buffer breaks it.
- Loudness normalisation after the fact cannot repair a graph that clips earlier in the chain.

## Source projects

- [musicgen](https://github.com/drsamonline/musicgen) — the audio module split, the worklet clock, LUFS mastering and the determinism lint.
