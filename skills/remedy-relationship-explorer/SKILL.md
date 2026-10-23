---
name: remedy-relationship-explorer
description: An offline single-file explorer for homeopathic remedy relationships — 686 remedies, 7,786 links from four public-domain materia medicas — visualised as an interactive graph with keynotes, quizzes and a Tauri desktop build.
metadata:
  title: "Remedy Relationship Explorer"
---

# Remedy Relationship Explorer

Remedy Relationship Explorer is a study and reference tool for homeopathic remedy relationships (complementary, antidotal, inimical, 'follows well', 'compare'), extracted from four public-domain materia medicas (Boericke 1927, Clarke 1900, Hering 1879, Allen 1898) and shown as an interactive graph — 686 remedies, 7,786 relationships, 653 keynotes. It is one self-contained `app.html` with no server or backend, plus a Tauri desktop build.

## When to use

- You are building an offline, single-file graph explorer over structured data.
- You need a force-directed network view with a focus/ring view and collision-aware layout.
- You want provenance carried per edge and a colour-blind-safe, accessible palette.

## Method

1. Keep the app in one `app.html` (no server, no backend, no API keys, no build step) with the graph data embedded; published at `docs/app.html`.
2. Provide a **focus view** (one remedy, relationships in a ring, click to re-centre with breadcrumbs) and a **network view** (force-directed graph with a detail slider and collision-aware layout).
3. Search by name or symptom (full-text over keynotes); support query expressions ('inimical to Lachesis and complementary to Sulphur'), compare-two-remedies with Jaccard overlap, and shortest path.
4. Carry provenance per relationship (superscript B/C/H/A) and offer a 'corroborated only' filter (≥2 books); filter by type, kingdom and source.
5. Add study features: keynotes reader, flashcards, three quiz modes, a study notebook (Markdown export), PNG export and a printable remedy sheet.
6. Accessibility: keyboard shortcuts, screen-reader support, system-aware light/dark, a high-contrast theme, adjustable text size and a colour-blind-safe palette with dashed edge patterns.
7. Add a Tauri desktop build (`desktop/src-tauri/`) with `build-desktop.yml` and `build-android.yml`; document the extraction method in `docs/data.md`.

## Key files / entry points

- `app.html` — the whole app; `docs/app.html` — published copy; `docs/index.html` — landing page.
- `desktop/` + `desktop/src-tauri/` — Tauri desktop wrapper; `.github/workflows/build-desktop.yml`, `build-android.yml`.
- `docs/data.md` — extraction method; `CITATION.cff`, `LICENSE`.

## Gotchas

- Force-directed layout must be collision-aware or nodes overlap illegibly; expose a detail slider.
- Provenance per edge is the point — never merge two books' links without keeping the source.
- Colour alone must not carry meaning; use dashed patterns and labels too (colour-blind safety).
- The data is OCR-derived from historical texts — keep the 'verify against the printed sources' disclaimer.

## Source projects

- [remedy-relationship-explorer](https://github.com/drsamonline/remedy-relationship-explorer) — custom licence, Tauri + web.

