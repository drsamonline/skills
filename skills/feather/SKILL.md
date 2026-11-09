---
name: feather
description: Structure a small portable document viewer in Rust as one crate per format plus a core, and gate the GUI work on a measured answer to the only question that matters: how long does it take to open a document and draw page one.
metadata:
  title: "Feather"
---

# Feather — prove the engine path before writing the window

Feather is a read-only document viewer: one window, one document, summoned by a keystroke, no editing, no annotation, no cloud, no plugins. The repository is at **M0 — the spike**, and the shape of that milestone is the reusable part.

## When to use

- You are starting a native desktop tool in Rust and want the crate boundaries decided before the UI exists.
- The product's promise is speed, so the first milestone must be a measurement, not a window.
- You need one code path per file format with a single router in front of them.

## Method

1. Split by responsibility into crates: `feather-core` (the model), one per format (`feather-pdf`, `feather-epub`, `feather-image`, `feather-text`, `feather-sheet`, `feather-slide`), then `feather-app` and `feather-cli`.
2. Route by **extension and magic bytes** in the core, so a mislabelled file still opens correctly and the router is testable without a window.
3. Answer the plan's first question with code before UI: how long to open a document and draw page one. The repository states the spike exists because that question comes before "does it look good".
4. Keep packaging per platform under `packaging/{linux,macos,windows}` rather than inventing one portable script.
5. Run the tests in `tests/` and the badges under `docs/assets/` as the CI surface.

## Key files / entry points

- `crates/feather-core` — the model and the format router.
- `crates/feather-pdf`, `-epub`, `-image`, `-text`, `-sheet`, `-slide` — one format each.
- `crates/feather-app`, `crates/feather-cli` — the two front ends.
- `packaging/` — per-platform packaging.
- `ROADMAP.md`, `docs/plan.html` — the milestone plan.

## Gotchas

- A viewer that also edits is a different product; the read-only constraint is what keeps the format crates small.
- Extension alone is not enough — magic bytes are what make the router honest.
- The spike is a deliverable, not a delay: skipping it is how a GUI gets built on an engine that is too slow to use.
- `LICENSE-UNRAR` exists because the unrar path carries its own licence; it is not the project's licence.

## Source projects

- [feather](https://github.com/drsamonline/feather) — the crate split, the format router and the M0 measurement.
