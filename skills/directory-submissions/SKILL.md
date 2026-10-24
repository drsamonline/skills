---
name: directory-submissions
description: Submit a project to a directory or an "awesome" list — a link, not a storefront — so people and AI engines can find it. Use when listing an app in a directory, a local-first or single-file-tools collection, or writing the one-line description and topics a listing needs.
metadata:
  title: "Directory submissions"
---

# Directory submissions

A directory submission is a link, not a storefront. It exists to be found by someone searching for what the app does — and by the AI engines that read those lists — and it only works when the page it points at is already good.

## When to use

- Listing a project in a directory, an "awesome" list, or a curated collection.
- A project needs a one-line description, a category and a set of topics for a listing form.
- Deciding whether a project qualifies for a given directory at all.

## Method

1. **Qualify before submitting.** Read the directory's stated criteria and check the project against every one. `awesome-singlefile-tools` requires single-file · local-first · zero critical CDNs · no analytics or telemetry; `tinytools.directory` wants small, free, artful tools. If the project does not meet the criteria, do not submit it — a rejected or off-criteria submission wastes the one first impression.
2. **Foundation before submission.** The page the link points at must already be live and indexed, with the SEO head the house already ships (a single `<h1>`, canonical, OG/Twitter, JSON-LD, sitemap) — see `static-landing-page-seo`. A directory that indexes a page with no head gives the link nothing to land on.
3. **Set the topics first.** Directories discover by topic, and most of our repos carry none. A repo with no topics is invisible to a topic-driven directory, so set 3-8 real topics before submitting.
4. **Position per directory type.** Do not copy one description everywhere. A single-file-tools list wants the single-file angle; a local-first list wants offline and no-server; a developer list wants the technical depth. Write one honest sentence per audience.
5. **Submit the link.** Point the directory at the project's landing page (or its source), never at a shop. There is no external storefront — Matneo is the store, and a listing is a link to the project.
6. **Record it.** Keep a row per submission: directory, date, the URL used, and its status. A listing nobody tracks is a listing nobody re-checks.
7. **Verify the link.** Once it is live, open the directory page and confirm the link resolves and the description is the one you wrote.

## Key files / entry points

- The project's `docs/index.html` — the page the listing points at.
- The repository's topics (GitHub repo settings) — the directory's discovery surface.
- The submission tracker — one row per directory.

## Gotchas

- **Never invent a link or a claim.** Buy links and store links come from the owner.
- Topics are set through a separate API call, not in a file — a repo can look "done" and still carry none.
- Do not submit the same description to every directory; duplicate descriptions are penalised and each audience wants its own framing.
- A directory carries no fee, revenue share or gatekeeper — if one asks for those, it is not the kind of listing this rule is about.

## Source projects

- [drsamonline.github.io](https://github.com/drsamonline/drsamonline.github.io) — the hub a listing would point at.
- [forge](https://github.com/drsamonline/forge) — the `submit: listings` queue item and the topics rule.

*Adapted from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT), rewritten for this system.*
