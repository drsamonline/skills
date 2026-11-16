---
name: widgets-kit
description: Buttons, tags, avatars, badges, alerts, progress, modals, drawers, toasts, tooltips, popovers, menus, tabs, accordion, pagination, breadcrumbs, steps, skeletons, grids and headers in one dependency-free file — with the behaviours that matter implemented: a real focus trap, focus restoration, Escape and backdrop close, a live region for toasts, and keyed lists that reuse the same node so a re-render keeps focus.
metadata:
  title: "Widgets kit — the component layer for offline apps"
---

# Widgets kit — the component layer for offline apps

The components every app in this fleet hand-rolls, in one file: `W.button`, `W.modal`,
`W.toast`, `W.tabs`, `W.list` and the rest. Zero dependencies, one global (`window.Widgets`) or
a Node export.

## When to use

- An app needs a modal, drawer, toast, tabs, menu, accordion or pagination and you are about to write the third version of it.
- Accessibility is the reason, not a nicety: you need a focus trap, focus restoration, a live region or ARIA roles that are actually wired.
- A list re-renders on every keystroke and you want the focused node to survive.

## Method

1. `require("./widgets-kit.js")` in Node or use `window.Widgets` in a page.
2. Mount a component: `var m = W.modal({ title, body }); m.mount(document.body).open();` — focus is trapped, Escape closes, focus is restored on close.
3. Call `W.toastHost()` once before any `W.toast(msg, { type })`; the host owns the live region.
4. Use `W.list({ items, key, render })` for anything that re-renders — the same node is reused per key, so focus and selection survive.
5. Build from primitives with `W.button`, `W.tag`, `W.avatar`, `W.badge`, `W.progress`, `W.alert`, `W.tabs`, `W.accordion`, `W.pagination`, `W.steps`, `W.skeleton`, `W.grid`, `W.header`.
6. Style with your own CSS; the kit ships structure and behaviour, not a look.
7. Verify with `node test-node.js` — 206 assertions run against a small DOM written inside the test file, so the kit takes the same code paths in Node as in a page.

## Key files / entry points

- `widgets-kit.js` — every component and the `FOCUSABLE` selector the trap uses.
- `test-node.js` — 206 assertions, including the focus trap in both directions and keyed-list reuse across a reorder.
- `docs/API.md`, `docs/index.html`, `VERSION`.

## Gotchas

- **`W.toastHost()` is not optional.** A toast with no host has nowhere to appear and no live region to announce it.
- **A keyed list is the point.** Re-rendering with a new array without a `key` throws away focus and scroll — the component cannot save you from a missing key.
- **Deferred on purpose:** `draggablePanel`, `sideNav`, `guideCard`, `floatingPanel`, `sortableList` and `contextMenu` are not in the kit; the audit recommended holding the drag-and-drop surface until an app needs it.
- **Consumers: none by design.** No app was modified to adopt this kit. The measured case for it: a modal hand-rolled in 74 files across 22 repos, tabs in 6 of 10 sampled apps, toasts in 5, dropdown menus in 4, focus trapping in 7. Adoption is one app at a time, by the owner.

## Source projects

- [widgets-kit](https://github.com/drsamonline/widgets-kit) — the kit, its API and its 206 assertions.
