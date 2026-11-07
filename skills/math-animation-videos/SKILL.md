---
name: math-animation-videos
description: "Produce code-driven explanatory animation and precise vector graphics with the Manim engine: mathematical visualisations, algorithm walkthroughs, derivations with LaTeX, 3Blue1Brown-style scenes. Use when the user mentions Manim, ManimCE or ManimGL, or wants an animated explanation rather than a generated clip. Not for photoreal video or ordinary screen recording."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Math and algorithm animation (Manim)"
  category: "media-design"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "manim-animator"
---

# Math and algorithm animation (Manim)

An explanatory animation is a program: scenes, objects, transforms. The work is planned scene by scene before a line is written, because a Manim scene that was not planned becomes an unreviewable 400-line file. One framework, chosen once, never mixed.

## When to use

- A concept, proof, algorithm or dataset needs to be explained by animation.
- Precise vector diagrams or LaTeX typesetting must move.
- The style requested is 3Blue1Brown, or the user names Manim.

## Method

1. Stage 1 — choose the framework (ManimCE by default, ManimGL only when the request needs it), record the choice, and do not mix them for the rest of the task. Stop early if the request is really an AI-generated video.
2. Stage 2 — read the decision tree and the framework rules that apply, so the code you write is inside the allowed subset.
3. Stage 3 — plan the scenes in a `scenes.md`: overview, narrative arc, per-scene duration and purpose, and what the viewer should understand at the end of each. Anything longer than one short clip gets this file.
4. Stage 4 — write `video.py` against the hard rules: no external resource files, no runtime `config.*` mutation, no third-party imports beyond Manim plus the scientific stack, deterministic layout.
5. Stage 5 — render a low-quality draft and watch it before the expensive pass.
6. Stage 6 — render at delivery quality only after stage 5 reports success.
7. Stage 7 — if the high-quality render exposes a latent bug, fall back to stage 6 once and retry; never hand-edit the rendered output.
8. Narration, when needed, is one audio clip per scene — never one monolithic file — so a re-render of one scene does not force a re-record.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`manim-animator`](references/manim-animator/) | The full seven-stage Manim workflow with framework decision tree, hard rules, scene planning and narration contract. |

## Key files / entry points

- `references/manim-animator/` — the seven-stage workflow, decision tree, framework rule files, composer and prompt references.
- `references/manim-animator/scripts/` — helper scripts for rendering and assembly.

## Gotchas

- Mixing ManimCE and ManimGL mid-task produces code that renders nowhere.
- Mutating `config.*` at runtime is forbidden — it changes behaviour between scenes.
- A single narration file makes every re-render expensive.
- Skipping the low-quality draft pass hides layout collisions until the expensive render.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `manim-animator` — no licence file shipped with the source
