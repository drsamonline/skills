---
name: ctx-upgrade
description: Pull latest from GitHub and reinstall the plugin.
license: see LICENSE
metadata:
  title: "ctx upgrade"
  origin: "mksglu/context-mode"
  upstream-path: "skills/ctx-upgrade/SKILL.md"
  upstream-commit: "49b318b5b894d286cda891732287400d9b43cea3"
  category: "engineering-workflow"
  description-source: "derived from the body — upstream ships no usable description"
---

# Context Mode Upgrade

Pull latest from GitHub and reinstall the plugin.

## Instructions

1. Call the `ctx_upgrade` MCP tool directly. It returns a shell command to execute.
2. Run the returned command using your shell execution tool (Bash, shell_execute, etc.).
3. Display results as a markdown checklist:
   ```
   ## context-mode upgrade
   - [x] Pulled latest from GitHub
   - [x] Built and installed v1.0.39
   - [x] Hooks configured
   - [x] Doctor: all checks PASS
   ```
   Use `[x]` for success, `[ ]` for failure. Show actual version numbers.
4. Tell the user to **restart their session** to pick up the new version.
5. **Fallback** (only if MCP tool call fails): Derive the **plugin root** from this skill's base directory (go up 2 levels — remove `/skills/ctx-upgrade`), then run with Bash:
   ```
   CLI="<PLUGIN_ROOT>/cli.bundle.mjs"; [ ! -f "$CLI" ] && CLI="<PLUGIN_ROOT>/build/cli.js"; node "$CLI" upgrade
   ```

## Provenance

Imported from [mksglu/context-mode](https://github.com/mksglu/context-mode) at commit `49b318b`, path `skills/ctx-upgrade/SKILL.md`. Licensed see LICENSE — the full text is in `LICENSE`.
