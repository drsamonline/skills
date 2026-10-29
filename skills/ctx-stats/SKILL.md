---
name: ctx-stats
description: Show context savings for the current session.
license: see LICENSE
metadata:
  title: "ctx stats"
  origin: "mksglu/context-mode"
  upstream-path: "skills/ctx-stats/SKILL.md"
  upstream-commit: "49b318b5b894d286cda891732287400d9b43cea3"
  category: "engineering-workflow"
  description-source: "derived from the body — upstream ships no usable description"
---

# Context Mode Stats

Show context savings for the current session.

## Instructions

1. Call the `mcp__context-mode__ctx_stats` MCP tool (no parameters needed).
2. **CRITICAL**: You MUST copy-paste the ENTIRE tool output as markdown text directly into your response message. Do NOT summarize, do NOT collapse, do NOT paraphrase. The user must see the full tables without pressing ctrl+o. Copy every line exactly as returned by the tool.
3. After the full output, add ONE sentence highlighting the key savings metric, e.g.:
   - "context-mode saved **12.4x** — 92% of data stayed in sandbox."
   - If no data yet: "No context-mode calls yet this session."

## Purge

- **`ctx_purge(confirm: true)`** — Permanently deletes all indexed content from the knowledge base. Use `/context-mode:ctx-purge` for this.

## Provenance

Imported from [mksglu/context-mode](https://github.com/mksglu/context-mode) at commit `49b318b`, path `skills/ctx-stats/SKILL.md`. Licensed see LICENSE — the full text is in `LICENSE`.
