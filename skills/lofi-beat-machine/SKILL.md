---
name: lofi-beat-machine
description: Build a lofi beat machine with six tracks, sixteen steps, nine ambience layers and a live tape chain — everything synthesised on the fly, offline-first, no samples, no account, no server.
metadata:
  title: "Lofi Studio Pro"
---

# Lofi Studio Pro — a sample-free lofi machine with a live tape chain

A lofi beat machine that runs entirely in the browser: six tracks, sixteen steps, nine ambience
layers and a live tape chain — all synthesised on the fly, no samples, no account, no server.

## When to use

- The *sound* is the product (warm, wobbly, tape-saturated) and it has to be generated, not sampled.
- A sequencer has to stay simple enough for one screen: six tracks, sixteen steps, no piano roll.
- Ambience is part of the instrument, not a background loop: rain, vinyl crackle and hum are layers you mix.

## Method

1. Six tracks × sixteen steps is the whole sequencer; resist adding tracks, because the constraint is what makes it usable on a phone.
2. Synthesise each voice (kick, snare, hat, chord, bass, texture) rather than loading samples — it keeps the app small and the sound yours.
3. Put the **tape chain** after the voices: saturation, wow/flutter, a gentle filter and noise. The imperfection is the feature, and it must be live (adjustable while playing), not baked into export.
4. Layer the nine ambience beds under the beat with independent levels.
5. Make it a PWA so the first load is the only load; nothing is fetched again.
6. Keep the landing page separate from the app page — one sells it, one runs it.

## Key files / entry points

- The step sequencer (six tracks × sixteen steps).
- The voice synthesisers.
- The tape chain and the ambience mixer.

## Gotchas

- Wow and flutter drift the timing if applied per-voice; apply the tape stage to the summed bus or the beat stops being a beat.
- A noise bed at a fixed level sounds loud on headphones and silent on a laptop — expose it, do not bake it.
- Saturation before the filter sounds warm; after it, harsh. The order of the chain is the sound.

## Source projects

- [lofi-studio-pro](https://github.com/drsamonline/lofi-studio-pro)
