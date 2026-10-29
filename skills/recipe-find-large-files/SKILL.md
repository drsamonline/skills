---
name: recipe-find-large-files
description: Identify large Google Drive files consuming storage quota.
license: Apache-2.0
metadata:
  title: "recipe find large files"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-find-large-files/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Find Largest Files in Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Identify large Google Drive files consuming storage quota.

## Steps

1. List files sorted by size: `gws drive files list --params '{"orderBy": "quotaBytesUsed desc", "pageSize": 20, "fields": "files(id,name,size,mimeType,owners)"}' --format table`
2. Review the output and identify files to archive or move

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-find-large-files/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
