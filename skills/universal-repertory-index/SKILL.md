---
name: universal-repertory-index
description: Index several classical homeopathic repertories into one search surface: normalise the books into a common record shape, keep the policy documents in the repository, and run the app where it can actually be hosted.
metadata:
  title: "UniRep"
---

# UniRep — one search surface over several repertories

The repertory, indexed: a single searchable index across the classical repertories. This repository
holds the **policy documents** and the index work; the app itself runs on Replit.

## When to use

- Several source books overlap in vocabulary and you need one query to reach all of them.
- The books disagree in structure (chapters, rubrics, grades) and a common record shape has to be decided before any search is possible.
- The runtime cannot live on a static host, so the repository carries the method and the app lives elsewhere.

## Method

1. Write the **policy first**: what counts as a rubric, how grades map between books, what is merged and what is kept distinct. This is `docs/` work, not code work.
2. Normalise each book into one record: rubric text, chapter path, grade, source book, source location.
3. Index the normalised records for search (prefix and fuzzy), and keep the original wording as a field rather than as the index key.
4. Keep the audit (`docs/AUDIT.md`) next to the guide (`docs/GUIDE.md`) — what was normalised, and what was left alone.
5. Run the app where it can be hosted (Replit) and keep this repository as the source of truth for the data and the rules.

## Key files / entry points

- `docs/GUIDE.md` — how the index is built and queried.
- `docs/AUDIT.md` — what the normalisation changed.
- `app/` — the running app.

## Gotchas

- Normalising two books' grades into one scale is a **claim** about equivalence; write it down where a reader can disagree with it.
- A search index over rubrics must not lose the chapter path — a rubric without its hierarchy is ambiguous.
- If the app runs elsewhere, the repository still has to be runnable locally, or the method cannot be checked.

## Source projects

- [UniRep](https://github.com/drsamonline/UniRep)
