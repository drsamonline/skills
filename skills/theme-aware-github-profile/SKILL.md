---
name: Theme-aware GitHub profile
description: A professional, self-updating GitHub profile README — a bespoke light/dark hero served through <picture>, a lowlighter/metrics card rendered twice with extras_css palettes, and a daily workflow that regenerates a badge row and a categorised project list from the GitHub API between HTML comment markers.
---

# Theme-aware GitHub profile

A GitHub user's profile page is the README of the repository named after the owner (`drsamonline/drsamonline`), and it is the one surface where the README itself has to look deliberate in **both** light and dark mode — something GitHub gives no native support for. The whole profile is a single `README.md` plus a small `assets/` folder and one daily workflow; every image is either hand-authored (the hero) or regenerated automatically (the metrics card, the badges, the project list).

## When to use

- You want a GitHub profile that reads as a designed product page rather than a wall of badges.
- The README must look intentional whether the visitor's GitHub is in light or dark mode.
- New repositories should appear on the profile without anyone editing the README by hand.
- You want a small, quiet, self-maintaining profile — not a maximal one.

## Method

1. Hand-author the hero banner twice, as `assets/hero-light.svg` and `assets/hero-dark.svg`, and serve the pair through a single `<picture>`:

   ```html
   <picture>
     <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
     <img alt="Dr. Sohil Momin — homeopathic physician & builder of offline-first open-source software" src="assets/hero-light.svg">
   </picture>
   ```

   `<picture>` with `media="(prefers-color-scheme: dark)"` is GitHub's **only** mechanism for theming a README: GitHub sanitises `<style>` and strips most CSS, so there is no stylesheet hook — the `<picture>` element is the one thing that can respond to the colour scheme.

2. Render the metrics card **twice** with [`lowlighter/metrics`](https://github.com/lowlighter/metrics) — once per theme — into `assets/metrics-light.svg` and `assets/metrics-dark.svg`. Use the `classic` template with the `base` and `calendar` plugins, and give each render its own `extras_css` palette so the light and dark variants stay visually in step. Embed the pair with the same `<picture>`/`<source>` pattern as the hero. Both renders run in **one** workflow job so the two themes can never drift apart.

3. Make the profile self-updating. Wrap a badge row between `<!-- BADGES:START -->` / `<!-- BADGES:END -->` and a categorised project list between `<!-- PROJECTS:START -->` / `<!-- PROJECTS:END -->`. A daily workflow (cron + `workflow_dispatch`) reads the owner's repositories from the GitHub API, rebuilds the badge row (a small shields.io set) and the categorised project list, regex-replaces each marked block, and commits **only if the file actually changed** — so a new repo shows up on the profile the next day with nothing edited by hand.

4. Apply the deliberate restraint rules — they are the point of the exercise, not decoration:
   - **No emoji headings.** Use plain text headings; emoji in a profile reads as noise.
   - **A small badge set.** A handful of meaningful badges, not every badge that exists.
   - **One idea per section.** Each section says one thing and stops.
   - **No pure black or pure white.** Use near-black and near-white (not `#000000` / `#ffffff`) so the page has tone and neither theme glares.

5. Keep the optional third-party embed (the `githubtrends.io` lines-of-code card) present but commented out and ready to enable once its account exists, rather than dropping it in half-configured.

## Key files / entry points

- `README.md` — the hero `<picture>`, the metrics `<picture>`, the `<!-- BADGES -->` and `<!-- PROJECTS -->` marker blocks, and the restraint-styled sections.
- `assets/hero-light.svg`, `assets/hero-dark.svg` — the hand-authored hero pair.
- `assets/metrics-light.svg`, `assets/metrics-dark.svg` — the generated metrics pair (one render per theme).
- `.github/workflows/*.yml` — the daily job that renders both metrics cards and regenerates the marked blocks, committing only on change.

## Gotchas

- `${{ secrets.GITHUB_TOKEN }}` **cannot read the `stargazers` field that metrics' base query requests.** The render fails with `FORBIDDEN: Resource not accessible by integration`, which silently empties the `plugin_languages` panel while the action still reports success — the card looks broken and there is no error to chase. The fix is a **classic personal access token with no scopes**, saved as the secret `METRICS_TOKEN` and passed to the metrics step as `token:`.
- `config_theme` is **not** a real metrics option and does nothing, despite being widely copied between profiles. Theme control comes from the template and `extras_css`, never from `config_theme`.
- GitHub sanitises `<style>` and most CSS in a README, so `<picture>` is the only theming hook — media queries in a `<style>` block will not work.
- Render the light and dark metrics cards in the same job; a change to one theme otherwise leaves the other stale and the profile looks mismatched.
- Commit the regenerated blocks only when they changed, or the daily job leaves a noisy commit every single day.

## Source projects

- [drsamonline](https://github.com/drsamonline/drsamonline) — the live profile: the light/dark hero and metrics `<picture>` pairs, the marker blocks and the daily regenerate workflow.
- [drsamonline.github.io](https://github.com/drsamonline/drsamonline.github.io) — the project hub that shares the same self-updating, commit-only-on-change discipline.
- [profile-kit](https://github.com/drsamonline/profile-kit) — the reusable kit extracted from this work, so another account can adopt the whole profile.

### References credited

- [lowlighter/metrics](https://github.com/lowlighter/metrics) — the rendering engine: its `classic` template, the `base` and `calendar` plugins, and `extras_css` for the light/dark palette pair.
- [avgupta456/github-trends](https://github.com/avgupta456/github-trends) — the lines-of-code-by-language-over-time idea, and the embed-a-hosted-SVG pattern (parked pending an account).
- [rzashakeri/beautify-github-profile](https://github.com/rzashakeri/beautify-github-profile) — the catalogue this profile was worked from: the badge vocabulary from its Badges section, and the metrics chosen from its Widgets list, with the busier widgets deliberately left out.
