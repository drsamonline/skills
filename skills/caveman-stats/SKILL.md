---
name: caveman-stats
description: In Claude Code, src/hooks/caveman-mode-tracker.js resolves src/hooks/caveman-stats.js next to itself and runs it on /caveman-stats. The hook does not block the prompt: it supplies the report through hookSpecificOutput.additionalContext with an instruction to print it verbatim inside a fenced code block. Do exactly that, and do not calculate, recompute or re-round the numbers yourself.
license: Apache-2.0
metadata:
  title: "caveman stats"
  origin: "JuliusBrussee/caveman"
  upstream-path: "skills/caveman-stats/SKILL.md"
  upstream-commit: "9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4"
  category: "engineering-workflow"
  description-source: "derived from the body — upstream ships no usable description"
---

In Claude Code, `src/hooks/caveman-mode-tracker.js` resolves `src/hooks/caveman-stats.js` next to itself and runs it on `/caveman-stats`. The hook does not block the prompt: it supplies the report through `hookSpecificOutput.additionalContext` with an instruction to print it verbatim inside a fenced code block. Do exactly that, and do not calculate, recompute or re-round the numbers yourself.

In Gemini CLI, direct the user to `/stats model` for current session token usage or `/stats session` for session statistics. Gemini custom commands are prompts; they cannot invoke the built-in command or read its live session metrics. Never read Claude Code transcripts as Gemini usage. In other hosts, use a native usage report if one is available; otherwise say that current session usage is unavailable. The Claude reader and its lifetime history apply only to Claude Code. Savings remain unknown in every host without a measured comparison.

The report shows recorded output and cache-read tokens, response counts, and mode attribution where available. Savings are unknown: the transcript has no measured comparison without Caveman. Do not infer saved tokens, percentages, dollars, rule overhead, or a net result from output counts or the current mode.

`--all` and `--since 7d` aggregate the latest recorded output count per session. `--share` reports observed usage with savings unknown. Historical `est_saved_*` fields are ignored; their original history rows remain on disk. The statusline shows the active mode without the retired savings badge.

Original/current memory-file pairs are reported by their measured byte sizes. Those file-size differences do not establish provider token or billing savings. See `docs/HONEST-NUMBERS.md`.

## Provenance

Imported from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) at commit `9b68f7e`, path `skills/caveman-stats/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
