---
name: mood-to-palette-playground
description: Build a colour playground where three mood sliders produce a coordinated four-colour palette, with six harmony schemes, WCAG contrast checks and CSS/JSON/Tailwind/PNG export — private, offline, no network calls.
metadata:
  title: "Mood Mixer"
---

# Mood Mixer — three sliders to a coordinated palette

A private, offline-ready colour playground: move three sliders, get a coordinated four-colour
palette, copy hex values, check WCAG contrast, and export what you like. No account, no analytics,
no network calls — and every feature listed is shipped and tested in headless Chrome.

## When to use

- A user needs a palette *now* and cannot reason about harmony schemes; the sliders carry the intent ("warm, calm, dark") and the maths carries the harmony.
- The palette has to leave the app in a real format: CSS variables, JSON, a Tailwind config, a PNG.
- Accessibility is part of the output, not a separate audit: contrast is checked on the palette you just made.

## Method

1. Map **three moods** (not colours) to a base HSL triple — the sliders are the input, the palette is derived.
2. Apply one of six harmony schemes (complementary, analogous, triadic, split, tetradic, monochrome) to produce four colours from the base.
3. Show every representation at once — HSL, RGB, HSV — because the value a user needs depends on where they will paste it.
4. Check **WCAG contrast** for each foreground/background pair and show the ratio, not a pass/fail badge.
5. Export CSS variables, JSON, a Tailwind snippet and a PNG of the palette; each export is the same data in a different coat.
6. Test the colour maths in a headless browser: harmony and contrast are arithmetic and they break silently.

## Key files / entry points

- The mood→base mapping and the six harmony functions.
- The contrast checker (WCAG ratio per pair).
- The export paths (CSS, JSON, Tailwind, PNG).

## Gotchas

- HSL lightness is not perceptual lightness: two colours at the same L can read as very different weights, so contrast must be computed, never assumed.
- Rounding at export changes the hex; export the rounded value you showed, or the user's pasted palette differs from the screen.
- A "mood" slider that maps to saturation alone produces a muddy palette — hue and lightness both have to move.

## Source projects

- [mood-mixer](https://github.com/drsamonline/mood-mixer)
