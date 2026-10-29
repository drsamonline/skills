---
name: recipe-share-doc-and-notify
description: Share a Google Docs document with edit access and email collaborators the link.
license: Apache-2.0
metadata:
  title: "recipe share doc and notify"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-share-doc-and-notify/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Share a Google Doc and Notify Collaborators

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-docs`, `gws-gmail`

Share a Google Docs document with edit access and email collaborators the link.

## Steps

1. Find the doc: `gws drive files list --params '{"q": "name contains '\''Project Brief'\'' and mimeType = '\''application/vnd.google-apps.document'\''"}'`
2. Share with editor access: `gws drive permissions create --params '{"fileId": "DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "reviewer@company.com"}'`
3. Email the link: `gws gmail +send --to reviewer@company.com --subject 'Please review: Project Brief' --body 'I have shared the project brief with you: https://docs.google.com/document/d/DOC_ID'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-share-doc-and-notify/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
