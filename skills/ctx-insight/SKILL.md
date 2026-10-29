---
name: ctx-insight
description: Open the hosted Insight dashboard in the user's default browser.
license: see LICENSE
metadata:
  title: "ctx insight"
  origin: "mksglu/context-mode"
  upstream-path: "skills/ctx-insight/SKILL.md"
  upstream-commit: "49b318b5b894d286cda891732287400d9b43cea3"
  category: "engineering-workflow"
  description-source: "derived from the body — upstream ships no usable description"
---

# Context Mode Insight

Open the hosted Insight dashboard in the user's default browser.

## Instructions

1. Call the `ctx_insight` MCP tool (no parameters). It opens
   <https://context-mode.com/insight> in the default browser and returns a
   confirmation line.
2. Display the tool's output to the user.
3. Tell the user:
   - "Insight opened at https://context-mode.com/insight"
   - The landing page at context-mode.com/insight is the single source of truth for sign-in and pricing details.
   - If the browser did not open automatically, share the URL so they can open it manually.

## Provenance

Imported from [mksglu/context-mode](https://github.com/mksglu/context-mode) at commit `49b318b`, path `skills/ctx-insight/SKILL.md`. Licensed see LICENSE — the full text is in `LICENSE`.
