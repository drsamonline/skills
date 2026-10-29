---
name: recipe-docs
description: Docs and Slides recipes — create, template, share, report. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "Docs and Slides recipes — create, template, share, report"
  origin: "googleworkspace/cli"
  merged-from: "4 skills"
  category: "google-workspace"
---

# Docs and Slides recipes — create, template, share, report

A merge of 4 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- Docs and Slides recipes — create, template, share, report. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `recipe-create-doc-from-template` | Copy a Google Docs template, fill in content, and share with collaborators. |
| `recipe-create-presentation` | Create a new Google Slides presentation and add initial slides. |
| `recipe-post-mortem-setup` | Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat. |
| `recipe-share-doc-and-notify` | Share a Google Docs document with edit access and email collaborators the link. |

## recipe-create-doc-from-template

### Create a Google Doc from a Template

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-docs`

Copy a Google Docs template, fill in content, and share with collaborators.

#### Steps

1. Copy the template: `gws drive files copy --params '{"fileId": "TEMPLATE_DOC_ID"}' --json '{"name": "Project Brief - Q2 Launch"}'`
2. Get the new doc ID from the response
3. Add content: `gws docs +write --document-id NEW_DOC_ID --text '## Project: Q2 Launch

##### Objective
Launch the new feature by end of Q2.'`
4. Share with team: `gws drive permissions create --params '{"fileId": "NEW_DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'`

## recipe-create-presentation

### Create a Google Slides Presentation

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-slides`

Create a new Google Slides presentation and add initial slides.

#### Steps

1. Create presentation: `gws slides presentations create --json '{"title": "Quarterly Review Q2"}'`
2. Get the presentation ID from the response
3. Share with team: `gws drive permissions create --params '{"fileId": "PRESENTATION_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'`

## recipe-post-mortem-setup

### Set Up Post-Mortem

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-docs`, `gws-calendar`, `gws-chat`

Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat.

#### Steps

1. Create post-mortem doc: `gws docs +write --title 'Post-Mortem: [Incident]' --body '## Summary\n\n## Timeline\n\n## Root Cause\n\n## Action Items'`
2. Schedule review meeting: `gws calendar +insert --summary 'Post-Mortem Review: [Incident]' --attendee team@company.com --start '2026-03-16T14:00:00' --end '2026-03-16T15:00:00'`
3. Notify in Chat: `gws chat +send --space spaces/ENG_SPACE --text '🔍 Post-mortem scheduled for [Incident].'`

## recipe-share-doc-and-notify

### Share a Google Doc and Notify Collaborators

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-docs`, `gws-gmail`

Share a Google Docs document with edit access and email collaborators the link.

#### Steps

1. Find the doc: `gws drive files list --params '{"q": "name contains '\''Project Brief'\'' and mimeType = '\''application/vnd.google-apps.document'\''"}'`
2. Share with editor access: `gws drive permissions create --params '{"fileId": "DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "reviewer@company.com"}'`
3. Email the link: `gws gmail +send --to reviewer@company.com --subject 'Please review: Project Brief' --body 'I have shared the project brief with you: https://docs.google.com/document/d/DOC_ID'`

## Provenance

Merged from 4 skills of [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`. Licence Apache-2.0 — the source text of every variant is preserved above.
