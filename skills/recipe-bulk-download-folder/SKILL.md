---
name: recipe-bulk-download-folder
description: List and download all files from a Google Drive folder.
license: Apache-2.0
metadata:
  title: "recipe bulk download folder"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-bulk-download-folder/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Bulk Download Drive Folder

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

List and download all files from a Google Drive folder.

## Steps

1. List files in folder: `gws drive files list --params '{"q": "'\''FOLDER_ID'\'' in parents"}' --format json`
2. Download each file: `gws drive files get --params '{"fileId": "FILE_ID", "alt": "media"}' -o filename.ext`
3. Export Google Docs as PDF: `gws drive files export --params '{"fileId": "FILE_ID", "mimeType": "application/pdf"}' -o document.pdf`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-bulk-download-folder/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
