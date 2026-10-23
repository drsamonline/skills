---
name: all4one-utility-suite
description: 551 Windows tools across 45 plugin packs compiled into one self-contained portable utility_suite.exe (Python, tkinter GUI + CLI) — an embedded bundle with per-pack enable/disable, guided dependency gating and an audit that verifies every tool.
metadata:
  title: "All4ONE — portable Windows utility suite"
---

# All4ONE — portable Windows utility suite

Utility Suite is a free, portable Windows toolbox: file ops, hashing, PDF/Office batch, image/audio/video, network diagnostics, registry helpers, disk cleaning and security audits — 551 tools across 45 plugin packs, shipped as a single self-contained `utility_suite.exe` you can keep on a USB stick. Zero installs, zero telemetry, MIT licensed, with a tkinter GUI and a CLI over one engine. The release is **one** download, `UtilitySuite-<v>-windows.zip` (the exe plus a short `README-FIRST.txt`); there are deliberately no separate pack downloads, no lite/full split and no pack manifest.

## When to use

- You want to add a Windows utility to a large, well-organised portable toolkit rather than start a new repo.
- You need a pattern for shipping many features in one binary and letting users turn individual packs on or off without rebuilding.
- You want to tell users honestly when a feature needs an external program the machine does not have, offer a guided install, and let them disable that pack instead if they decline.
- You want to ship a big Python app as one unsigned portable EXE built in CI.

## Method

1. Organise tools into domain packages (plugin packs), each exporting handlers. Register every tool with metadata (id, name, category, declared optional dependencies) so the catalogue is data-driven.
2. Compile all 45 packs / 551 tools into one deterministic archive, `bundle/tools.dat`, with `core/bundle.py::build_bundle()`. Embed it into `utility_suite.exe` via PyInstaller `datas` in `build_onefile.spec`; at runtime `core/bundle.py::get_bundle_path()` locates it under `_MEIPASS` and adds it to `sys.path`, so handlers resolve from the archive via `zipimport`. One artefact, no external files to ship.
3. Build the registry with a fixed merge precedence (`core/cli.py::build_registry()`): the external `plugins/` directory **first** (a user-installed pack overrides the embedded copy of the same pack), then the embedded bundle as the baseline for any `cli_command` not already registered, then a source-tree scan as a dev-only fallback. First registration for a given `cli_command` wins — that is what gives external packs precedence.
4. Persist per-pack enable/disable as an explicit **disabled** list in `core/preferences.py`, written atomically to the user config directory (`%APPDATA%\UtilitySuite\preferences.json` on Windows) and never into the install directory. An empty list means every pack is enabled, so an existing install is unchanged and a pack added by a future update defaults to on.
5. Expose the gating API from `core/tool_registry.py`: `enabled_packs()`, `is_pack_enabled()`, `set_pack_enabled()`, `pack_summaries()`. A disabled pack's tools are excluded from `search()`/`list_categories()`, `get_tool()` returns `None`, and `run_tool()` returns exit code 4 with a message telling the user which pack to enable.
6. Gate availability on external dependencies with a **closed** catalogue (`core/dependencies.py`, exactly the 27 external programs the 45 packs really declare). `check(dep)` reports presence/version; `install_plan(dep)` returns an ordered, honest plan: already on PATH → the Windows built-in → `pip install` → a package-manager command the user runs (`winget install --id Gyan.FFmpeg -e`, `choco install ffmpeg -y`) → the official vendor page over HTTPS. **Nothing auto-downloads or executes anything**, and a missing dependency keeps the tool marked unavailable — the user can decline and disable the pack in one click instead.
7. Front it with a tkinter GUI (`core/gui.py`) — a Tools tab and a **Packs** view (per-pack title, tool count, runnable count, enabled toggle, "Get dependencies") — and a CLI (`core/cli.py`, commands `list`, `search`, `run`, `packs`, `deps`) over the same engine.
8. Make GUI controls conditional on optional per-tool metadata `accepts` (`file`|`folder`|`text`|`none`), `produces` (`file`|`text`|`none`) and `destructive` (bool). Absent metadata preserves the old behaviour of showing every control; 316 of 551 tools have it populated and the rest are left unset rather than guessed.
9. Verify with `audit.py` (45 packs / 551 tools / 551 unique commands / 551 handlers resolved) plus six test modules: the smoke suite, the registry merge, a headless fake-tkinter GUI harness, the pack enable/disable behaviour, the dependency catalogue, and the tool metadata.
10. Build the EXE in CI on `windows-latest` (`.github/workflows/build-windows-exe.yml`), regenerating the bundle before PyInstaller runs; Linux-side validation runs on every push. Release the single zip through GitHub Releases.

## Key files / entry points

- `core/bundle.py` — `build_bundle()` compiles `bundle/tools.dat`; `get_bundle_path()` locates it under `_MEIPASS` at runtime.
- `build_onefile.spec` — embeds `bundle/tools.dat` into the exe via PyInstaller `datas`.
- `core/cli.py` — `build_registry()` (the merge precedence) and the `list` / `search` / `run` / `packs` / `deps` commands.
- `core/preferences.py` — the disabled-pack list, written atomically to the user config directory.
- `core/tool_registry.py` — `enabled_packs()`, `is_pack_enabled()`, `set_pack_enabled()`, `pack_summaries()`.
- `core/dependencies.py` — the closed dependency catalogue; `check()` and `install_plan()`.
- `core/gui.py` — the tkinter Tools tab and Packs view.
- `audit.py` — registry verification (45 packs / 551 tools / 551 handlers).
- `.github/workflows/build-windows-exe.yml`, `.github/workflows/ci.yml`.

## Gotchas

- **PyInstaller cannot cross-compile a Windows EXE from Linux**, so the exe must be built on `windows-latest`.
- **The GUI cannot be verified without a display**, so a headless fake-tkinter harness is the only automated guard.
- **The exe is unsigned** — SmartScreen warns on first run. Document 'More info → Run anyway'.
- **A missing optional dependency must disable exactly one tool, never the suite.** Graceful degradation is the whole point of the metadata registry.
- **The user preference must never be written into the install directory**, which may be read-only and is replaced by an update; keep it in the user config directory.
- **The bundle must be regenerated before PyInstaller runs**, or the exe ships with zero tools — the build now fails loudly if it does.
- Zero telemetry and no background services are promises in the README; do not add an updater that phones home.

## Source projects

- [All4ONE](https://github.com/drsamonline/All4ONE) — the utility suite repo: 551 tools across 45 packs, shipped as one self-contained `utility_suite.exe` (one zip release, no pack downloads).
