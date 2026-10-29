---
name: recipe-create-feedback-form
description: Create a Google Form for feedback and share it via Gmail.
license: Apache-2.0
metadata:
  title: "recipe create feedback form"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-feedback-form/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create and Share a Google Form

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-forms`, `gws-gmail`

Create a Google Form for feedback and share it via Gmail.

## Steps

1. Create form: `gws forms forms create --json '{"info": {"title": "Event Feedback", "documentTitle": "Event Feedback Form"}}'`
2. Get the form URL from the response (responderUri field)
3. Email the form: `gws gmail +send --to attendees@company.com --subject 'Please share your feedback' --body 'Fill out the form: FORM_URL'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-feedback-form/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
