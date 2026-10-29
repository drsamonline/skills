---
name: gws-script-push
description: Google Apps Script: Upload local files to an Apps Script project.
license: Apache-2.0
metadata:
  title: "gws script push"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-script-push/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# script +push

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Upload local files to an Apps Script project

## Usage

```bash
gws script +push --script <ID>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--script` | ✓ | — | Script Project ID |
| `--dir` | — | — | Directory containing script files (defaults to current dir) |

## Examples

```bash
gws script +push --script SCRIPT_ID
gws script +push --script SCRIPT_ID --dir ./src
```

## Tips

- Supports .gs, .js, .html, and appsscript.json files.
- Skips hidden files and node_modules automatically.
- This replaces ALL files in the project.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-script](../gws-script/SKILL.md) — All manage google apps script projects commands

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-script-push/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
