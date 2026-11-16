---
name: tokens-kit
description: A design token set as data: 121 colour names and 187 values per mode, a 19-field size scale, three elevations with their rings, WCAG contrast and premultiplied mixing — plus the springs, easings and transition presets absorbed from motion-kit on 2026-11-12. Opt-in only: importing it touches no element, no document and no storage.
metadata:
  title: "Tokens kit — the design tokens, and their motion"
---

# Tokens kit — the design tokens, and their motion

The token set as data rather than as CSS: `T.light` / `T.dark` maps, a size scale, three
elevations, contrast maths and the motion presets. It absorbed `motion-kit` on 2026-11-12 —
a token set without its motion is half a design system — so the springs and easings live here
as `T.motion.*`.

## When to use

- You need a colour, size or elevation value in JavaScript, not in a stylesheet.
- You are mixing a translucent token into an opaque one and need the result to match the source palette.
- You must prove a text/background pair is readable, or emit the tokens as CSS custom properties.
- You need an easing curve, a spring's step response or a settle time for a transition.

## Method

1. `require("./tokens-kit.js")` in Node, or use `window.Tokens` in a page.
2. Read tokens directly: `T.light.BgContainer`, `T.dark.Text`, and the nine-step palettes.
3. Mix with `T.mix(a, b, t)` — a premultiplied port of the source's `theme.Mix`, so a translucent token mixed into an opaque one does not darken it.
4. Check with `T.contrast(a, b)` — WCAG relative luminance, compositing a translucent colour over a background first.
5. Take an elevation with `T.shadow("modal" | "popover" | "tooltip", mode)`; the ring is included.
6. Emit the whole set with `T.cssVars(mode)` (209 variables) and write it wherever you choose — `T.apply(el, mode)` is the only function that writes to a node, and it writes to exactly the element you hand it.
7. Animate with `T.motion.*`: the bezier easing, the spring step response and the settle-time helper.
8. Verify with `node test-node.js` — 55 assertions, including that the kit never touches `document`, `window` or storage.

## Key files / entry points

- `tokens-kit.js` — the tokens, `mix`, `contrast`, `shadow`, `cssVars`, `apply` and `T.motion.*`.
- `tokens.source.json` — the generated token data.
- `scripts/gen-tokens.js` — the generator; the values come from lobe-mygo's own token source so they cannot drift from it.
- `docs/API.md`, `test-node.js`, `tools/check-claims.js`, `VERSION`.

## Gotchas

- **It changes nothing on its own.** No auto-apply, no stylesheet injection — and the tests assert the source contains no `document.`, no `window.` and no auto-apply. A lint fix that adds either breaks the suite.
- **Adopting the palette is a per-app decision.** The apps keep their own `design.css`; this kit makes the tokens available, it does not rebrand the fleet.
- **The values are generated.** Edit `tokens.source.json` and re-run `scripts/gen-tokens.js`; hand-editing `tokens-kit.js` is overwritten on the next generation.
- **`contrast` needs an opaque colour.** A ratio against a translucent token means nothing until it is composited over a background — which is why the kit does that first.
- **`motion-kit` no longer exists as a separate adoption.** It was absorbed here; a vendored `motion-kit.js` is a different, older file.

## Source projects

- [tokens-kit](https://github.com/drsamonline/tokens-kit) — the kit, its generator and tests.
- [sui](https://github.com/drsamonline/sui) — a vendored copy of the token set.
