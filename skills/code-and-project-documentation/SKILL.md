---
name: code-and-project-documentation
description: "Write the documentation a codebase actually needs: docstrings, API references (OpenAPI/Swagger, JSDoc), documentation sites, READMEs matched to their audience, and lean AGENTS.md/CLAUDE.md instruction files. Use when documenting functions or APIs, building a docs site, writing or fixing a README, or refactoring a bloated agent instruction file into linked progressive-disclosure docs."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Code and project documentation"
  category: "docs-and-planning"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "code-documenter, crafting-effective-readmes, agent-md-refactor"
---

# Code and project documentation

Three audiences, three formats: **code-level** docs (docstrings, API specs) for people calling the code, **project-level** docs (README) for people deciding whether to use it, and **agent-level** docs (AGENTS.md) for a model that must act correctly with the least context. Each has a different failure mode, and mixing them is why documentation rots.

## When to use

- Functions, modules or APIs need documentation.
- A README is missing, bloated, or written for the wrong reader.
- An AGENTS.md/CLAUDE.md has grown into a monolith and needs progressive disclosure.
- A docs site, getting-started guide or tutorial is wanted.

## Method

1. Identify which of the three jobs you are doing before writing a line; a README fix is not an API-docs pass.
2. For code docs: match the language's convention (Google or NumPy style for Python, JSDoc for TypeScript), document behaviour and units rather than restating the signature, and document the failure modes.
3. For API docs: generate the spec from the code where possible, keep request/response examples executable, and state auth and error shapes.
4. For a README: ask who reads it and what they need to know, then use the template for the project type — a library, a tool, an app and a data project need different sections. Do not assume open-source defaults.
5. For agent instruction files: find contradictions first, then extract the essentials (the rules that override defaults), then group the rest by topic into linked files, leaving a short root file as the map.
6. Delete rather than keep: rules an agent already follows ('don't introduce bugs', 'don't commit secrets') waste context and dilute the rules that matter.
7. Keep every claim checkable — a runnable command, a real path, a version. Do not invent features or commands.
8. Verify the docs by following them once, cold.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`code-documenter`](references/code-documenter/) | Code-level documentation: docstring formats, OpenAPI/JSDoc, docs portals, tutorials and guides. |
| [`crafting-effective-readmes`](references/crafting-effective-readmes/) | README method matched to audience and project type, with templates and section checklists. |
| [`agent-md-refactor`](references/agent-md-refactor/) | Refactoring monolithic agent instruction files into progressive-disclosure linked docs. |

## Key files / entry points

- `references/code-documenter/` — docstring formats, API spec generation, docs sites, constraints and output formats.
- `references/crafting-effective-readmes/` — README process, project types, essential sections, templates.
- `references/agent-md-refactor/` — the five-phase refactor: contradictions, essentials, grouping, file structure, deletion flags.

## Gotchas

- Documenting the signature instead of the behaviour adds words and no information.
- A README written for the wrong audience (contributor text in a user README) is the most common documentation failure.
- A 600-line AGENTS.md is not thorough, it is unread — both by people and by models.
- Obvious rules in an instruction file crowd out the non-obvious ones.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `code-documenter` — no licence file shipped with the source
- `crafting-effective-readmes` — no licence file shipped with the source
- `agent-md-refactor` — no licence file shipped with the source
