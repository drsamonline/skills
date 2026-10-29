---
name: recipe-create-task-list
description: Set up a new Google Tasks list with initial tasks.
license: Apache-2.0
metadata:
  title: "recipe create task list"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-task-list/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create a Task List and Add Tasks

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-tasks`

Set up a new Google Tasks list with initial tasks.

## Steps

1. Create task list: `gws tasks tasklists insert --json '{"title": "Q2 Goals"}'`
2. Add a task: `gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Review Q1 metrics", "notes": "Pull data from analytics dashboard", "due": "2024-04-01T00:00:00Z"}'`
3. Add another task: `gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Draft Q2 OKRs"}'`
4. List tasks: `gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}' --format table`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-task-list/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
