---
name: recipe-organize-drive-folder
description: Create a Google Drive folder structure and move files into the right locations.
license: Apache-2.0
metadata:
  title: "recipe organize drive folder"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-organize-drive-folder/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Organize Files into Google Drive Folders

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Create a Google Drive folder structure and move files into the right locations.

## Steps

1. Create a project folder: `gws drive files create --json '{"name": "Q2 Project", "mimeType": "application/vnd.google-apps.folder"}'`
2. Create sub-folders: `gws drive files create --json '{"name": "Documents", "mimeType": "application/vnd.google-apps.folder", "parents": ["PARENT_FOLDER_ID"]}'`
3. Move existing files into folder: `gws drive files update --params '{"fileId": "FILE_ID", "addParents": "FOLDER_ID", "removeParents": "OLD_PARENT_ID"}'`
4. Verify structure: `gws drive files list --params '{"q": "FOLDER_ID in parents"}' --format table`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-organize-drive-folder/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
