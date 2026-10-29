---
name: pack-office-docs
description: Produce and edit real office files: Word documents with tracked changes and styles, PowerPoint decks built with PptxGenJS or edited XML-safely inside a template, Excel workbooks with formulas and formatting, and PDFs — read, filled, merged, split or generated.
license: see each member
metadata:
  title: "Office documents pack"
  kind: "index pack"
  members: "15"
---

# Office documents pack

15 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 3 upstream repositories.

## When to use

- A .docx, .pptx, .xlsx or .pdf has to be created, edited or read.
- A deck has to follow a corporate template exactly.
- A spreadsheet needs formulas, pivots or validation, not a CSV dump.
- A PDF needs filling, merging, splitting or extracting.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`docx`](../docx/SKILL.md) | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Triggers include: any mention of 'Word… | anthropics/skills | proprietary (see LICENSE) |
| [`frontend-slides`](../frontend-slides/SKILL.md) | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. | sickn33/agentic-awesome-skills | MIT |
| [`minimax-docx`](../minimax-docx/SKILL.md) | Create, edit, and format DOCX documents via CLI tools or direct C# scripts built on OpenXML SDK (.NET). | MiniMax-AI/skills | MIT |
| [`minimax-pdf`](../minimax-pdf/SKILL.md) | Rule: when in doubt between CREATE and REFORMAT, ask whether the user has an existing document to start from. If yes → REFORMAT. If no → CREATE. | MiniMax-AI/skills | MIT |
| [`minimax-xlsx`](../minimax-xlsx/SKILL.md) | Open, create, read, analyze, edit, or validate Excel/spreadsheet files (.xlsx, .xlsm, .csv, .tsv). Use when the user asks to create, build, modify, analyze, read, validate, or… | MiniMax-AI/skills | MIT |
| [`pdf`](../pdf/SKILL.md) | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one,… | anthropics/skills | proprietary (see LICENSE) |
| [`pdf-conversion-router`](../pdf-conversion-router/SKILL.md) | Use when converting a PDF into another format such as Markdown, HTML, text, JSON, DOCX, or structured notes and the agent must choose the best extraction route, settings, and… | sickn33/agentic-awesome-skills | MIT |
| [`ppt-editing-skill`](../ppt-editing-skill/SKILL.md) | Edit existing PowerPoint files or templates with XML-safe workflows. Use for template-based deck updates: analyze layouts, map content to slides, duplicate/reorder/delete… | MiniMax-AI/skills | MIT |
| [`ppt-orchestra-skill`](../ppt-orchestra-skill/SKILL.md) | Plan and orchestrate multi-slide PowerPoint creation from scratch. Use before generating a full deck with subagents: classify each slide type, enforce visual variety, set… | MiniMax-AI/skills | MIT |
| [`pptx`](../pptx/SKILL.md) | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading,… | anthropics/skills | proprietary (see LICENSE) |
| [`pptx-deck-creation`](../pptx-deck-creation/SKILL.md) | Create editable, production-ready PPTX decks with narrative planning, explicit layout specs, asset guidance, and quality checks. | sickn33/agentic-awesome-skills | MIT |
| [`pptx-generator`](../pptx-generator/SKILL.md) | Generate, edit, and read PowerPoint presentations. Create from scratch with PptxGenJS (cover, TOC, content, section divider, summary slides), edit existing PPTX via XML… | MiniMax-AI/skills | MIT |
| [`slide-making-skill`](../slide-making-skill/SKILL.md) | Implement single-slide PowerPoint pages with PptxGenJS. Use when writing or fixing slide JS files: dimensions, positioning, text/image/chart APIs, styling rules, and export… | MiniMax-AI/skills | MIT |
| [`spreadsheet-manual-build`](../spreadsheet-manual-build/SKILL.md) | Spreadsheet Manual Build: an empty Excel workbook or CSV from a confirmed field list, formatted and validated. Use for an xlsx template or a manual register. | sickn33/agentic-awesome-skills | MIT |
| [`xlsx`](../xlsx/SKILL.md) | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm,… | anthropics/skills | proprietary (see LICENSE) |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (MIT, proprietary (see LICENSE)). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
