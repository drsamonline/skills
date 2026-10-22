---
name: Clinical Health Calculator
description: A single-file, offline clinical calculator for adult outpatients: BMI, BMR (Mifflin-St Jeor), TDEE, macros, fluid requirement and body composition, with Indian/WHO cut-offs and EN/HI/GU UI.
---

# Clinical Health Calculator

Clinical Health Calculator is a single-file, offline-capable clinical calculator for adult outpatients: BMI, BMR (Mifflin-St Jeor), TDEE, macros, fluid requirement and body composition, with Indian/WHO BMI cut-offs, saved entries, CSV export/import and an EN/HI/GU UI. No build step, no dependencies, no server, no tracking. MIT.

## When to use

- You are building a small clinical calculator that must work offline.
- You need locale-aware cut-offs (Indian/WHO BMI) and a trilingual UI.
- You want CSV export/import for saved entries in a single-file app.

## Method

1. Keep the app in one HTML file (root `index.html`, published at `docs/play/`) — no build step, no dependencies.
2. Implement the standard formulas (BMI; BMR via Mifflin-St Jeor; TDEE from an activity factor; macros; fluid requirement; body composition) and label each with its formula.
3. Use locale-appropriate cut-offs (Indian/WHO BMI categories) and show them explicitly.
4. Persist saved entries locally and support CSV export/import so a clinician can move data.
5. Provide the trilingual UI (English / Hindi / Gujarati).
6. Ship a landing page (`docs/index.html`) with the full SEO block, `robots.txt`, `sitemap.xml`, `404.html`, `.nojekyll`; build EXE + APK with `.github/workflows/build-apps.yml`.

## Key files / entry points

- `index.html` — the app; `docs/play/index.html`, `docs/play/src/clinical-health-calculator.html`.
- `docs/index.html` — landing page; `docs/404.html`, `docs/robots.txt`, `docs/sitemap.xml`, `docs/.nojekyll`.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Name the formula behind every number; a clinical calculator must be auditable.
- Indian BMI cut-offs differ from WHO's — do not silently apply the wrong one.
- CSV export must round-trip through import without loss.
- It is a calculator, not advice — keep the disclaimer and the 'consult a professional' line.

## Source projects

- [bmi-bmr-tdee-macros-fluid-calculator](https://github.com/drsamonline/bmi-bmr-tdee-macros-fluid-calculator) — MIT, single file, EN/HI/GU.

