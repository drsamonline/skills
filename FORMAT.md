# Skill format — aligned to the Agent Skills specification

Every skill in this repository follows the **Agent Skills** open specification
(https://agentskills.io/specification), so a skill written here can be loaded by
any conforming agent — not only by ours. The format is the standard; this repo
just implements it.

## Directory layout

```
skills/<skill-name>/
├── SKILL.md          # Required: YAML frontmatter + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: extra documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files
```

## `SKILL.md` frontmatter

| Field | Required | Rule |
| --- | --- | --- |
| `name` | **Yes** | 1–64 chars; lowercase letters, digits and single hyphens; no leading/trailing/consecutive hyphen; **must equal the folder name** |
| `description` | **Yes** | 1–1024 chars; says **what** the skill does **and when** to use it |
| `license` | No | short name, or a reference to a bundled licence file |
| `compatibility` | No | 1–500 chars; environment requirements only |
| `metadata` | No | map of string → string (use unique key names) |
| `allowed-tools` | No | space-separated pre-approved tools (experimental) |

Minimal valid skill:

```markdown
---
name: optical-file-transfer
description: Send a file between two devices using light — QR or a colour matrix. Use when moving a file with no network.
---

# Optical file transfer
…instructions…
```

## House conventions (on top of the spec)

The spec fixes the frontmatter; these are our own conventions for the body, so
the skills read consistently:

- **When to use** — the trigger, in one or two lines.
- **Method** — the steps, in order.
- **Key files** — the files that matter in the source repo.
- **Gotchas** — the traps we actually hit.
- **Source projects** — the repo(s) this was distilled from.

The body has **no format restrictions** in the spec — these headings are a
convention, not a requirement.

## Validate

```bash
python3 scripts/validate.py
```

`scripts/validate.py` checks every `skills/*/SKILL.md` against the spec
(frontmatter present, `name` matching the folder and the character rules,
`description` length, optional-field limits). It exits non-zero on any problem,
and `.github/workflows/validate.yml` runs it on every push.

**A skill that does not validate is a bug** — fix it, don't special-case it.
