---
name: search-kit-ranked-search
description: Build an inverted index once and query it with exact, prefix and fuzzy matching, ranked by field weight.
metadata:
  title: "Ranked search over a large corpus"
---

# Ranked search over a large corpus

## When to use

Build an inverted index once and query it with exact, prefix and fuzzy matching, ranked by field weight.

## Method

Extract the capability into a single, zero-dependency file (`search.js`-style),
verify it headless in Node, and let the apps delegate to it instead of repeating it.

## Key files

- the kit's main `.js` file — the API
- `test-node.js` — the verified behaviour (run it before and after any change)

## Gotchas

- Keep the app's own public API stable while swapping in the kit, so its tests
  still pass — that is the proof the refactor is correct.
- One file, zero dependencies, MIT; register it and give it a landing page.

## Source projects

kent-repertory-explorer, open-materia-medica, SmartNotes, search-kit
