---
name: auto-updating-showcase-hub
description: A single static page that lists every repository by reading the GitHub API at runtime, with an embedded JSON snapshot fallback, a curated map for hand-written copy, and a scheduled workflow that refreshes the snapshot.
metadata:
  title: "Auto-updating showcase hub"
---

# Auto-updating showcase hub

The hub at `drsamonline.github.io` lists all projects with nothing to update by hand. On load it fetches `https://api.github.com/users/drsamonline/repos?per_page=100&sort=updated` and renders a card per repo; a JSON snapshot of the repos is **embedded in the page** and used only when the API is unreachable or rate-limited, so the page is never blank. A curated map keyed by lower-cased repo name supplies hand-written descriptions, categories, feature flags and demo flags, with anything not in the map falling under an automatic 'Other / New' chip.

## When to use

- You maintain many repos and want one index that stays current without manual edits.
- You need the page to degrade gracefully when the unauthenticated GitHub API rate limit (60/hr/visitor) is hit.
- New repos should appear automatically, with hand-written copy for the ones you care about.

## Method

1. Fetch the owner's repos at runtime with the `Accept: application/vnd.github+json` header; filter out forks and the site's own repos; cache the result in `sessionStorage` for ~10 minutes to stay inside the rate limit.
2. Embed a snapshot: put `<script id="repo-snapshot" type="application/json">[...]</script>` between `<!--REPO_SNAPSHOT_START-->` / `<!--REPO_SNAPSHOT_END-->` markers. Render immediately from the snapshot, then re-render if the live fetch succeeds; on any fetch error keep the snapshot render.
3. Keep a `CURATED` object keyed by lower-cased repo name, each value carrying `cat`, `desc`, `demo`, `feat`, `rel`, and optional `kicker`/`tag`. Merge curated fields over the API data; fall back to the API description and an `other` category when absent.
4. Define category labels and a fixed order, a `FEATURED` pin list, and a language-colour map for chips. Show stars, language, last-updated ('today'/'3d ago'), archived state, and buttons for landing/demo/code/downloads.
5. Constrain network access with a Content-Security-Policy meta tag: `default-src 'none'`, `img-src https: data:`, `style-src 'unsafe-inline'`, `script-src 'unsafe-inline'`, `connect-src https://api.github.com`, `base-uri 'none'`, `form-action 'none'`, `object-src 'none'`.
6. Add a weekly workflow (`.github/workflows/refresh-hub.yml`, cron + `workflow_dispatch`, `permissions: contents: write`) that re-reads the repos from the API with the `GITHUB_TOKEN`, rebuilds the snapshot JSON (sorted by `pushed_at` desc, `</` escaped), regex-replaces the marked block in `index.html`, and commits **only if the file changed**.
7. Optionally verify an external service (e.g. the screenshot service) in the same workflow with `continue-on-error` so a third-party outage never fails the refresh.

## Key files / entry points

- `index.html` — the hub: inline `<style>`, the embedded snapshot block, and the `CURATED`/`CAT_LABEL`/`FEATURED` config plus the render + fetch logic.
- `.github/workflows/refresh-hub.yml` — the scheduled snapshot refresh (Python `urllib` + `re.sub` + conditional commit).
- `README.md` — documents `USER`, `EXCLUDE`, `FEATURED`, `CACHE_TTL`.

## Gotchas

- The embedded snapshot must be valid JSON inside a `<script type="application/json">`; escape `</` as `<\/` so the payload can never close the tag.
- Never let the live fetch being blocked leave the page empty — always render the snapshot first.
- The CSP must allow `https://api.github.com` in `connect-src` and inline script/style, or the page silently stops updating.
- Curated keys are lower-cased repo names; a mismatch quietly drops your hand-written description.
- Commit only when the snapshot actually changed, or you get a noisy commit every week.

## Source projects

- [drsamonline.github.io](https://github.com/drsamonline/drsamonline.github.io) — the live hub with the embedded snapshot, curated map and weekly refresh workflow.

