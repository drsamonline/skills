---
name: browser-compression-with-measured-claims
description: Ship a compression tool whose README numbers are generated from a measured corpus and fail the build when they drift — Brotli in a WebAssembly worker and a portable CLI, with the honest table that says where it loses.
metadata:
  title: "Faztest"
---

# Faztest — a Brotli front end with claims that can be checked

A Brotli front end for files you would rather not upload: compress and decompress in the browser
(WebAssembly workers, nothing leaves the machine) or from a portable CLI. The distinguishing part
is not the codec — it is that the performance table is measured, published, and enforced.

## When to use

- A tool makes a **performance claim** and you want the claim to be checkable rather than aspirational.
- Compression has to happen on the user's machine because the file is private.
- The same engine has to run in a page and in a shell, so the browser is not a special case.

## Method

1. Measure on a **named public corpus** (Silesia, twelve files, ~212 MB), one run per cell, and decode every archive back and compare byte for byte. A ratio without a round-trip check is a guess.
2. Publish the full tables in `docs/FINDINGS.md` and make it the authority; the README quotes it and nothing else.
3. Add `scripts/check-claims.py` to CI: if the README table and FINDINGS disagree, the build fails. This is the part most projects skip.
4. State where you **lose**: Brotli at `-q5` is about three times xz's speed for 23% more bytes; it does not beat xz or 7z on size at any setting. Saying so is what makes the wins credible.
5. Run the codec in a WebAssembly worker in the browser and as `public/faztest.mjs` in the shell — one implementation, two front ends.

## Key files / entry points

- `public/faztest.mjs` — the CLI (`compress`, `decompress`, `-q`).
- `docs/FINDINGS.md` — the measurement, method and caveats.
- `scripts/check-claims.py` — the CI guard that keeps the README honest.

## Gotchas

- This README **used to claim** it beat xz. The measurement said otherwise, and the correction is now part of the documentation — a benchmark you have not re-run is a claim you are still making.
- Wall-clock times from different machines are not comparable; the corpus, the core and the run count belong next to every number.
- A browser worker has no filesystem: the CLI and the page must share the codec, not the I/O.

## Source projects

- [faztest-fast-file-forge](https://github.com/drsamonline/faztest-fast-file-forge)
