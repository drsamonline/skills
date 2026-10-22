---
name: Offline-first single-file web app
description: Build a whole app as one self-contained index.html — inline CSS/JS, no CDN, no build step — that runs from file:// or GitHub Pages, works offline, and persists data locally.
---

# Offline-first single-file web app

The house default for a drsamonline browser app: one `index.html` that carries the entire application. All CSS is in a `<style>` block, all JavaScript in `<script>` blocks, every icon an inline `<svg>`. There is no bundler, no npm runtime dependency, no CDN and no network call after first load, so the same file runs from a USB stick, from `file://`, and from GitHub Pages unchanged.

## When to use

- The deliverable is a browser tool or small app that must work with no server and no internet.
- You want one artefact to hand to a user (email, USB, `file://`) rather than a build output tree.
- The app is also going to be wrapped as a portable Windows EXE or an Android APK — the single-file layout is what those wrappers consume.
- You need the app to survive offline (clinics, field work, aeroplanes) with no backend and no account.

## Method

1. Start from one `index.html`. Put `<style>` in the `<head>` and one or more `<script>` blocks at the end of `<body>`. Keep the CSP meta tag permissive only for what you need (inline style/script, `img-src https: data:`).
2. Use only platform APIs: DOM, Canvas 2D, Web Audio, `localStorage` / `IndexedDB`, `fetch` for optional extras. Do not add a framework or a CDN `<script src>`; icons are inline `<svg>`, never an icon font or emoji.
3. Persist user data locally. Small settings go in `localStorage`; structured records (notes, cases, sessions) go in `IndexedDB`. Always provide an explicit **export** (JSON download) and **import** so the user owns their data and can move it between devices.
4. Design for the offline case first: no spinner that waits on a network call, no remote font, no remote image. Everything the first paint needs is in the file.
5. Make it a PWA where useful: add a `manifest.webmanifest` (name, icons, `display: standalone`, theme colour) and a small `sw.js` service worker that precaches the shell. The icons live in `docs/play/` next to the app. Register the service worker only when served over http(s); guard the registration so `file://` still works.
6. Keep a fixed visual theme per app (the house style is one distinct palette per site) and inline SVG for the favicon as a `data:` URI so no icon file is required.
7. Split the app's source into small modules only when it grows; ship them as plain ES modules (`<script type="module">`) or concatenated IIFEs, still with no build step. Larger apps (retro-strike, idle-city) keep one document and organise by comment-delimited sections.
8. Test by opening the file directly (`file://`) and from a static server (`python3 -m http.server`), then offline (DevTools → Network → Offline) to confirm nothing depends on the network.

## Key files / entry points

- `index.html` — the entire app (inline `<style>` + `<script>`).
- `docs/play/index.html` — the published copy the EXE/APK wrappers and Pages both serve (same file, copied into the landing repo layout).
- `docs/play/manifest.webmanifest`, `docs/play/sw.js` — PWA manifest and precache service worker.
- `docs/play/icons/icon-192.png`, `icon-512.png` — PWA/home-screen icons.

## Gotchas

- `file://` blocks service workers and some `fetch`; guard every browser API behind a feature check so the file still opens locally.
- A single-file app grows fast — keep CSS and JS sectioned with comment banners or it becomes unmaintainable. Large apps here ship 100–200 KB minified, one file.
- Do not reach for a CDN 'just for one library'. That single dependency is what breaks the offline promise; write the ~50 lines instead.
- `localStorage` is per-origin: moving between `file://`, a local server and the Pages URL means the data does not follow. Export/import is the portable path.
- Storage can be evicted; always offer export and never make export a second-class feature.

## Source projects

- [conqueror-os](https://github.com/drsamonline/conqueror-os) — a private offline resilience workspace in a single HTML file (read, journal, track, review).
- [ambient-sound-studio](https://github.com/drsamonline/ambient-sound-studio) — 25 synthesised layers, 36 presets, WAV/Opus export, installable PWA, one file.
- [retro-strike](https://github.com/drsamonline/retro-strike) — a full 3D third-person shooter (custom software renderer) in one HTML file.
- [boericke-repertory](https://github.com/drsamonline/boericke-repertory) — 6,110 rubrics + repertorisation chart, single file, no dependencies.
- [bmi-bmr-tdee-macros-fluid-calculator](https://github.com/drsamonline/bmi-bmr-tdee-macros-fluid-calculator) — clinical calculator, EN/HI/GU, CSV export/import, offline.

