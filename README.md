# skills — a reusable knowledge base of drsamonline project methods

This repository is a **machine-consumable knowledge base**. Each of the
projects under [`drsamonline`](https://github.com/drsamonline) has its working
*method* extracted into a reusable **skill**, so the same approach can be
reused, extended or branched from instead of being rediscovered.

There are two kinds of skill:

- **Technique skills** — the cross-cutting methods that recur across many
  projects (offline-first single-file web apps, Android WebView packaging,
  the portable EXE launcher, the shared release workflow, the landing-page
  conventions, the open-data pipeline, the LAN server architecture, optical
  file transfer).
- **Project skills** — one per repository: what the project is, how it is
  built, how it is released, and what makes its workflow distinctive.

## Repository layout

```
README.md                     # this file — human index + how AIs consume the repo
llms.txt                      # short plain-text pointer for AI agents
catalog.json                  # machine-readable index of every skill
skills/<skill-id>/SKILL.md    # the skill itself (YAML front-matter + body)
skills/<skill-id>/meta.json   # machine-readable metadata for that skill
docs/                         # the landing page (its own sub-website)
```

Skill ids are lowercase-hyphenated and stable. Categories are a fixed set:

`web-app-patterns`, `android-packaging`, `windows-desktop`, `game-engine`,
`data-and-schema`, `health-tools`, `landing-and-seo`, `ci-and-release`.

## The skill format

### `SKILL.md`

YAML front-matter, then a body with five fixed sections.

```markdown
---
name: Human-readable skill name
description: One sentence — what the skill lets you do.
---

# Human-readable skill name

A short introduction.

## When to use
- ...

## Method
1. ...

## Key files / entry points
- ...

## Gotchas
- ...

## Source projects
- [repo](https://github.com/drsamonline/<repo>) — what it demonstrates.
```

### `meta.json`

```json
{
  "id": "lowercase-hyphenated-id",
  "name": "Human-readable skill name",
  "category": "one of the eight categories",
  "description": "One sentence.",
  "tags": ["..."],
  "source_repos": ["RepoName", "..."],
  "version": "1.0.0",
  "updated": "YYYY-MM-DD",
  "source_snapshot": { "RepoName": "<latest commit SHA when derived>" },
  "subskills": ["related-skill-id", "..."]
}
```

`source_snapshot` maps each source repository to its latest commit SHA at the
time the skill was derived, so a consumer can tell whether the skill still
matches the code it describes.

## How an AI agent should consume this repo

1. Read **`catalog.json`** first — it is the single source of truth. It carries
   `generated`, `count`, `categories[]` and a `skills[]` array whose entries
   mirror each `meta.json`.
2. Pick the skill(s) you need by `id`, `category` or `tags`.
3. Read the matching **`skills/<id>/SKILL.md`** for the actual method.
4. To reuse a project's approach, follow its `source_repos` and, if the skill
   looks stale, compare `source_snapshot` against the repo's current HEAD.

A short pointer file for agents is also provided at [`llms.txt`](llms.txt).

> The catalogue is being populated. `catalog.json` lists every skill present
> under `skills/`.
