---
name: Clinical case tracking
description: Record a case as sections, dated symptoms with severity, and follow-ups - with a timeline, a summary and JSON round-trip.
---

# Clinical case tracking

## When to use

Record a case as sections, dated symptoms with severity, and follow-ups - with a timeline, a summary and JSON round-trip.

## Method

Extract the capability into a single, zero-dependency file (`case.js`-style),
verify it headless in Node, and let the apps delegate to it instead of repeating it.

## Key files

- the kit's main `.js` file — the API
- `test-node.js` — the verified behaviour (run it before and after any change)

## Gotchas

- Keep the app's own public API stable while swapping in the kit, so its tests
  still pass — that is the proof the refactor is correct.
- One file, zero dependencies, MIT; register it and give it a landing page.

## Source projects

skin-case-tracker, HMS, case-kit
