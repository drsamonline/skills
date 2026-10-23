---
name: repertory-kit-repertorisation
description: Score remedies by weighted rubric grades - the repertorisation a homeopath actually does - with must-have and exclude filters.
metadata:
  title: "Homeopathic repertorisation (rubric grading)"
---

# Homeopathic repertorisation (rubric grading)

## When to use

Score remedies by weighted rubric grades - the repertorisation a homeopath actually does - with must-have and exclude filters.

## Method

Extract the capability into a single, zero-dependency file (`repertory.js`-style),
verify it headless in Node, and let the apps delegate to it instead of repeating it.

## Key files

- the kit's main `.js` file — the API
- `test-node.js` — the verified behaviour (run it before and after any change)

## Gotchas

- Keep the app's own public API stable while swapping in the kit, so its tests
  still pass — that is the proof the refactor is correct.
- One file, zero dependencies, MIT; register it and give it a landing page.

## Source projects

kent-repertory-explorer, boericke-repertory, remedy-relationship-explorer, repertory-kit
