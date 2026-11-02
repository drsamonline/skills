---
name: base-bench
description: Number bases, units and timezones on one page with the arithmetic shown at every step, so the answer can be checked on paper — offline, no accounts.
metadata:
  title: "Base Bench — converters with the working shown"
---

# Base Bench — converters with the working shown

A converter you cannot check is a converter you have to trust. Base Bench shows the arithmetic at every step: the division chain for a base conversion, the conversion factor for a unit, the offset for a timezone. The point of the app is the *evidence line*, not the result box.

## When to use

- You are writing a calculator or converter whose answers someone might have to defend.
- You need unit and timezone conversion with no network and no library.
- You want a single-page app where the working is part of the data model.

## Method

1. Model each conversion as a function that returns both the result **and the steps** that produced it; render the steps, never re-derive them in the view.
2. Cover the three families in one page — number bases (`docs/play/basebench.js`), units, and timezones — with a shared result/steps shape.
3. Use the vendored `web-kit.js` for storage, i18n and export, and `export-kit.js` for getting a table off the device.
4. Test the maths with `test-node.js` — a converter test should assert the steps, not only the number.
5. Generate badges with `tools/badges.py`, keep `release-notes.md` per release, and release via `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/basebench.js` — the conversion and step model.
- `docs/play/web-kit.js`, `docs/play/export-kit.js` — vendored kits.
- `test-node.js` — the maths tests; `tools/badges.py` — badges.

## Gotchas

- Timezone offsets are not constants — historic and DST rules make a table wrong eventually; prefer `Intl` where the platform has it.
- Floating point makes "the working" wrong if you print raw binary artefacts; round for display, compute at full precision.
- A step model that is generated separately from the result will disagree with it; return both from one function.
- Unit systems that share a name (US vs imperial gallon) need the system in the label, not just the unit.

## Source projects

- [base-bench](https://github.com/drsamonline/base-bench) — the result-plus-steps model across bases, units and timezones.
