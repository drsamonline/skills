---
name: search-kit-ranked-search
description: Ranked search over a big corpus in one zero-dependency file: an inverted index with prefix and fuzzy matching, scored hits and a vocabulary size.
metadata:
  title: "Ranked search over a big corpus"
---

# Ranked search over a big corpus

`search-kit` is the search a single-file app can afford: build an inverted index
over the corpus once, then answer a query with ranked hits, prefix matches and
fuzzy tolerance — in memory, offline, with no dependency.

## When to use

- An app carries thousands of records (rubrics, remedies, poems, notes) and the
  user expects instant ranked results as they type.
- You want typo tolerance and prefix matching without a search service.
- The corpus is static enough to index at load or at build time.

## Method

1. Index the documents once, at startup or at build time; keep the index in
   memory for the session.
2. Query it and rank the hits by the kit's score; show the score's order, not
   insertion order.
3. Use prefix matching for the as-you-type path and fuzzy matching only on a
   submit, so a slow query never runs on every keystroke.
4. Cap the result list and the vocabulary you keep — the index is a memory cost
   the user's phone pays.
5. For a corpus that never changes, ship a prebuilt index file (as
   `open-materia-medica` does with its 665 KB `search-index.js`) instead of
   indexing on load.

## Key files

- `search-kit.js` — index build, query, scoring, prefix/fuzzy matching,
  vocabulary size.
- `test-node.js` — ranking behaviour over a small fixture corpus.

## Gotchas

- The index lives in memory. A very large corpus wants a prebuilt index or a
  worker, not a bigger array.
- Search is not ranking by meaning: `ml-kit`'s tf-idf/cosine is the other tool,
  and mixing the two scores produces an order nobody can explain.
- `app-poets-studio`'s 124k-word dictionary is a different problem (rhyme and
  metre, not lookup); do not point this kit at it and expect a rhyme engine.
- `app-poets-studio` and `app-encrypted-case-log` vendor the kit; the big
  readers (`open-materia-medica`, the two repertories) still ship their own
  search.

## Source projects

- [search-kit](https://github.com/drsamonline/search-kit) — the index and ranking.
- [app-poets-studio](https://github.com/drsamonline/app-poets-studio) — rhyme, metre and fixed forms over a 124,085-word dictionary.
- [app-encrypted-case-log](https://github.com/drsamonline/app-encrypted-case-log) — encrypted case notes with search.
- [open-materia-medica](https://github.com/drsamonline/open-materia-medica) — a prebuilt 665 KB search index.
