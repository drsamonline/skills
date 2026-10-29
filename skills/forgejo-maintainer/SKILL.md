---
name: forgejo-maintainer
description: Administer Forgejo or Gitea installations, including upgrades, backups, migrations, repository access, and Actions runners. Use for application-specific operations, not general Linux host troubleshooting.
license: MIT
metadata:
  title: "Forgejo and Gitea administration"
  origin: "ChrisTitusTech/titstack"
  upstream-path: ".agents/skills/forgejo-maintainer"
  upstream-commit: "b9b7fb03bd347e4b514c5a6ccff397dbc909b65c"
  license: "MIT"
---
# forgejo-maintainer

## Workflow

1. Establish the deployment method, Forgejo version, database, storage paths,
   configuration, and runner topology.
2. Separate application failures from host, network, container, and reverse
   proxy failures; use the narrower skill for substantial work in those layers.
3. For authorized changes, determine affected access paths and prepare
   rollback. Take database and data backups before upgrades or migrations;
   read-only diagnosis does not require creating backups.
4. Make the smallest application-specific change and validate every affected
   access path.

## Diagnostics

```bash
systemctl status forgejo
journalctl -xeu forgejo
forgejo --version
df -h
findmnt
ss -tulpn
ssh -T git@<host>
curl -I <root-url>
```

## Safety Rules

- Never upgrade before taking database and data backups.
- Never trust a backup policy until restore has been tested.
- Never expose runner registration tokens in logs or docs.
- Preserve `app.ini`, repositories, LFS objects, attachments, packages, and custom templates.
- Isolate Actions runners by trust boundary.

## Validation

- Validate the access paths affected by the change; an upgrade needs the full
  application smoke test below. Report unavailable checks explicitly.
- Web login and repository browsing work.
- HTTPS clone and SSH clone work.
- Pull works; test pushes and Actions jobs require authorization for those
  remote writes and an appropriate test repository.
- Actions runners register and run a small job when applicable.
- Backup artifacts exist and restore steps are documented.

## Licence and provenance

Imported unchanged from [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) at commit `b9b7fb0`, path `.agents/skills/forgejo-maintainer/`. MIT licensed, © 2026 titstack contributors — the full licence text travels with this skill as `LICENSE`.
