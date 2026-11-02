---
name: hcs-vendored-source-vault
description: The canonical offline vault of vendored compressor, preprocessor and recompressor sources behind the CHCE engines, with a source catalogue, a submodule policy and an explicit licence-warning section.
metadata:
  title: "HCS — vendored compressor source vault"
---

# HCS — vendored compressor source vault

One repository holds the third-party sources the CHCE engines are built from — compressors, preprocessors, recompressors — pinned as submodules and catalogued in `SOURCES`. The reason it exists is reproducibility: an engine built from a vault can be rebuilt from the vault, and a vault can be audited.

## When to use

- You are building an engine from many upstream C/C++ projects and need one pinned source of truth.
- You need a documented policy for how upstream sources are bumped and added.
- You want licence obligations collected in one place instead of rediscovered per build.

## Method

1. Pin every source as a submodule in `.gitmodules` and record it in the catalogue (`SOURCES`); a source that is copied rather than pinned cannot be bumped safely.
2. Follow the documented bump procedure in the README when moving a source, and the documented "add a new source" procedure when introducing one.
3. Keep the older vendored trees under `old/<project>/` rather than deleting them — the engine may still build against one.
4. Read the licence-warning section before shipping: the vault mixes licences and at least one class of source carries obligations that affect distribution.
5. Verify the vault with `scripts/check-vendor.sh` and gate it in `.github/workflows/vendor-check.yml`; a submodule that moved without a check is an unreviewed change.
6. Keep `PROJECT_OVERVIEW.md` describing how the vault relates to the engines that consume it.

## Key files / entry points

- `.gitmodules` — the pins.
- `SOURCES` — the catalogue.
- `scripts/check-vendor.sh`, `.github/workflows/vendor-check.yml` — the gate.
- `old/<project>/` — superseded vendored trees.

## Gotchas

- A submodule pinned to a branch is not pinned; pin the commit.
- Vendored source carries its own licence file, and a parent LICENSE does not override it.
- `old/` trees still count as distribution — removing them is a licensing decision, not a cleanup.
- A vendor check that only verifies the submodule exists will not catch a source that moved within its own history.

## Source projects

- [HCS](https://github.com/drsamonline/HCS) — the submodule policy, the source catalogue and the licence warnings.
