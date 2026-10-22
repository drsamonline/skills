---
name: LEXORA — exact-text compression architecture
description: A text-cleaning and exact-compression system: canonicalize documents conservatively, then compress with guaranteed byte-exact recovery (decode(encode(C)) == C), on low-resource hardware.
---

# LEXORA — exact-text compression architecture

LEXORA is a text-cleaning and exact-compression system for document collections (TXT, PDF, optionally OCR'd scans). It ingests files, canonicalizes the extracted text conservatively into deterministic UTF-8 bytes (this step *may* be lossy relative to the source), then compresses those canonical bytes with guaranteed byte-exact recovery: `decode(encode(C)) == C` for every input. Phase-1 prototype, no stable API.

## When to use

- You need a compressor whose correctness is a provable round-trip, not a hope.
- You want to exploit document structure (boilerplate, templates, records, multilingual text) beyond a generic compressor.
- You are designing a versioned, test-vector-driven canonicalization format.

## Method

1. Ingest TXT/PDF (OCR optional); extract text; canonicalize it conservatively and deterministically into UTF-8 bytes, versioned, with golden test vectors.
2. Compress the canonical bytes with a Zstd core baseline behind a `.lxz` v0 container; the invariant is byte-exact recovery after canonicalization.
3. Verify every round trip in tests (`pytest -q`) and run a link check before each commit; keep a benchmark harness with a committed corpus and provenance (`benchmarks/`).
4. Track status honestly: `docs/STATUS.md` states what is verified; badges note that GitHub Actions runs are paused and that the 'tests' badge is a static snapshot.
5. Ship a CLI app and experimental PySide6 GUI milestones (M1–M3).
6. Keep the blueprint/design docs (`LEXORA_Full_Blueprint_Design_Master_Prompt.md`, Batches A–E) alongside the code.

## Key files / entry points

- `Cargo.toml`/Python package + CLI app entry points.
- `benchmarks/harness.py`, `benchmarks/corpus.py`, `benchmarks/results-r*.json`, `benchmarks/provenance/`.
- `docs/STATUS.md` — the verified state.
- `.github/workflows/ci.yml`.

## Gotchas

- Canonicalization may lose information relative to the source *by design*; compression after canonicalization must never lose a byte. Do not blur the two.
- Never claim a compression ratio you have not measured on the committed corpus — publish the real numbers.
- Be honest about paused CI and static badges; do not imply a live green build that is not running.
- Low-resource target (~4 GiB RAM) constrains algorithm choice — test on modest hardware.

## Source projects

- [lexora](https://github.com/drsamonline/lexora) — MIT, Python 3.12, Phase-1 prototype.

