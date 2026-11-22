---
name: browser-beat-workstation
description: Build a browser beat workstation where every loop is synthesised on device at boot: a hardware-style pad grid, a canvas arrangement, a mixer with sends and master FX, automation and scenes, and WAV/stem export — one 192 KB file, zero dependencies.
metadata:
  title: "NEONBOOM"
---

# NEONBOOM — a beat workstation in a browser tab

A beat workstation that lives in a browser tab. Twenty-seven loops are synthesised on the device at
boot — nothing to download, no account, no upload, no server — with a hardware-style pad grid, a
canvas arrangement, a mixer with sends and master FX, automation, scenes, and WAV/stem export.
192 KB single file, zero dependencies, feature-frozen at 2.4.0.

## When to use

- The instrument has to work offline and ship as one file, so samples are out and synthesis is in.
- The interface should feel like hardware: pads, a mixer strip, sends — not a form.
- The output must leave the app as audio (WAV, stems), because a browser toy that cannot export is a demo.

## Method

1. Synthesise every loop at boot into `AudioBuffer`s; a 27-loop kit that costs no bytes is the whole trick.
2. Lay out the pads as a grid with fixed hit areas and keyboard equivalents, so the app is playable with a mouse, a finger or a keyboard.
3. Separate **pattern** (steps per track) from **arrangement** (scenes over time) — the canvas shows the second, the grid edits the first.
4. Build a mixer with per-track gain, sends to a shared reverb/delay, and a master chain; automation writes to the same parameters the UI moves.
5. Export offline: render the arrangement through an `OfflineAudioContext` and encode to WAV, per stem as well as the mix.
6. Freeze the feature set when it is done (2.4.0) — a beat machine that keeps growing stops being a beat machine.

## Key files / entry points

- The synth/boot path that builds the loop kit.
- The pad grid and the canvas arrangement.
- The mixer and master chain.
- The WAV/stem export path.

## Gotchas

- `OfflineAudioContext` renders faster than real time but not instantly: a long arrangement needs a progress state, not a frozen tab.
- A send that shares one reverb between tracks makes stems wrong — the stem export must include its own effects or exclude them explicitly.
- Automation recorded against UI parameter values breaks when a control's range changes; store normalised values.

## Source projects

- [neonboom](https://github.com/drsamonline/neonboom)
