---
name: srs-kit-sm2
description: Schedule flashcards with the SM-2 algorithm: ease, interval, reps, lapses, due cards and stats.
metadata:
  title: "Spaced repetition with SM-2"
---

# Spaced repetition with SM-2

## When to use

Schedule flashcards with the SM-2 algorithm: ease, interval, reps, lapses, due cards and stats.

## Method

Extract the capability into a single, zero-dependency file (`srs.js`-style),
verify it headless in Node, and let the apps delegate to it instead of repeating it.

## Key files

- the kit's main `.js` file — the API
- `test-node.js` — the verified behaviour (run it before and after any change)

## Gotchas

- Keep the app's own public API stable while swapping in the kit, so its tests
  still pass — that is the proof the refactor is correct.
- One file, zero dependencies, MIT; register it and give it a landing page.

## Source projects

mnemosyne-companion, unstoppable-mind-companion, srs-kit
