---
name: form-kit
description: The form controls every app in this fleet hand-rolls — inputs, selects, a date picker, OTP boxes, uploads, checkboxes, switches, sliders, rating, toggles, colour swatches — behind one API (`wrap`, `value()`, `set()`, `on()`) and one validation pass, in a single dependency-free file.
metadata:
  title: "Form kit — 24 controls with one validation pass"
---

# Form kit — 24 controls with one validation pass

Each control returns the same shape — `wrap` (label + control + help + error line), `value()`,
`set()`, `on()` — so a form is a loop rather than 24 special cases, and validation happens once.

## When to use

- An app needs a date picker, OTP boxes, an upload field or a slider and you are about to hand-roll it for the third time.
- You want one validation pass over a mixed set of controls instead of per-field ad-hoc checks.
- You are binding controls to a signal and want two-way updates that do not fire change events in a loop.

## Method

1. `require("./form-kit.js")` in Node, or use `window.Form` in a page.
2. Build a control: `var name = F.input({ label: "Name", required: true })` and append `name.wrap` — the label, control, help text and error line are already assembled.
3. Read with `name.value()`, write with `name.set(v)` (which does not fire a change event), listen with `name.on("change", fn)`.
4. Bind to state with `F.bind(control, signal)` for two-way updates with a `ui-kit` signal.
5. Pick from the families: **text** (`input`, `textarea`, `password`, `search`, `number`, `date`, `datePicker`), **choice** (`select`, `autocomplete`, `checkbox`, `switch`, `radioGroup`, `slider`, `rate`, `toggleGroup`, `otp`), and the wider set (`calendar` — Monday-first, ISO dates — `upload`, `colorSwatches`).
6. Verify with `node test-node.js` — 108 assertions against a small DOM written inside the test file: structure and ARIA, value round-trips, change events, the calendar's Monday-first grid and year wrap, OTP focus flow, autocomplete filtering, every validation rule and binding in both directions.

## Key files / entry points

- `form-kit.js` — every control, the validation pass and `F.bind`.
- `test-node.js` — 108 assertions and the small DOM they run against.
- `docs/API.md`, `docs/index.html`, `VERSION`.

## Gotchas

- **`set()` is silent by design.** It writes without firing `change`; a caller that relies on the event to recompute state must call its own update after `set()`.
- **`number` reads as a number or `null`.** An empty numeric field is `null`, not `0` and not `""` — validation that expects a string will mis-handle it.
- **`calendar` is Monday-first with ISO dates.** A Sunday-first locale is not a flag; the grid is fixed.
- **Deferred on purpose:** lobe's `Select` with async search and its `Upload` with a progress stream are not here — no app in the fleet has asked for either.
- **Consumers: none by design.** No app was modified. The measured case: date pickers appear in 18 files across 5 sampled apps, checkboxes and switches in 14 files across 5, sliders in 2. Adoption is one app at a time, by the owner.

## Source projects

- [form-kit](https://github.com/drsamonline/form-kit) — the controls, the validation pass and its 108 assertions.
