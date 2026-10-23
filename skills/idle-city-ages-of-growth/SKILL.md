---
name: idle-city-ages-of-growth
description: A single-file idle city-builder that grows from a Stone Age village to a Fusion Age world-city: roads, zoning, power and happiness, running itself while you plan and expand.
metadata:
  title: "Idle City — Ages of Growth"
---

# Idle City — Ages of Growth

Idle City is a single-file idle city-builder that grows from a Stone Age village into a Fusion Age world-city. Lay roads, zone land, generate power and keep citizens happy — the city runs itself while you watch, plan and expand. Canvas 2D, zero dependencies, fully offline, mobile-ready. Source-available under PolyForm Noncommercial 1.0.0.

## When to use

- You want to build or extend a single-file simulation/idle game.
- You need a reference for an ages/progression loop and a self-running simulation.
- You want a game with a noncommercial licence rather than MIT.

## Method

1. Keep the whole game in one HTML file with a Canvas 2D simulation and an idle tick that advances the city while the player plans.
2. Model progression as ages (Stone → … → Fusion) that unlock buildings, utilities and scale.
3. Provide zoning (residential/commercial/industrial), roads and power as the core placement mechanics; track happiness as the balancing lever.
4. Make it mobile-friendly (touch placement, responsive canvas) and fully offline.
5. Ship a landing page + play copy in `docs/`, and build EXE + APK with `.github/workflows/build-apps.yml` (and `build.yml`).
6. State the licence clearly: PolyForm Noncommercial 1.0.0, attribution required, commercial use needs a licence.

## Key files / entry points

- `docs/play/index.html` — the playable game; `docs/index.html` — landing page.
- `assets/screenshot-desktop.png`, `assets/screenshot-mobile.png`.
- `ATTRIBUTION.md`, `LICENSE`, `.github/workflows/build.yml`, `.github/workflows/build-apps.yml`.

## Gotchas

- Idle progression needs a real sink and a real wall, or it plateaus; balance it against the age curve.
- The licence is noncommercial — do not ship it in a commercial bundle.
- Large grids on mobile need a light render path (redraw only what changed / off-screen culling).

## Source projects

- [idle-city-ages-of-growth](https://github.com/drsamonline/idle-city-ages-of-growth) — PolyForm Noncommercial 1.0.0, v1.1.0.

