---
name: recipe-draft-email-from-doc
description: Read content from a Google Doc and use it as the body of a Gmail message.
license: Apache-2.0
metadata:
  title: "recipe draft email from doc"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-draft-email-from-doc/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Draft a Gmail Message from a Google Doc

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-docs`, `gws-gmail`

Read content from a Google Doc and use it as the body of a Gmail message.

## Steps

1. Get the document content: `gws docs documents get --params '{"documentId": "DOC_ID"}'`
2. Copy the text from the body content
3. Send the email: `gws gmail +send --to recipient@example.com --subject 'Newsletter Update' --body 'CONTENT_FROM_DOC'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-draft-email-from-doc/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
