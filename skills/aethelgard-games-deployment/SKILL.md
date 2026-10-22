---
name: Aethelgard — two games (deployment)
description: A deployment repo holding the built, playable copies of two Aethelgard browser games — The Books (a 36-chapter visual novel) and Chronicles of Fate (a deep single-player RPG) — so GitHub Pages can serve them.
---

# Aethelgard — two games (deployment)

Aethelgard — Two Games is a **deployment repo**: it holds the built, playable copies of both games so GitHub Pages can serve them — *The Books* (a visual novel in three books, 36 chapters, 7 endings, four hidden counters) and *Chronicles of Fate* (a fantasy RPG with 8 classes, 8 races, two campaigns, crafting, settlement building and an endless dungeon). Both are plain HTML/CSS/JS, no server, no framework, no dependencies.

## When to use

- You are publishing a built game (or two) to GitHub Pages and want the deployment layout.
- You need a landing page that links multiple playable builds and their downloads.
- You want to understand the split between engine repos and the deployment repo.

## Method

1. Keep each game in its own folder under the repo (`books/`, `chronicles/`) with the built assets and its own README/CHANGELOG.
2. Serve both from `docs/play/` (with sub-paths per game) and a landing page at `docs/index.html`.
3. Link downloads to the stable release assets per game (`aethelgard-games-books-portable.exe`, `…-chronicles.apk`, …).
4. Build the portable EXE + APK for each game with `.github/workflows/build-apps.yml`.
5. Keep `.nojekyll` at the root so underscore-prefixed paths are served.

## Key files / entry points

- `books/` and `chronicles/` (or equivalent) — the built games.
- `docs/play/` — the served play copies; `docs/index.html` — landing page.
- `.github/workflows/build-apps.yml`, `.nojekyll`.

## Gotchas

- This repo holds built copies; source changes belong in `Aethelgard-Engine` / `AethelgardVN`.
- Per-game asset names must be distinct so the release is unambiguous.
- Large sprite sets (`books/assets/sprites/*.webp`) bloat the repo — keep them webp and consider lazy loading.

## Source projects

- [aethelgard-games](https://github.com/drsamonline/aethelgard-games) — deployment repo for two Aethelgard games.

