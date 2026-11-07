---
name: frontend-engineering
description: "Build a modern web front end properly: pick the stack and scaffold it, declare a design system and design tokens before writing UI, keep the visual craft high, and hold the performance budget. Use for a new web app or dashboard, a design-system or token pass, a React/shadcn/Tailwind build, a single-file interactive playground, or a 'why is my site slow' audit. Not for back-end work or non-visual coding."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Frontend engineering (design system, scaffold, performance)"
  category: "frontend-ui"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "web-design-engineer, tailwind-design-system, spark-app-template, performance, playground"
---

# Frontend engineering (design system, scaffold, performance)

Four jobs that run in a fixed order: **scaffold** the stack, **declare** the design system, **build** the interface, **measure** the result. Skipping the declaration step is what makes generated UI look generic; skipping the measurement step is what makes it slow. The stack guidance is opinionated on purpose — defaults are cheaper to review than choices.

## When to use

- A new web app, dashboard, prototype or marketing page is to be built.
- An existing interface needs a design system, tokens, or standardised components.
- The user asks for a single-file interactive explorer or playground.
- A page loads slowly and a performance audit with a budget is wanted.

## Method

1. Verify facts before designing around them: if the request names a product, SDK, brand or version you are not certain of, search first. Never assert an unverified capability.
2. Gather design context before choosing anything — existing brand assets, an existing UI to match, references the user likes. Never start from thin air, and never substitute CSS silhouettes or hand-drawn SVG for real product imagery.
3. Calibrate five dials explicitly (density, expressiveness, contrast, motion, ornament) and, when the brief is genuinely vague, offer three differentiated directions from different schools rather than asking ten questions.
4. Scaffold in dependency order: create the app, configure path aliases **before** initialising the component library, install the component library **before** writing components that import it. This order exists because the reverse fails with TypeScript and install errors.
5. Declare the design system before writing UI: token hierarchy (primitive → semantic → component), type scale, spacing scale, radius, elevation, motion durations. Tokens are named for their role, not their value.
6. Build the interface against the tokens only — no ad-hoc hex values. Show a v0 draft early when the direction is uncertain, then complete the build.
7. For an interactive playground, keep it one self-contained file: every control change re-renders the preview immediately, and the page emits a copyable prompt or config as its output.
8. Verify in the browser (render, keyboard, small viewport) before delivery, and critique your own work against the design bar.
9. Then hold the performance budget: measure with a trace, keep the critical rendering path short, defer and split JavaScript, serve modern image formats at the right sizes, prioritise the LCP image, self-host and preload fonts with `font-display: swap`, and set cache headers by asset class (immutable for hashed assets, no-cache for HTML).
10. Fix a budget breach by removing work, not by raising the budget.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`web-design-engineer`](references/web-design-engineer/) | The design-engineer method: verify facts, gather context, five dials, declare the system, draft early, verify, self-critique. |
| [`tailwind-design-system`](references/tailwind-design-system/) | Tailwind v4 design tokens, component architecture and responsive patterns. |
| [`spark-app-template`](references/spark-app-template/) | The opinionated stack, the install order that avoids build errors, project structure and four stack variants. |
| [`performance`](references/performance/) | The performance budget method: critical path, JS, images, fonts, caching, and how to measure. |
| [`playground`](references/playground/) | The self-contained single-file interactive explorer pattern with instant preview and prompt output. |

## Key files / entry points

- `references/web-design-engineer/` — the design-engineer workflow: fact check, context gathering, five dials, design-system declaration, verification, self-critique.
- `references/tailwind-design-system/` — Tailwind v4 token hierarchy, component architecture, responsive patterns.
- `references/spark-app-template/` — the opinionated stack, install order, project structure and stack variants.
- `references/performance/` — the performance method: budget, critical path, JS, images, fonts, caching.
- `references/playground/` — the single-file interactive explorer pattern.

## Gotchas

- `shadcn init` before path aliases are configured fails validation; components imported before they are installed fail the build.
- Overused fonts (Inter, Roboto, Arial, Space Grotesk) are the default tell of generated UI.
- Embedding a design system after the build starts means two systems in one page.
- A performance number without a budget is an opinion — set the budget from the target device and network.
- A playground whose preview lags one change behind feels broken.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `web-design-engineer` — no licence file shipped with the source
- `tailwind-design-system` — no licence file shipped with the source
- `spark-app-template` — no licence file shipped with the source
- `performance` — no licence file shipped with the source
- `playground` — no licence file shipped with the source
