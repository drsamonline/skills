---
name: ctx-index
description: Index local project content for later search.
license: see LICENSE
metadata:
  title: "ctx index"
  origin: "mksglu/context-mode"
  upstream-path: "skills/ctx-index/SKILL.md"
  upstream-commit: "49b318b5b894d286cda891732287400d9b43cea3"
  category: "engineering-workflow"
  description-source: "derived from the body — upstream ships no usable description"
---

# Context Mode Index

Index local project content for later search.

## Instructions

1. Prefer the `ctx_index` MCP tool when it is available.
2. Ask for a path only if the user did not provide one and the current project root is ambiguous.
3. Use `path`, not large inline `content`, so file bytes do not enter the conversation.
4. For repository indexing, pass conservative bounds and a clear source label:

```javascript
ctx_index({
  path: ".",
  source: "project:<name>",
  maxDepth: 5,
  maxFiles: 200
})
```

5. If MCP tools are unavailable, fall back to the CLI:

```bash
context-mode index . --source project:<name>
```

6. Report the indexed source label, file count or section count, and the matching search command:

```javascript
ctx_search({ source: "project:<name>", queries: ["..."] })
```

## Safety

- Do not index dependency directories, build outputs, secrets, or generated artifacts.
- Prefer `--exclude` or `exclude` for project-specific noisy paths.
- For broad repos, ask the user before raising `maxFiles` above 500.

## Provenance

Imported from [mksglu/context-mode](https://github.com/mksglu/context-mode) at commit `49b318b`, path `skills/ctx-index/SKILL.md`. Licensed see LICENSE — the full text is in `LICENSE`.
