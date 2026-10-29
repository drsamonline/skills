---
name: gws-modelarmor-create-template
description: Google Model Armor: Create a new Model Armor template.
license: Apache-2.0
metadata:
  title: "gws modelarmor create template"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-modelarmor-create-template/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# modelarmor +create-template

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Create a new Model Armor template

## Usage

```bash
gws modelarmor +create-template --project <PROJECT> --location <LOCATION> --template-id <ID>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--project` | ✓ | — | GCP project ID |
| `--location` | ✓ | — | GCP location (e.g. us-central1) |
| `--template-id` | ✓ | — | Template ID to create |
| `--preset` | — | — | Use a preset template: jailbreak |
| `--json` | — | — | JSON body for the template configuration (overrides --preset) |

## Examples

```bash
gws modelarmor +create-template --project P --location us-central1 --template-id my-tmpl --preset jailbreak
gws modelarmor +create-template --project P --location us-central1 --template-id my-tmpl --json '{...}'
```

## Tips

- Defaults to the jailbreak preset if neither --preset nor --json is given.
- Use the resulting template name with +sanitize-prompt and +sanitize-response.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-modelarmor](../gws-modelarmor/SKILL.md) — All filter user-generated content for safety commands

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-modelarmor-create-template/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
