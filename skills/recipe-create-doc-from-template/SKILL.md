---
name: recipe-create-doc-from-template
description: Copy a Google Docs template, fill in content, and share with collaborators.
license: Apache-2.0
metadata:
  title: "recipe create doc from template"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-doc-from-template/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create a Google Doc from a Template

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-docs`

Copy a Google Docs template, fill in content, and share with collaborators.

## Steps

1. Copy the template: `gws drive files copy --params '{"fileId": "TEMPLATE_DOC_ID"}' --json '{"name": "Project Brief - Q2 Launch"}'`
2. Get the new doc ID from the response
3. Add content: `gws docs +write --document-id NEW_DOC_ID --text '## Project: Q2 Launch

### Objective
Launch the new feature by end of Q2.'`
4. Share with team: `gws drive permissions create --params '{"fileId": "NEW_DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-doc-from-template/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
