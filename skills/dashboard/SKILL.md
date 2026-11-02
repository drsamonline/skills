---
name: dashboard
description: A static, public status page for a whole repository fleet: data pre-built into JSON by a script, refreshed by a scheduled workflow, with no token in the browser and no server to run.
metadata:
  title: "Public fleet status page"
---

# Public fleet status page

A static page cannot read private repositories from a browser, so the data is **built ahead of time**: `generate.py` produces the JSON, a scheduled workflow commits it, and Pages serves the result. That is the whole architecture, and it is why the page can be public and free while the fleet stays private.

## When to use

- You want a public status page over many repositories without a server or a token in the client.
- You need the page to stay current without a human running anything.
- You want the data contract written down before the page grows.

## Method

1. Generate the data with `generate.py` into the JSON files the page reads: `data.json`, `changes.json`, `community.json`, `history.json`, `forks.json`.
2. Write the contracts down in `DATA_CONTRACTS.md` and keep `SPEC-GAP.json` as the explicit list of what the page does not yet cover.
3. Serve it from `docs/` with `.nojekyll`, `robots.txt`, `sitemap.xml` and a `feed.xml` for the change stream.
4. Refresh on a schedule with `.github/workflows/refresh.yml` and gate the shape with `tests/structure.test.js` (`npm test`) — a page that silently loses a section is worse than one that fails.
5. Keep the app copy at `docs/play/` separate from the landing page at `docs/index.html`; the extra views (`network.html`, `forks.html`) are pages, not tabs inside one file.

## Key files / entry points

- `generate.py` — the data build.
- `data.json`, `changes.json`, `community.json`, `history.json`, `forks.json` — what the page reads.
- `DATA_CONTRACTS.md`, `SPEC-GAP.json` — the contract and the known gaps.
- `.github/workflows/refresh.yml`, `tests/structure.test.js`.

## Gotchas

- A token shipped to the browser to "just read the API" is a published token; build the JSON instead.
- Pages serves `docs/` only when `.nojekyll` is present and the folder is configured as the source.
- A structure test is the only thing that catches a refresh that quietly produced an empty array.
- `history.json` grows forever unless the generator prunes it — decide the window when you write the generator, not later.

## Source projects

- [dashboard](https://github.com/drsamonline/dashboard) — the generated-JSON architecture, the data contracts and the structure test.
