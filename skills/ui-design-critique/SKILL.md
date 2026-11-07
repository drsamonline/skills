---
name: ui-design-critique
description: "Critique a UI screenshot, mockup or design against Apple's Human Interface Guidelines and UX writing principles. Use whenever a screenshot or design of an interface is shared — desktop, web or mobile — even if feedback was not explicitly requested. Default output is a short, well-formed quick read; a full section breakdown only when asked."
license: "per source — see references/*/LICENSE"
metadata:
  title: "UI design critique (Apple HIG and UX writing)"
  category: "frontend-ui"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "ui-design-critique"
---

# UI design critique (Apple HIG and UX writing)

A critique is only useful if it is specific and principled: name the principle, name the element, say what to change. The default deliverable is short on purpose — a designer should learn *why* something is weak in one line, not after a paragraph.

## When to use

- A screenshot, mockup or design file of an interface is shared, with or without a question.
- A design needs a pre-ship review or a second opinion.
- Copy inside an interface needs a UX-writing pass.

## Method

1. Read the screen before judging it: state platform, purpose and context on one line. A critique that misreads purpose is worse than no critique.
2. Pick the mode: quick read by default, deep only when the user asks for a full breakdown or 'go further'.
3. Check against the house design system when the screen comes from it, and say so once when it does not — do not force token names onto an outside design.
4. Write the quick read: hard cap 120 words, 6–10 bullets, no overview paragraph. Every bullet names its principle (clarity, deference, Gestalt proximity, Fitts's law, consistency, PACE) and its element.
5. Praise as specifically as you criticise; generic filler ('looks clean!') is worse than silence.
6. In deep mode, work the sections in order — first impression, layout and hierarchy, typography, colour and contrast including accessibility, components and interaction patterns, copywriting, psychology (cognitive load, affordance, trust, friction) — each as 2–4 one-sentence bullets.
7. Close with a verdict: fix these first, in order.
8. Compare platforms where it matters: pointer versus touch (about 44×44pt), and never hide a critical affordance behind hover.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`ui-design-critique`](references/ui-design-critique/) | The critique protocol: read-then-judge, quick vs deep mode, the section rubric, HIG and UX-writing checks, verdict format. |

## Key files / entry points

- `references/ui-design-critique/` — modes, the section rubric, HIG checks and UX-writing rules.

## Gotchas

- If you cannot name the principle behind a point, drop the point.
- Do not exceed 120 words in quick mode — the limit is the product.
- Low-contrast text on bright backgrounds is the most common real defect; check it numerically.
- A critique that lists ten equal-weight problems gives the reader no order of work.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `ui-design-critique` — no licence file shipped with the source
