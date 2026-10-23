---
name: matneo-storefront
description: A static storefront served from docs/ with no build step: a single data file (docs/data/products.json) drives the catalogue, so new products are added by editing JSON, not markup.
metadata:
  title: "Matneo — static storefront"
---

# Matneo — static storefront

Matneo is a static storefront for AI-powered digital products and automation tools. The whole site is the shop — plain HTML, CSS and JavaScript, no build step, served from `docs/` via GitHub Pages. The catalogue is driven by a single data file, `docs/data/products.json`, so a new product is added by editing that file; there are also product pages, a blog and free downloads.

## When to use

- You are building a static catalogue where content is data, not markup.
- You want a no-build storefront that stays current by editing one JSON file.
- You need product, blog and download pages served from `docs/`.

## Method

1. Keep the site plain HTML/CSS/JS with no build step, served from `docs/` (also mirrored at the repo root).
2. Drive the catalogue from `docs/data/products.json` (and `docs/data/settings.json`) so adding a product is a data edit; render client-side with `docs/js/products.js` and `docs/js/app.js`.
3. Provide product pages (`docs/products/`), a blog (`docs/blog/`) and a downloads page (`docs/downloads/`).
4. Ship `docs/404.html`, `.nojekyll`, `assets/favicon.svg`, and the site CSS in `docs/css/style.css`.
5. Keep the pages self-contained and fast; no external JS libraries.

## Key files / entry points

- `docs/data/products.json`, `docs/data/settings.json` — the catalogue.
- `docs/js/app.js`, `docs/js/products.js` — the render layer.
- `docs/index.html`, `docs/products/`, `docs/blog/`, `docs/downloads/`, `docs/css/style.css`, `docs/404.html`.

## Gotchas

- Content-as-data means the JSON schema is the API — validate it or a typo blanks the catalogue.
- Keep the root mirror and `docs/` in sync, or edit only the served copy to avoid drift.
- No build step means no bundler conveniences — keep JS small and dependency-free.
- Product/download links must be stable; point them at release URLs where possible.

## Source projects

- [Matneo](https://github.com/drsamonline/Matneo) — static storefront, JSON-driven catalogue.

