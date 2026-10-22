---
name: Static landing page, SEO and accessibility conventions
description: The house landing-page recipe: a bespoke self-contained docs/index.html with a distinct theme, a full SEO head (canonical, OG, Twitter, JSON-LD, robots), robots.txt, sitemap.xml, .nojekyll and a themed 404.
---

# Static landing page, SEO and accessibility conventions

Each drsamonline project ships its own landing page at `docs/index.html`, served by GitHub Pages (legacy build, source `main`, path `/docs`). It is a **bespoke, self-contained** page: inline CSS/JS, no external JS libraries, inline SVG icons, never emoji, one distinct visual theme per site. It is fully responsive with no horizontal overflow down to 390px. The app itself usually lives beside it at `docs/play/`.

## When to use

- A project needs a public page explaining what it is and linking to the live app and downloads.
- You want the page to be indexable, shareable (OG/Twitter cards) and rich in search results (JSON-LD).
- The repo will serve Pages from `docs/`.

## Method

1. Write `docs/index.html` with `<!DOCTYPE html>`, `lang="en"`, and a `viewport` meta including `viewport-fit=cover`. All CSS in one `<style>`, all JS in one inline `<script>`. No CDN, no framework.
2. Build the SEO head: `<title>`, `meta description`, `meta keywords`, `meta author`, `meta robots="index, follow, max-image-preview:large, max-snippet:-1"`, `theme-color`, `color-scheme`, `<link rel="canonical">`, and an inline-SVG favicon as a `data:` URI plus `apple-touch-icon`.
3. Add Open Graph (`og:type`, `og:site_name`, `og:title`, `og:description`, `og:url`, `og:image` + width/height/alt, `og:locale="en_IN"`) and Twitter (`twitter:card=summary_large_image`, title, description, image, image:alt).
4. Add a `<script type="application/ld+json">` block describing the project (`SoftwareApplication`/`WebSite`, with name, description, applicationCategory, operatingSystem, url, codeRepository, author Person, keywords).
5. Ship the supporting files: `docs/.nojekyll` (so `_`-prefixed paths are served), `docs/robots.txt` (`User-agent: *` / `Allow: /` / `Sitemap: <site>/sitemap.xml`), and `docs/sitemap.xml` (one `<url>` with `loc`, `lastmod`, `changefreq`, `priority`).
6. Add a themed `docs/404.html` that reuses the site palette, has `meta robots="noindex, follow"`, and links back to the home page.
7. Structure the page: a hero with a one-line pitch and primary CTAs (Open app / Download), a features grid, screenshots, a how-it-works section, FAQ, and a footer. Link downloads to the stable `/releases/latest/download/<asset>` URLs.
8. Accessibility: semantic landmarks (`header`/`main`/`footer`/`nav`), `aria-label`s on nav and controls, `alt` text on every image, inline SVG marked `aria-hidden="true"`, visible focus styles, sufficient contrast, and `prefers-reduced-motion` respected for any animation.
9. Responsiveness: mobile-first, fluid type, `grid`/`flex` with `minmax`, and `overflow-wrap`; verify no horizontal scroll at 390px and 1440px.
10. Set Pages in the repo to `build_type="legacy"`, source `main`, path `/docs`, and set the repo `homepage` to the site URL.

## Key files / entry points

- `docs/index.html` — the landing page.
- `docs/404.html` — themed not-found page.
- `docs/robots.txt`, `docs/sitemap.xml`, `docs/.nojekyll`.
- `docs/play/` — the live app the page links to (when the project has one).
- `docs/assets/favicon.svg` — the icon (also inlined as a data: URI in the head).

## Gotchas

- Legacy Pages serves the `docs/` folder as-is — there is no build step, so everything the page needs must be committed.
- Keep OG/Twitter image dimensions honest (1280×640) and give a real `og:image:alt`.
- No emoji anywhere in the shipped page; use inline SVG icons. The theme must be distinct per project, not a shared template recoloured.
- Test 390px *and* 1440px for horizontal overflow — long unbroken strings (URLs, code) are the usual culprit.
- A `data:`-URI favicon avoids shipping an icon file and an extra request; keep the SVG small.

## Source projects

- [app-builder](https://github.com/drsamonline/app-builder) — a compact, complete landing page + SEO block.
- [homoeopathic-materia-medica-repertory-json](https://github.com/drsamonline/homoeopathic-materia-medica-repertory-json) — a dataset landing page with the same head conventions.
- [neon-runner](https://github.com/drsamonline/neon-runner) — a game landing page with hero cards and download links.
- [conqueror-os](https://github.com/drsamonline/conqueror-os) — a themed landing page for a single-file app.

