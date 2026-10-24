---
name: ui-kit
description: A reactive UI layer small enough for a single file — signals, computed, reactive effects, hyperscript, a keyed list, events, a hash router and two-way form binding. Zero runtime dependencies, no build step.
metadata:
  title: "ui-kit — reactive UI with no build step"
---

# ui-kit — reactive UI with no build step

## When to use

Build a reactive view in a single-file offline app with **no bundler and no
node_modules** — signals, derived values, declarative DOM and a keyed list. Reach for
this instead of hand-rolling DOM updates in every app.

## Method

A **signal** is a function you call to read; calling it inside an **effect** or a
**computed** records the dependency, so a change re-runs exactly what read it. Render
with `h(...)`, bind text with `text(sig)`, and render lists with `list(items, key,
render)` — the **same node is reused for the same key**, so a reorder does not flicker.
Update list items **immutably** (map to new objects) so a changed item re-renders.

## Key files

- `ui-kit.js` — the API: `signal`, `computed`, `effect`, `h`, `text`, `list`, `on`,
  `bus`, `router`, `bind`
- `test-node.js` — 31 core cases; `test-todomvc.js` — the acceptance run
- `examples/todomvc.js` — TodoMVC built on the kit, the proof it works

## Gotchas

- **No build step.** The whole library is one file; drop it in a `<script>` and go.
- **No copied code** and no vendored framework — the shape is after hyperapp, Vue 3
  and Mithril, named in comments only.
- List items must be **replaced immutably**; a mutated object in place will not
  re-render.
- `jsdom` is a dev dependency for the tests only; the kit has none.

## Source projects

ui-kit, ambient-sound-studio, web-kit
