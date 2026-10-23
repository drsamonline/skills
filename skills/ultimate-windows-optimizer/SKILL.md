---
name: ultimate-windows-optimizer
description: A PowerShell + batch toolkit that applies documented, fully reversible Windows 10/11 debloat and performance tweaks, with real logging, real registry/service backups and a one-shot undo.
metadata:
  title: "Ultimate Windows Optimizer"
---

# Ultimate Windows Optimizer

A PowerShell + batch toolkit that wires up well-known Windows tweaks (telemetry, CPU priority separation, GPU scheduling, power plans, visual effects) into profiles, with real logging to `%USERPROFILE%\OptimizationLogs`, real backups of every registry value and service state changed, and an `Undo-All-Changes.ps1` that restores the system. It makes no outbound calls and sends no telemetry.

## When to use

- You are applying a Windows tweak and need it to be reversible and logged.
- You want a PowerShell toolkit structured as a menu + profiles with Pester tests.
- You need to verify a change actually took effect rather than printing a canned result.

## Method

1. Structure the toolkit as a master batch menu (`scripts/00_Ultimate_Master.bat`) plus PowerShell modules (`Advanced-Modules.ps1`) and per-profile scripts.
2. Before every change, back up the affected registry value or service state so the undo script can restore the exact prior state; log actions to `%USERPROFILE%\OptimizationLogs`.
3. Provide `Undo-All-Changes.ps1` to reverse everything, and `Cleanup-Backups.ps1` to prune old backups.
4. Ship verification and benchmarking utilities (`Performance-Monitor.ps1`, `Compare-Results.ps1`) that measure the machine before and after instead of promising a percentage.
5. Test with Pester 5; run `PSScriptAnalyzer` with `PSScriptAnalyzerSettings.psd1`; CI in `.github/workflows/ci.yml`.
6. Ship the landing page in `docs/` (with SVG screenshots) and a `QUICK_START.txt`.
7. Never make a network call and never claim a specific speed-up — results depend on hardware and workload.

## Key files / entry points

- `scripts/00_Ultimate_Master.bat` — the master menu.
- `scripts/Advanced-Modules.ps1`, `scripts/Undo-All-Changes.ps1`, `scripts/Cleanup-*.ps1`, `scripts/Performance-Monitor.ps1`, `Compare-Results.ps1`.
- `PSScriptAnalyzerSettings.psd1`, `tests/` (Pester 5).
- `.github/workflows/ci.yml`.
- `docs/index.html` — the landing page; `docs/images/*.svg`.

## Gotchas

- Reversibility is the contract: if you change a registry value or service without backing it up, the undo script is a lie.
- Do not promise a performance multiplier anywhere; measure and report the user's own before/after.
- Keep the toolkit offline — no downloads, no telemetry, no credential reads.
- Some tweaks need elevation; handle the non-admin case with a clear message rather than a half-applied change.

## Source projects

- [ULTIMATE-WINDOWS-OPTIMIZER](https://github.com/drsamonline/ULTIMATE-WINDOWS-OPTIMIZER) — v6.2.0, BSD-3-Clause, PowerShell + batch with Pester tests.

