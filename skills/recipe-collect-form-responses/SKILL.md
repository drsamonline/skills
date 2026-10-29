---
name: recipe-collect-form-responses
description: Retrieve and review responses from a Google Form.
license: Apache-2.0
metadata:
  title: "recipe collect form responses"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-collect-form-responses/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Check Form Responses

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-forms`

Retrieve and review responses from a Google Form.

## Steps

1. List forms: `gws forms forms list` (if you don't have the form ID)
2. Get form details: `gws forms forms get --params '{"formId": "FORM_ID"}'`
3. Get responses: `gws forms forms responses list --params '{"formId": "FORM_ID"}' --format table`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-collect-form-responses/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
