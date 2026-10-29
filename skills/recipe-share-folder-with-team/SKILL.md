---
name: recipe-share-folder-with-team
description: Share a Google Drive folder and all its contents with a list of collaborators.
license: Apache-2.0
metadata:
  title: "recipe share folder with team"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-share-folder-with-team/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Share a Google Drive Folder with a Team

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Share a Google Drive folder and all its contents with a list of collaborators.

## Steps

1. Find the folder: `gws drive files list --params '{"q": "name = '\''Project X'\'' and mimeType = '\''application/vnd.google-apps.folder'\''"}'`
2. Share as editor: `gws drive permissions create --params '{"fileId": "FOLDER_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "colleague@company.com"}'`
3. Share as viewer: `gws drive permissions create --params '{"fileId": "FOLDER_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "stakeholder@company.com"}'`
4. Verify permissions: `gws drive permissions list --params '{"fileId": "FOLDER_ID"}' --format table`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-share-folder-with-team/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
