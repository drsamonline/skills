---
name: embedded-bundle-feature-gating
description: Ship many features in one self-contained binary, compile them into a single embedded archive, and let users turn each feature on or off — while telling them honestly when one needs something the machine does not have.
metadata:
  title: "Embedded bundle with feature gating"
---

# Embedded bundle with feature gating

A reusable pattern for a single self-contained binary that holds many features. Every feature module is compiled into one deterministic archive embedded in the binary and resolved at runtime from the extracted temp directory. Users can turn features on or off without a rebuild, an external module they drop in overrides the embedded baseline, and when a feature needs an external program the machine lacks, the app says so plainly and offers a guided install — or to disable that feature instead. The point is one artefact, honest availability, and no hidden downloads.

## When to use

- You ship one self-contained binary that holds many features, and you want users to turn features on or off **without rebuilding**.
- You want to be told honestly when a feature needs something the machine does not have, and to install it deliberately or disable the feature instead.
- You want a user-supplied external module to override the built-in copy of the same feature, so the app stays extensible without a fork.

## Method

1. **Compile every feature module into one deterministic archive embedded in the binary.** One build step walks the feature packages and writes a single archive (in All4ONE, `bundle/tools.dat` via `core/bundle.py::build_bundle()`); the archive is embedded in the frozen binary and resolved at runtime from the extracted temp directory (`_MEIPASS`), then added to `sys.path` so handlers resolve from it via `zipimport`. No loose files to ship.
2. **Keep a merge order where a user-supplied external module overrides the embedded baseline, and first registration wins.** Register the external directory first, then fall back to the embedded archive for anything not already registered, then (dev-only) a source scan. The first registration for a given key wins — that is what gives the external override precedence.
3. **Persist the user's choice as an explicit *disabled* list in the user config directory.** Store the packs the user turned **off**, not the ones they turned on. An empty list means everything is enabled, so an existing install is unchanged and a feature added by a future update defaults to **on**. Write it atomically, and never into the install directory.
4. **Expose a small gating API** — `enabled()`, `is_enabled()`, `set_enabled()`, `summaries()` (All4ONE's `core/tool_registry.py` names them `enabled_packs()`, `is_pack_enabled()`, `set_pack_enabled()`, `pack_summaries()`). A disabled feature is excluded from search and listing, and running it returns a distinct exit code with a message naming what to enable.
5. **Gate availability on external dependencies with a closed catalogue and an ordered install plan.** The catalogue is exactly the programs the features declare (All4ONE: `core/dependencies.py`, 27 programs). `check(dep)` reports presence/version; `install_plan(dep)` returns an ordered, honest plan: already on PATH → the OS built-in → `pip install` → a package-manager command the user runs → the official vendor page over HTTPS.
6. **Never auto-download or execute a dependency.** The app only ever *prints* a plan and hands the user a command or an HTTPS link; a missing dependency keeps the feature marked unavailable. Any download of a third-party binary is an explicit, confirmed action against an official HTTPS source.
7. **Always offer "disable the feature instead" as the escape hatch.** A user who declines a dependency can turn the feature off in one click rather than being blocked.
8. **Keep the availability state visible in the UI** rather than hiding the feature: show the feature with its status (runnable / needs a dependency), so the user understands what exists and why it is unavailable.

## Key files / entry points

The pattern is demonstrated end-to-end in All4ONE (`core/`):

- `core/bundle.py` — `build_bundle()` compiles the embedded archive; `get_bundle_path()` locates it under `_MEIPASS` at runtime.
- `build_onefile.spec` — embeds the archive into the frozen binary (PyInstaller `datas`).
- `core/cli.py` — `build_registry()`, the merge precedence (external → embedded → dev scan).
- `core/preferences.py` — the disabled-list preference, written atomically to the user config directory.
- `core/tool_registry.py` — the gating API (`enabled_packs()`, `is_pack_enabled()`, `set_pack_enabled()`, `pack_summaries()`).
- `core/dependencies.py` — the closed dependency catalogue; `check()` and `install_plan()`.
- `core/gui.py` — the UI that keeps availability state visible and offers the enable/disable toggle.

## Gotchas

- **The disabled-list inversion (opt-out, not opt-in) is what makes updates safe.** Storing what the user turned *off* means a new feature defaults to on and an existing install is unchanged; storing what they turned *on* would silently switch off every feature added after the user last saved.
- **Writing preferences into the install directory breaks on read-only or updated installs.** The install directory may be read-only and is replaced by an update; keep the preference in the user config directory instead.
- **A missing dependency must degrade one feature, not the whole app.** Availability is per-feature; the suite must stay usable when one feature's external program is absent.
- **Any download of a third-party binary must be an explicit, confirmed action against an official HTTPS source.** Never auto-download or auto-execute a dependency, and never fetch from a non-HTTPS or unofficial mirror.

## Source projects

- [All4ONE](https://github.com/drsamonline/All4ONE) — the 45-pack, 551-tool portable suite where this pattern was built (embedded `bundle/tools.dat`, per-pack enable/disable, guided dependency gating).
