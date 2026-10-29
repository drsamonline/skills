---
name: recipe-email-drive-link
description: Share a Google Drive file and email the link with a message to recipients.
license: Apache-2.0
metadata:
  title: "recipe email drive link"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-email-drive-link/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Email a Google Drive File Link

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-gmail`

Share a Google Drive file and email the link with a message to recipients.

## Steps

1. Find the file: `gws drive files list --params '{"q": "name = '\''Quarterly Report'\''"}'`
2. Share the file: `gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "client@example.com"}'`
3. Email the link: `gws gmail +send --to client@example.com --subject 'Quarterly Report' --body 'Hi, please find the report here: https://docs.google.com/document/d/FILE_ID'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-email-drive-link/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
