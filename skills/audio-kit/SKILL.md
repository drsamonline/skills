---
name: audio-kit
description: Synthesis, theory, patterns and notation for offline apps — a pure ADSR envelope, oscillator voices, filters, noise and a mixer; notes, scales and chords; a pattern sequencer; a staff layout; byte sonification; and honest mastering helpers. Zero dependencies, single file, no audio assets.
metadata:
  title: "audio-kit — sound from code, not files"
---

# audio-kit — sound from code, not files

## When to use

Generate sound with no asset file: game music and effects, an ambient layer, a
practising tool, or a sonified file. Reach for this instead of shipping audio.

## Method

**Game music is patterns, not files.** A pattern is a few KB of data and plays
through WebAudio; an audio file is megabytes. Use `seq.pattern` + `seq.play`, and
`music` for the theory. The **envelope maths and the scheduling are pure**, so they
test headless — only the node-building needs an audio context, and only on a user
gesture.

## Key files

- `audio-kit.js` — the API: `music`, `synth` (adsr/voice/noise/mixer), `seq`,
  `notation`, `sonify`, `master`
- `test-node.js` — 42 verified cases (run it before and after any change)

## Gotchas

- **No autoplay.** Build every node from a context created on a user gesture.
- **No copied code.** References (the tracker tradition, Orca, MuseScore,
  matchering, binary-synth) are named in comments only; the copyleft ones are
  technique only.
- The mastering helpers are a **matching aid, not an engineer** — say so in any app
  that uses them.
- One file, zero dependencies, UMD (`module.exports` / `AudioKit`), MIT.

## Source projects

audio-kit, game-kit, ambient-sound-studio
