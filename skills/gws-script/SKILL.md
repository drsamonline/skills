---
name: gws-script
description: Manage Google Apps Script projects.
license: Apache-2.0
metadata:
  title: "gws script"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-script/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# script (v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws script <resource> <method> [flags]
```

## Helper Commands

| Command | Description |
|---------|-------------|
| [`+push`](../gws-script-push/SKILL.md) | Upload local files to an Apps Script project |

## API Resources

### processes

  - `list` — List information about processes made by or on behalf of a user, such as process type and current status.
  - `listScriptProcesses` — List information about a script's executed processes, such as process type and current status.

### projects

  - `create` — Creates a new, empty script project with no script files and a base manifest file.
  - `get` — Gets a script project's metadata.
  - `getContent` — Gets the content of the script project, including the code source and metadata for each script file.
  - `getMetrics` — Get metrics data for scripts, such as number of executions and active users.
  - `updateContent` — Updates the content of the specified script project. This content is stored as the HEAD version, and is used when the script is executed as a trigger, in the script editor, in add-on preview mode, or as a web app or Apps Script API in development mode. This clears all the existing files in the project.
  - `deployments` — Operations on the 'deployments' resource
  - `versions` — Operations on the 'versions' resource

### scripts

  - `run` — 

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws script --help

# Inspect a method's required params, types, and defaults
gws schema script.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-script/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
