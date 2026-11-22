---
name: monuments-generated-in-code
description: Rebuild twenty-four monuments as live 3D miniatures in the browser with no photographs, no downloaded meshes and no build step — every dome, bracket and lattice screen generated from code, lit by a physical sky, and paired with the history behind it.
metadata:
  title: "INDIA"
---

# INDIA — monuments rebuilt in code

Twenty-four Indian monuments, rebuilt as live 3D miniatures in the browser. No photographs in the
models, no downloaded meshes, no build step: every dome, bracket and lattice screen is generated
from code with three.js, lit by a physical sky, and paired with the history behind it.

## When to use

- The subject is architecture and the model has to be *made*, not scanned — a procedurally built dome teaches more than a mesh.
- The page must ship with no assets: geometry from code, light from a physical sky model.
- A cultural subject needs its history attached, not just its silhouette.

## Method

1. One page per monument, one generator per architectural element (dome, bracket, jali screen, plinth) — the elements repeat across buildings, which is why 24 of them are affordable.
2. Build geometry procedurally with three.js primitives and parametric loops; keep every dimension in a small data table per monument so proportions are reviewable.
3. Light with a physical sky rather than a hand-placed rig, so each page looks right at any time of day without per-monument tuning.
4. Pair each model with its history: place, period and the one fact worth knowing — the model is the hook, the history is the content.
5. Keep a landing page that indexes all 24 with their periods, and no build step at all.

## Key files / entry points

- The per-monument generator and its dimension table.
- The shared element library (dome, bracket, lattice).
- The landing page index.

## Gotchas

- Procedural architecture drifts from the real building fast; a dimension table with sources is what keeps it honest.
- A lattice screen built from real geometry is thousands of triangles — instance it, or the phone drops to 12 fps.
- "No photographs" is a claim about the *models*; the history pages may still need sourced images, and that is a different licence question.

## Source projects

- [INDIA](https://github.com/drsamonline/INDIA)
