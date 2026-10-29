---
name: recipe-create-shared-drive
description: Create a Google Shared Drive and add members with appropriate roles.
license: Apache-2.0
metadata:
  title: "recipe create shared drive"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-shared-drive/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create and Configure a Shared Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Create a Google Shared Drive and add members with appropriate roles.

## Steps

1. Create shared drive: `gws drive drives create --params '{"requestId": "unique-id-123"}' --json '{"name": "Project X"}'`
2. Add a member: `gws drive permissions create --params '{"fileId": "DRIVE_ID", "supportsAllDrives": true}' --json '{"role": "writer", "type": "user", "emailAddress": "member@company.com"}'`
3. List members: `gws drive permissions list --params '{"fileId": "DRIVE_ID", "supportsAllDrives": true}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-shared-drive/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
