---
name: gws-modelarmor-sanitize-prompt
description: Google Model Armor: Sanitize a user prompt through a Model Armor template.
license: Apache-2.0
metadata:
  title: "gws modelarmor sanitize prompt"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-modelarmor-sanitize-prompt/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# modelarmor +sanitize-prompt

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Sanitize a user prompt through a Model Armor template

## Usage

```bash
gws modelarmor +sanitize-prompt --template <NAME>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--template` | ✓ | — | Full template resource name (projects/PROJECT/locations/LOCATION/templates/TEMPLATE) |
| `--text` | — | — | Text content to sanitize |
| `--json` | — | — | Full JSON request body (overrides --text) |

## Examples

```bash
gws modelarmor +sanitize-prompt --template projects/P/locations/L/templates/T --text 'user input'
echo 'prompt' | gws modelarmor +sanitize-prompt --template ...
```

## Tips

- If neither --text nor --json is given, reads from stdin.
- For outbound safety, use +sanitize-response instead.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-modelarmor](../gws-modelarmor/SKILL.md) — All filter user-generated content for safety commands

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-modelarmor-sanitize-prompt/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
