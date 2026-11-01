---
name: repo-presentation
description: Present a built repository the way this estate presents its apps — a designed landing page at docs/index.html, the app itself at docs/play/, screenshots taken with headless Chromium, local SVG badges generated rather than fetched, and a README that leads with them. Use when publishing a new build/publish repo, or when an existing one has no landing page, no screenshots, or a README with no badges.
---

# Repo presentation

Every repository in this estate ships the same three surfaces, each with its own design:
a **landing page**, a **README**, and the **app or product itself**. The design is unique per
repository — the shared part is the structure and the discipline, never the styling.

## When to use

- A new app or kit has just been built and pushed, and needs its public face.
- An existing repo has a bare README, or the app is served at `docs/index.html` with no landing page.
- The owner asks for "a landing page", "badges", "screenshots", or "a beautified README".

## Method

1. **Split the app from the page.** Move the app to `docs/play/` (`index.html` plus whatever it
   loads: `thermals.js`, `vendor/`, `data/bundle.js`, `sw.js`, `manifest.webmanifest`, `icon.svg`).
   Relative paths inside `docs/play/` keep working; only the *entry* path changes.
   `docs/index.html` becomes the landing page. Update the tests that read the page, the service
   worker's file list, and the build workflow (`app_src: docs/play`, `deploy_path: docs`).
2. **Design the page for that project only.** Pick one strong idea from the subject and build the
   page around it — a thermal gradient for a remedies app, a punched card for a loom machine.
   Use it in the band, the hero and one accent; do not import a shared stylesheet. Serif display
   against a sans body, paper tones against one saturated accent, works for most of this estate.
   Sections that carry their weight: hero + CTAs + badges, one screenshot of the real app, what it
   does (3 cards), what it refuses to do, the numbers, the sources, how to run it, footer.
3. **The demo is the app, embedded — not a picture of it.** A landing page whose "demo" is a
   screenshot looks like the app twice. Put the real app in a browser frame
   (`<iframe src="play/">`) and drive it with three or four **guided buttons** that move the frame
   to a route worth seeing (`play/#/remedy/<slug>`) — the two-source case, the unclassified case,
   the case that shows the feature you are proudest of. Layer a poster screenshot *behind* the
   frame and reveal the frame only once it has loaded (`location.protocol` http/https +
   `load` event), so a demo that cannot load never looks broken.

4. **Screenshots, from the real page.** `scripts/shot.sh <repo> <name>` writes
   `docs/assets/<name>-desktop.png` and `-mobile.png` with headless Chromium. Look at them before
   committing — a page that renders wrong is worse than no screenshot.
5. **Badges, generated locally.** `scripts/badges.py` draws the SVGs into `docs/assets/badge-*.svg`
   and the README/landing page reference them by relative path. Never point a badge at an image
   service: an offline-first repo that needs the network to describe itself has broken its own rule.
   Keep the *claims* true — the assertion count, the licence, the dependency count.
6. **README leads with them.** Badges, one-line promise, links (live app, landing page, rule,
   sources), then the pipeline's own screenshot block:

   ```
   <!-- shot:start -->

   ![Screenshot](docs/shot.png)

   <!-- shot:end -->
   ```

   Keep those markers: `app-builder`'s `shot` job rewrites `docs/shot.png` and that block on every
   build, and it silently stops working if the markers go.
7. **Verify, then say so.** Fresh clone → tests → open the landing page and the app in headless
   Chromium and look at both. Only then report it as done.

### The landing page must not look like the app

This is the failure to avoid, and it happened the first time: the page borrowed the app's palette,
type and rhythm, so the two read as the same product twice. Make them different objects —

| | app (`docs/play/`) | landing page (`docs/`) |
|---|---|---|
| canvas | warm paper | dark, or a colour the app never uses |
| type | the app's own face | a display face it does not use |
| rhythm | one centred column | full-bleed bands, a light interlude, a closing CTA |
| the product | is the interface | is shown *inside a frame* with callouts |

**Neither surface may force a theme.** Light is the base palette; the system preference decides the
first paint; a toggle in the header (landing page) and beside the title (app) overrides it, and the
choice is remembered under *separate* keys so setting one does not silently change the other. Wire
the whole page to the same variables — demo bands, browser frames and device mocks are where
hardcoded dark colours hide and the light mode then looks broken.

## Key files

```
docs/index.html              the landing page — this project's own design
docs/play/index.html         the app or product
docs/play/…                  everything the app loads
docs/assets/app-desktop.png  screenshot, desktop width
docs/assets/app-mobile.png   screenshot, phone width
docs/assets/badge-*.svg      generated badges
docs/shot.png                the pipeline's own screenshot (do not hand-edit)
README.md                    badges → promise → links → screenshot → substance
```

## Gotchas

- **A single multi-file commit has a size limit.** Base64 PNGs blow through it: commit text and SVG
  with `GITHUB_COMMIT_MULTIPLE_FILES`, then add each PNG separately with
  `GITHUB_CREATE_OR_UPDATE_FILE_CONTENTS`. A 600 KB screenshot will 413 the whole batch.
- **Multi-file commits do not delete.** After moving the app into `docs/play/`, the old copies stay
  in `docs/` and get deployed alongside the landing page. Pass them in `deletes`.
- **`chromium` needs `--no-sandbox --disable-gpu --hide-scrollbars`** in this sandbox, and writes
  to `/tmp` fine. `--window-size=1280,1400` is a good default; `430,860` for the phone shot.
- **A cache-first service worker hides every release.** This is the one that made a shipped,
  green-deployed toggle invisible: the worker answered the HTML from cache and the cache name had
  not changed, so a returning reader kept the old app with no way to know. Serve the **HTML
  network-first** (cache is only the offline fallback), keep assets cache-first with a background
  refresh, **bump `CACHE` on every release**, call `registration.update()` on load, and print a
  **build stamp** in the footer so "am I on the new one?" is answerable from the page itself.
- **An iframe of the app needs a poster.** Same-origin `play/` works on Pages and even from
  `file://` in Chromium, but a visitor with a blocked frame should still see the product: keep the
  screenshot behind the frame and reveal the frame only after `load`.
- **Take the screenshot of a page with content.** A landing page whose app shot shows an empty
  search box sells nothing; open the app on a populated view first.
- **Check the claims in the badges against the repo.** "567 passing" must be the number the suite
  actually prints, and the licence badge must match `LICENSE`.
- **Do not let the design escape its repo.** Copy the structure, never the palette; two estate apps
  that look identical read as one product with two names.

## Source projects

`drsamonline/app-thermals` — landing page, local badges, screenshots and README as first built.
`drsamonline/app-jacquard`, `drsamonline/app-lantern` — the `docs/play/` split and the pipeline
conventions this follows.
