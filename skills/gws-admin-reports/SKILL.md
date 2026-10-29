---
name: gws-admin-reports
description: Google Workspace Admin SDK: Audit logs and usage reports.
license: Apache-2.0
metadata:
  title: "gws admin reports"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-admin-reports/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# admin-reports (reports_v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws admin-reports <resource> <method> [flags]
```

## API Resources

### activities

  - `list` — Retrieves a list of activities for a specific customer's account and application such as the Admin console application or the Google Drive application. For more information, see the guides for administrator and Google Drive activity reports. For more information about the activity report's parameters, see the activity parameters reference guides.
  - `watch` — Start receiving notifications for account activities. For more information, see Receiving Push Notifications.

### channels

  - `stop` — Stop watching resources through this channel.

### customerUsageReports

  - `get` — Retrieves a report which is a collection of properties and statistics for a specific customer's account. For more information, see the Customers Usage Report guide. For more information about the customer report's parameters, see the Customers Usage parameters reference guides.

### entityUsageReports

  - `get` — Retrieves a report which is a collection of properties and statistics for entities used by users within the account. For more information, see the Entities Usage Report guide. For more information about the entities report's parameters, see the Entities Usage parameters reference guides.

### userUsageReport

  - `get` — Retrieves a report which is a collection of properties and statistics for a set of users with the account. For more information, see the User Usage Report guide. For more information about the user report's parameters, see the Users Usage parameters reference guides.

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws admin-reports --help

# Inspect a method's required params, types, and defaults
gws schema admin-reports.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-admin-reports/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
