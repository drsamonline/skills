---
name: ml-kit
description: The classic ML algorithms from scratch for offline features — tf-idf ranking, Naive Bayes, k-NN, k-means, PCA, ID3, linear regression, Markov chains and grammar generation. Zero dependencies, single file.
metadata:
  title: "ml-kit — classic algorithms from scratch"
---

# ml-kit — classic algorithms from scratch

## When to use

Rank text, find similar items, cluster, reduce dimensions for a plot, draw a trend
line, or generate text from a corpus or a grammar — all offline, with no model and
no API key. Reach for this instead of a framework.

## Method

Compose the kit instead of a runtime. Every algorithm is small (tens of lines),
reimplemented from the idea, and deterministic where it matters — k-means seeds
from the first k points, and Markov and the grammar take a seed so a generation is
reproducible. Use `tfidf` + `search` for ranking, `NaiveBayes`/`knn`/`id3` to
classify, `kmeans`/`pca2` for structure, `linearRegression` for a trend, and
`markov`/`grammar` to generate.

## Key files

- `ml-kit.js` — the API: `tfidf`/`search`, `NaiveBayes`, `knn`, `kmeans`, `pca2`,
  `id3`/`predict`, `linearRegression`, `markov`/`generate`, `grammar`, `rng`
- `test-node.js` — 22 verified cases (run it before and after any change)

## Gotchas

- **THE BOUNDARY:** this is for ranking, similarity, clustering and simple trend.
  It is **not** a diagnostic or predictive engine, and nothing in it may be used to
  claim a clinical or medical capability.
- One file, zero dependencies, UMD (`module.exports` / `MLKit`), MIT.
- Do not introduce an unseeded RNG — reproducibility is the point.

## Source projects

ml-kit, search-kit
