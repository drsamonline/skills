---
name: ctx-doctor
description: Run diagnostics and display results directly in the conversation.
license: see LICENSE
metadata:
  title: "ctx doctor"
  origin: "mksglu/context-mode"
  upstream-path: "skills/ctx-doctor/SKILL.md"
  upstream-commit: "49b318b5b894d286cda891732287400d9b43cea3"
  category: "engineering-workflow"
  description-source: "derived from the body — upstream ships no usable description"
---

# Context Mode Doctor

Run diagnostics and display results directly in the conversation.

## Instructions

1. Call the `ctx_doctor` MCP tool directly. It runs all checks server-side and returns a plain-text status report.
2. Display the results verbatim — they are already formatted with plain-text status prefixes: `[OK]` PASS, `[FAIL]` FAIL, `[WARN]` WARN. Renderer-safe (no markdown task-list syntax) for cross-client compatibility (e.g., Z.ai GLM).
3. **Fallback** (only if MCP tool call fails): Derive the **plugin root** from this skill's base directory (go up 2 levels — remove `/skills/ctx-doctor`), then run with Bash:
   ```
   CLI="<PLUGIN_ROOT>/cli.bundle.mjs"; [ ! -f "$CLI" ] && CLI="<PLUGIN_ROOT>/build/cli.js"; node "$CLI" doctor
   ```
   Re-display results verbatim with the same `[OK]`/`[FAIL]`/`[WARN]` prefixes.

## Provenance

Imported from [mksglu/context-mode](https://github.com/mksglu/context-mode) at commit `49b318b`, path `skills/ctx-doctor/SKILL.md`. Licensed see LICENSE — the full text is in `LICENSE`.
