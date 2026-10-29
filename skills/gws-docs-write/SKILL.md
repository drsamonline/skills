---
name: gws-docs-write
description: Google Docs: Append text to a document.
license: Apache-2.0
metadata:
  title: "gws docs write"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-docs-write/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# docs +write

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Append text to a document

## Usage

```bash
gws docs +write --document <ID> --text <TEXT>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--document` | ✓ | — | Document ID |
| `--text` | ✓ | — | Text to append (plain text) |

## Examples

```bash
gws docs +write --document DOC_ID --text 'Hello, world!'
```

## Tips

- Text is inserted at the end of the document body.
- For rich formatting, use the raw batchUpdate API instead.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-docs](../gws-docs/SKILL.md) — All read and write google docs commands

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-docs-write/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
