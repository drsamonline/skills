---
name: profile-kit — reusable GitHub-profile kit
description: A small, reusable kit for a theme-aware, self-updating GitHub profile — a hero banner, a metrics card and a README generator — extracted from the drsamonline profile so another account can adopt the whole thing instead of rebuilding it.
---

# profile-kit — reusable GitHub-profile kit

`profile-kit` is the reusable form of the theme-aware profile built for [drsamonline/drsamonline](https://github.com/drsamonline/drsamonline). The live profile is bespoke — its hero art and metrics palette are drawn for one person — so its parts were packaged into a small kit with nothing person-specific baked in: a **hero banner**, a **metrics card** and a **README generator**. It exists so the same profile can be adopted again (by another account, or a fresh one) by copying the kit and filling in the blanks, rather than re-deriving the whole [Theme-aware GitHub profile](../theme-aware-github-profile/SKILL.md) method.

## When to use

- You want a theme-aware, self-updating GitHub profile without re-deriving the method.
- You are starting a profile repository (`<owner>/<owner>`) and want the hero banner, the metrics card and the README generator in place from the first commit.
- You want the profile conventions (light/dark, marker blocks, commit-only-on-change) applied consistently.

## Method

1. Copy the kit into the **profile** repository — the repository named after the account owner, whose `README.md` GitHub renders as the profile.
2. Supply the account-specific parts the kit leaves to you: the light and dark hero art, and the metrics palette values. The kit supplies the structure (the `<picture>` pairs and the marker blocks); the artwork and the palette are yours.
3. Add the `METRICS_TOKEN` secret (a classic personal access token with no scopes) so the metrics render can read the fields its base query requests; without it the card renders empty while the action still reports success.
4. Let the README generator and its workflow do the maintenance: on schedule it renders the light and dark metrics cards and regenerates the badge row and the categorised project list from the GitHub API between the marker blocks, committing only when something changed.
5. Keep the kit's restraint rules: no emoji headings, a small badge set, one idea per section, and no pure black or pure white.

## Key files / entry points

- `README.md` — defines the kit: a hero banner, a metrics card and a README generator for a theme-aware, self-updating profile.
- The kit's three parts are adopted into the profile repository per the method above; the layout mirrors the live `drsamonline` profile.

## Gotchas

- The kit is structure, not content — the hero art and the metrics palette are deliberately left for the adopter, or every profile built from it would look identical.
- `${{ secrets.GITHUB_TOKEN }}` cannot read the `stargazers` field the metrics base query requests; the render fails with `FORBIDDEN: Resource not accessible by integration` and silently empties the `plugin_languages` panel while the action reports success. Use a classic PAT with no scopes saved as `METRICS_TOKEN`.
- `config_theme` is not a real metrics option and does nothing — theme control lives in the template and `extras_css`.
- GitHub sanitises `<style>` in a README, so `<picture>` is the only light/dark hook; a media query in a `<style>` block will not work.
- The kit must be copied into the **profile** repo (the one named after the owner), not an ordinary project repo, or GitHub will not render it as a profile.

## Source projects

- [profile-kit](https://github.com/drsamonline/profile-kit) — the reusable kit itself: a hero banner, a metrics card and a README generator.
- [drsamonline](https://github.com/drsamonline/drsamonline) — the live profile the kit was extracted from.
