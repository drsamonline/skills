---
name: text-browser-with-machine-output
description: Fork a text browser into two jobs: reading without distraction, and turning pages into deterministic markdown or JSON for scripts and models — with a size tier of the browser family that fits in 5-8 MB.
metadata:
  title: "Volumen"
---

# Volumen — the web as text, with deterministic dumps

Volumen is a fork of Lynx, kept small, rebuilt around the two jobs a text browser is uniquely good
at: reading without distraction, and turning the web into data a program can use. It is tier 3 of
the Aetheris browser family — the text and automation tier, 5-8 MB where the full browser is 200 MB+.

## When to use

- A page has to become **structured text** for a script or a model: headings, links, lists and tables intact.
- The output has to be *deterministic* — the same page produces the same dump, so a diff means the page changed.
- The machine is small, or the link is slow: the rendering model was designed for 9600 baud.

## Method

1. Fork at a **pinned commit** and record it (`Lynx at 7f67078`); an unpinned fork is a different program every month.
2. Keep the reading model from Lynx — text at the speed of reading, no images, no layout — and resist modernising it.
3. Add one switch for machine output: `--dump --format=json|markdown|reader`, with headings, links, lists and tables preserved in all three.
4. Make the dump deterministic: stable ordering, no timestamps, no locale-dependent formatting, so two runs can be diffed.
5. Place the product in the family explicitly (`FAMILY.md`, tiers T0-T3 with size budgets) so nobody wonders why this one has no images.

## Key files / entry points

- `FAMILY.md` — the four tiers and their size budgets.
- `--dump --format=` — the machine interface (json, markdown, reader).
- The fork point: Lynx commit `7f67078`.

## Gotchas

- A dump format is an API: adding a field is fine, reordering headings is a breaking change for every consumer.
- Text browsers follow the page's own semantics; a site that renders everything in `<div>`s dumps as one blob and no amount of formatting fixes it.
- "Small" is a budget, not a slogan — the tier table is what stops feature creep from doubling the binary.

## Source projects

- [volumen](https://github.com/drsamonline/volumen)
