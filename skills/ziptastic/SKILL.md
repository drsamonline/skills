---
name: ziptastic
description: The CHCE native compression engine as one self-contained C++ binary: preprocessors, a dual-resolution match finder, a joint optimal parser and per-block entropy backends in a single stream format, built with CMake against vendored sources.
metadata:
  title: "Ziptastic — single-binary CHCE engine"
---

# Ziptastic — single-binary CHCE engine

A compression engine that ships as **one binary with the codecs embedded** — no external processes, no network, no model files. It composes preprocessors, a dual-resolution match finder, a joint optimal parser and per-block entropy backends into a single stream format. The source tree is large because the third-party compressors are vendored, not linked at runtime.

## When to use

- You are assembling a compressor that must run as a single self-contained binary.
- You need to vendor upstream C sources reproducibly and prove they have not drifted.
- You want a measured, documented format rather than a pile of tuned constants.

## Method

1. Build with CMake (`CMakeLists.txt`) and keep the vendored compressors out of the main tree — they arrive as submodules pinned in `.gitmodules`, sourced from the `HCS` vault.
2. Document the container explicitly in `docs/FORMAT.md` and the integrity story in `docs/INTEGRITY.md`, so a decoder can be written against the document rather than the code.
3. Record what was measured in `docs/BENCHMARKS.md` and keep the per-codec integration notes next to it (`docs/GZIP_INTEGRATION.md`, `docs/LZ4_MEASURED.md`, `docs/BASE64_MEASUREMENT.md`).
4. Gate the vendored trees with `.github/workflows/vendor-check.yml` — a submodule that silently moves is a supply-chain change.
5. Keep the phase plan in `README.md` current: what is built, what is measured, what is still an experiment (`docs/NUMERIC_RESIDUAL_EXPERIMENT.md`).

## Key files / entry points

- `CMakeLists.txt` — the build.
- `.gitmodules` — the vendored compressor pins.
- `docs/FORMAT.md`, `docs/INTEGRITY.md` — the format contract.
- `docs/BENCHMARKS.md` — the measurement record.
- `.github/workflows/vendor-check.yml` — the vendoring gate.

## Gotchas

- A single-binary claim fails the moment a codec is spawned as a subprocess — vendoring exists to prevent that.
- Vendored C from many upstreams carries many licences; the licence file has to be read per source, not assumed.
- Benchmarks that are not committed as data get re-argued every session; `docs/BENCHMARKS.md` is the argument.
- Submodules pinned by branch instead of commit drift without a diff.

## Source projects

- [ziptastic](https://github.com/drsamonline/ziptastic) — the CMake build, the vendored-source model and the format/integrity documents.
