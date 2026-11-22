---
name: sourced-claims-archive
description: Publish a large archive of contested claims without endorsing them: every claim attributed to the person who made it, every source linked, every test shown next to the thing it tested, plus a reading guide, search and a single-volume print edition.
metadata:
  title: "LARGE_GLOBE"
---

# LARGE_GLOBE — a sourced archive of hidden-world claims

A sourced reference library of hidden-world claims — the larger globe, the flat disc, the hollow
shell, the ice wall, the inner sun, the sea beneath the sea — plus the giants, dragons, cryptids,
aliens and secret societies said to live in them. Every claim is attributed to the person who made
it, every source is linked, and every test is shown next to the thing it tested.

## When to use

- The material is contested and the page must **report** rather than advocate.
- Volume is the problem: hundreds of entries need a master list, a search and a reading guide, or they are unfindable.
- The output is a book as well as a site — a single-volume print edition from the same sources.

## Method

1. One entry per claim, with the claimant named and the source linked. An unattributed claim does not go in.
2. Put the **test next to the claim**: what would settle it, and what happened when it was tried. That adjacency is the whole editorial position.
3. Build the navigation as data: master list, search index, reading guide, feed — all generated from the same entry records.
4. Offer a single-volume print edition assembled from the same entries, so the archive survives a browser.
5. Keep the tone even: describe what is claimed and by whom, without adjudicating in the headline.

## Key files / entry points

- The entry records (claim, claimant, sources, test).
- `master-list.html`, `search.html`, `reading-guide.html`, `feed.xml` — all generated views.
- `print-edition.html` — the single volume.

## Gotchas

- An archive of contested claims attracts readers who take it as proof: the framing has to be visible on the entry, not only in an about page.
- Attribution is not endorsement, but a page that quotes a claim without its test reads as one.
- Generated views drift from the records unless the build is the only way to edit them.

## Source projects

- [LARGE_GLOBE](https://github.com/drsamonline/LARGE_GLOBE)
