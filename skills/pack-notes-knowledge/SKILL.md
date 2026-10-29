---
name: pack-notes-knowledge
description: Work inside a Markdown knowledge base: Obsidian Flavored Markdown with wikilinks, callouts and properties, Bases views and formulas, JSON Canvas boards, the Obsidian CLI, templated rendering with Knap, and pulling clean Markdown out of any web page with Defuddle.
license: see each member
metadata:
  title: "Notes and knowledge pack"
  kind: "index pack"
  members: "11"
---

# Notes and knowledge pack

11 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 4 upstream repositories.

## When to use

- Creating or editing notes, callouts, properties or embeds in an Obsidian vault.
- Building a Bases view or a JSON Canvas board.
- Reading, searching or scripting a vault from the command line.
- Converting a web page into clean Markdown.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`bulletmind`](../bulletmind/SKILL.md) | Convert input into clean, structured, hierarchical bullet points for summarization, note-taking, and structured thinking. | sickn33/agentic-awesome-skills | MIT |
| [`defuddle`](../defuddle/SKILL.md) | Extract clean Markdown from HTML pages with Defuddle CLI. | kepano/obsidian-skills | MIT |
| [`json-canvas`](../json-canvas/SKILL.md) | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files, creating visual canvases, mind maps, flowcharts, or… | kepano/obsidian-skills | MIT |
| [`knap`](../knap/SKILL.md) | Render Markdown from templates and structured data using Knap CLI. Use when the user asks to apply a Knap template, turn JSON or CSV data into notes, batch-generate Markdown… | kepano/obsidian-skills | MIT |
| [`notebooklm`](../notebooklm/SKILL.md) | Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automation, library… | PleasePrompto/notebooklm-skill | MIT |
| [`obsidian-bases`](../obsidian-bases/SKILL.md) | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating database-like views of notes, or when the… | kepano/obsidian-skills | MIT |
| [`obsidian-cli`](../obsidian-cli/SKILL.md) | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, and more. Also supports plugin and theme development with… | kepano/obsidian-skills | MIT |
| [`obsidian-clipper-template-creator`](../obsidian-clipper-template-creator/SKILL.md) | Guide for creating templates for the Obsidian Web Clipper. Use when you want to create a new clipping template, understand available variables, or format clipped content. | sickn33/agentic-awesome-skills | MIT |
| [`obsidian-markdown`](../obsidian-markdown/SKILL.md) | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when working with .md files in Obsidian, or… | kepano/obsidian-skills | MIT |
| [`obsidian-second-brain`](../obsidian-second-brain/SKILL.md) | Claude operates your Obsidian vault as a self-rewriting knowledge base. An evolution of Karpathy's LLM Wiki… | eugeniughelbur/obsidian-second-brain | MIT |
| [`unpaid-intern`](../unpaid-intern/SKILL.md) | A free second brain for work in plain markdown files the user owns. Turns transcripts, docs, and tickets into briefings, meeting prep, debriefs, follow-ups, and status tables. | sickn33/agentic-awesome-skills | MIT |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (MIT). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
