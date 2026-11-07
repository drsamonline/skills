---
name: html-video-production
description: "Build editable, scene-based HTML videos and render them to MP4 with HyperFrames: GSAP timelines, kinetic typography, data-driven motion graphics, transitions, captions, lower thirds. Use when the video must be reproducible and editable from structured sources (PDF, repo, CSV, deck, design doc, URL, music track), or when the user mentions HyperFrames, GSAP timeline video, cut-the-curve, or a motion template. Not for photoreal generated footage (use ai-video-generation)."
license: "per source — see references/*/LICENSE"
metadata:
  title: "HTML video production (HyperFrames)"
  category: "media-design"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "html-video-production, hyperframes-registry, cut-the-curve, review-animations, video-template-frame-light-leak-cinema"
---

# HTML video production (HyperFrames)

The video is code: a project of scenes, each an HTML document animated by GSAP, rendered headlessly to MP4. That makes it diffable, re-renderable and cheap to restyle, and it means the craft lives in the cut and the type rather than in a generation prompt. The technique catalog below (seams, waterfall entries, nudge curves) is what separates a motion graphic from a slideshow with fades.

## When to use

- The source is structured (a report, a repo, a CSV, a deck, a URL) and the output must be re-renderable when the source changes.
- The video is typographic, diagrammatic or data-driven rather than photoreal.
- A named visual is wanted — CRT scanlines, glitch, film grain, a chart, a map overlay, a 3D camera move — and a ready-made block probably exists.
- The user wants a scene-by-scene edit they can keep adjusting after delivery.

## Method

1. Run the fidelity gate before scaffolding anything: if the request is photoreal, cinematic and generated purely from a creative description with no editable layer, decline and route to native AI video generation. If it needs both an editable layer and generated footage, go hybrid and say so.
2. Decide the route once (editable HTML, native generation, or hybrid) and ask a single question if it is genuinely ambiguous. Never scaffold a project for a request that should have gone to generation.
3. Produce every media asset (voice, music, images, icons) before writing HTML that references it, and hand-write the asset ledger rather than running an upstream resolver.
4. Scaffold the project manually and install the framework with npm. Never run the framework's init or skills-update commands (they overwrite patched skills) and never run the paid cloud renderer.
5. Search the block registry before hand-building any named visual: ~450 blocks are installed as editable source (transitions, overlays, titles, kinetic type, captions, charts, maps, 3D, camera moves). Local search only.
6. Compose the cut from the technique catalog: velocity-matched seams (zoom-through, inverse zoom-through, cut-the-curve, waterfall cut, rack-focus blur-cut) at scene boundaries, waterfall entries and nudge curves inside a scene. Match the sign of the Z velocity across a cut, blur the wrapper and never the children, and give exit opacity its own linear tween.
7. Keep the stage ground opaque, use one surface per visual theme, and fire a visible cut only on a narrative beat — at most once per ~8 seconds, never mid-caption or during a hold.
8. Finish through the CLI: lint, check, inspect, preview in the studio and pause for approval, then render locally. Use the strict/docker flags for the final render.
9. Review the motion against the craft bar before delivering: justified motion, physical correctness (scale from the trigger, never from scale(0)), interruptibility, and no animation that exists because it looked cool.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`html-video-production`](references/html-video-production/) | The full production skill — fidelity gate, three routes, media contract, hard rules, CLI finish, file map. |
| [`hyperframes-registry`](references/hyperframes-registry/) | ~450 ready-made blocks installed as editable source; search before hand-building a named visual. |
| [`cut-the-curve`](references/cut-the-curve/) | The technique catalog: five velocity-matched seams plus waterfall entry and the nudge curve. |
| [`review-animations`](references/review-animations/) | The craft bar for reviewing motion code — ten standards, escalation triggers, required findings table. |
| [`video-template-frame-light-leak-cinema`](references/video-template-frame-light-leak-cinema/) | A complete cinematic template: film light leaks, grain, 16:9 letterbox, large serif type. |

## Key files / entry points

- `references/html-video-production/` — the full production skill: fidelity gate, routes, the media contract, hard rules, file map.
- `references/hyperframes-registry/` — the ~450-block registry and how to install from it.
- `references/cut-the-curve/` — the seam catalog, with code and anti-patterns.
- `references/review-animations/` — the ten non-negotiable motion standards and the required review format.
- `references/video-template-frame-light-leak-cinema/` — a complete worked template (light leaks, grain, letterbox, serif type).

## Gotchas

- `npx hyperframes init` and `npx hyperframes skills update` overwrite the patched skills; `hyperframes lambda *` is paid cloud. Scaffold manually, render locally.
- Never set the upstream API keys or run the upstream audio/resolve media paths — produce media natively.
- Animating children instead of the wrapper breaks the blur and the seam.
- A self-contained composition must not pull network assets or the headless render fails.
- Same axis is not enough on Z: the sign of d(scale)/dt must match across the cut.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `html-video-production` — carries its own LICENSE file
- `hyperframes-registry` — no licence file shipped with the source
- `cut-the-curve` — no licence file shipped with the source
- `review-animations` — no licence file shipped with the source
- `video-template-frame-light-leak-cinema` — no licence file shipped with the source
