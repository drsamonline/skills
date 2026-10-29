---
name: recipe-save-email-to-doc
description: Save a Gmail message body into a Google Doc for archival or reference.
license: Apache-2.0
metadata:
  title: "recipe save email to doc"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-save-email-to-doc/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Save a Gmail Message to Google Docs

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-docs`

Save a Gmail message body into a Google Doc for archival or reference.

## Steps

1. Find the message: `gws gmail users messages list --params '{"userId": "me", "q": "subject:important from:boss@company.com"}' --format table`
2. Get message content: `gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'`
3. Create a doc with the content: `gws docs documents create --json '{"title": "Saved Email - Important Update"}'`
4. Write the email body: `gws docs +write --document-id DOC_ID --text 'From: boss@company.com
Subject: Important Update

[EMAIL BODY]'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-save-email-to-doc/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
