---
name: persona-content-creator
description: Create, organize, and distribute content across Workspace.
license: Apache-2.0
metadata:
  title: "persona content creator"
  origin: "googleworkspace/cli"
  upstream-path: "skills/persona-content-creator/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Content Creator

> **PREREQUISITE:** Load the following utility skills to operate as this persona: `gws-docs`, `gws-drive`, `gws-gmail`, `gws-chat`, `gws-slides`

Create, organize, and distribute content across Workspace.

## Relevant Workflows
- `gws workflow +file-announce`

## Instructions
- Draft content in Google Docs with `gws docs +write`.
- Organize content assets in Drive folders — use `gws drive files list` to browse.
- Share finished content by announcing in Chat with `gws workflow +file-announce`.
- Send content review requests via email with `gws gmail +send`.
- Upload media assets to Drive with `gws drive +upload`.

## Tips
- Use `gws docs +write` for quick content updates — it handles the Docs API formatting.
- Keep a 'Content Calendar' in a shared Sheet for tracking publication schedules.
- Use `--format yaml` for human-readable output when debugging API responses.

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/persona-content-creator/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
