---
name: gsap-web-animation
description: "Animate the DOM and SVG with GSAP: tweens, timelines, easing, stagger, ScrollTrigger-family scrolling, Flip, Draggable, SplitText, SVG drawing and morphing, and plugin registration. Use when the user wants a JavaScript animation library, scroll-driven or timeline animation, split-text reveals, draggable interfaces, or responsive and reduced-motion-aware motion."
license: "per source — see references/*/LICENSE"
metadata:
  title: "GSAP web animation"
  category: "frontend-ui"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "gsap-core, gsap-plugins"
---

# GSAP web animation

Core API for the tweens and timelines; plugins for everything that touches the document, the scroll position, or the SVG geometry. The house rules are the same in both halves: camelCase property names, transform aliases over raw `transform`, timelines over chained delays, and reduced-motion respected.

## When to use

- Motion must be synchronised, interruptible, reversible or driven by scroll.
- A UI needs staggered reveals, split-text animation, SVG draw or morph, drag with inertia.
- The user asks which animation library to use for a DOM/SVG interface.

## Method

1. Decide whether CSS is enough: if the motion is a single, non-interruptible state change, CSS wins. Use GSAP when motion must be sequenced, retargeted mid-flight, reversed, or tied to scroll or drag.
2. Write tweens with camelCase property names and transform aliases (`x`, `y`, `scale`, `rotation`, `xPercent`, `yPercent`); use `autoAlpha` rather than `opacity` when an element should also become non-interactive when hidden.
3. Sequence with timelines rather than chained delays; set `defaults` once per timeline instead of repeating duration and ease.
4. Register every plugin once, at module top level — in React, before the first `useGSAP`, never inside a re-rendering component.
5. Gate responsive and reduced-motion behaviour through `gsap.matchMedia()` with the conditions object; skip the animation (or use `duration: 0`) when reduced motion is requested.
6. For text splitting, split only what you animate, split after fonts load (or set `autoSplit`), keep `aria: 'auto'` so screen readers get the label, and add `smartWrap` when splitting characters only.
7. For SVG, the element must have a visible stroke before `drawSVG` runs, and `morphSVG` needs the start and end shapes; try `type: 'rotational'` when linear morphing kinks.
8. Verify on a slow device and with reduced motion enabled before calling the animation done.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`gsap-core`](references/gsap-core/) | Core API: tweens, easing, stagger, defaults, timelines, matchMedia, accessibility, best practices. |
| [`gsap-plugins`](references/gsap-plugins/) | Plugin reference and registration: scroll, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG, easing plugins, licensing. |

## Key files / entry points

- `references/gsap-core/` — core tween methods, easing, stagger, defaults, matchMedia, official best practices and the 'do not' list.
- `references/gsap-plugins/` — registration, licensing, scroll (ScrollTo, ScrollSmoother), DOM (Flip, Draggable, Inertia, Observer), text (SplitText, ScrambleText), SVG (DrawSVG, MorphSVG, MotionPath), easing plugins.

## Gotchas

- Registering a plugin inside a component that re-renders registers it repeatedly.
- Animating the raw `transform` string loses the alias benefits and composes badly.
- Starting an entrance from `scale(0)` reads as a glitch; start at 0.9–0.97 with opacity.
- Split text before custom fonts load produces wrong line breaks.
- `drawSVG` on an element with no stroke silently draws nothing.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `gsap-core` — no licence file shipped with the source
- `gsap-plugins` — no licence file shipped with the source
