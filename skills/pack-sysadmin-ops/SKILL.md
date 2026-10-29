---
name: pack-sysadmin-ops
description: Infrastructure administration in one pack: Linux host diagnostics (services, packages, SELinux, firewalls, SSH), Podman containers and Quadlet units, Forgejo/Gitea upgrades, backups and runners, and cross-system homelab work. Use for operations that span a host, its containers and its services.
license: MIT
metadata:
  title: "Sysadmin pack — host, container, service, homelab"
  origin: "ChrisTitusTech/titstack"
  license: "MIT"
  upstream-commit: "b9b7fb03bd347e4b514c5a6ccff397dbc909b65c"
  members: "linux-sysadmin, podman-operator, forgejo-maintainer, homelab-admin"
---

# Sysadmin pack — host, container, service, homelab

A pack of 4 related skills from [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack), merged into one document so the whole workflow is in front of you at once. Each member is also kept as its own skill in this repository, and every member's support files are preserved here under `references/<member>/`, `scripts/<member>/` and `assets/<member>/`.

## When to use

- A host-level problem — a failed unit, a permission or SELinux denial, a firewall rule, an SSH login.
- A container or Quadlet unit needs building, deploying, networking or debugging, including rootless.
- A Forgejo/Gitea instance needs an upgrade, backup, migration, access change or Actions runner.
- The work crosses hosts — DNS, NFS, a reverse proxy, several services at once.

## Which member to follow

| Situation | Skill |
|---|---|
| One Linux host, host-level symptom | `linux-sysadmin` |
| Containers, Quadlet, rootless deployment | `podman-operator` |
| Forgejo or Gitea itself | `forgejo-maintainer` |
| Several hosts, DNS, storage, reverse proxy | `homelab-admin` |
| A dwm/Quickshell desktop app is broken | not here — use the Linux desktop pack |

## Method

Pick the member for the situation in the table above, then follow that member's own workflow below. Do not run all of them: each member is written to stand alone, and running a review loop for a one-line edit is the failure mode this pack is meant to prevent.

## Linux host administration

*Member skill: `linux-sysadmin` — Diagnose and operate Linux hosts, services, packages, permissions, SELinux, firewalls, and SSH. Use for host-level work that is not primarily an application-specific or container task.*

### Workflow

1. Gather diagnostics for the reported symptom and complete relevant log
   interval. Do not run every example below for an isolated service issue.
2. Determine whether the failure is host-level or primarily belongs to a
   specialized application, container, or cross-system infrastructure skill.
3. For an authorized fix, identify impact and recent changes, then prepare
   rollback for the files, packages, units, or firewall rules being changed.
4. Implement the smallest host-level fix and validate runtime behavior, remote
   access, security policy, and boot persistence.

### Diagnostics

```bash
cat /etc/os-release
uname -a
uptime
free -h
df -h
lsblk
systemctl status <unit>
journalctl -xeu <unit>
ss -tulpn
getenforce
firewall-cmd --list-all
ufw status verbose
```

### Safety Rules

- Never disable SELinux as a default fix.
- Never rotate SSH keys or change `sshd_config` without rollback.
- Never modify firewall rules without confirming active firewall stack.
- Prefer systemd drop-ins over editing packaged unit files.
- Preserve ownership, permissions, ACLs, mount options, and labels.

### Validation

- The affected service runs and its boot configuration is correct. Reboot only
  when authorized; distinguish inspection from a verified reboot test.
- Logs show no new errors.
- Expected ports listen and unexpected ports do not.
- SSH access still works.
- SELinux and firewall state match the intended policy.

## Podman and Quadlet operations

*Member skill: `podman-operator` — Build and operate Podman containers and Quadlet services, including rootless deployment, networking, volumes, systemd integration, and troubleshooting.*

### Workflow

1. Gather container, image, network, volume, and systemd state.
2. Separate container lifecycle or Quadlet failures from underlying host,
   storage, DNS, and application failures; route substantial work in those
   layers to the narrower skill.
3. Preserve the rootless or rootful deployment model unless the task requires
   changing it. Before mutation, retain prior image identifiers and units;
   back up volume data when the operation could change or remove it.
4. Implement the smallest Podman-specific change and validate it through both
   systemd and Podman.

### Diagnostics

```bash
podman ps -a
podman images
podman logs <container>
podman inspect <container>
podman network ls
podman volume ls
systemctl --user status <unit>
journalctl --user -xeu <unit>
loginctl show-user <user>
```

Use selected `podman inspect --format` fields for the diagnosis; full inspect
output and logs can contain environment credentials. Do not expose secrets.
Use `systemctl --user` for rootless units and the system manager for rootful
units; run only the diagnostics relevant to the failure.

### Safety Rules

- Prefer Quadlet for persistent services.
- Prefer rootless containers unless host integration requires rootful operation.
- Never put secrets directly in unit files.
- Never delete volumes without explicit approval.
- Preserve SELinux labels and fix denials with targeted labels.

### Validation

- The unit is healthy in the correct systemd manager.
- `podman ps` shows expected ports and status.
- Container logs show no startup errors.
- Published endpoints respond from the host and expected clients.
- Inspect restart and boot configuration. Exercise disruptive restart or reboot
  tests only within the authorized maintenance scope and report untested paths.

## Forgejo and Gitea administration

*Member skill: `forgejo-maintainer` — Administer Forgejo or Gitea installations, including upgrades, backups, migrations, repository access, and Actions runners. Use for application-specific operations, not general Linux host troubleshooting.*

### Workflow

1. Establish the deployment method, Forgejo version, database, storage paths,
   configuration, and runner topology.
2. Separate application failures from host, network, container, and reverse
   proxy failures; use the narrower skill for substantial work in those layers.
3. For authorized changes, determine affected access paths and prepare
   rollback. Take database and data backups before upgrades or migrations;
   read-only diagnosis does not require creating backups.
4. Make the smallest application-specific change and validate every affected
   access path.

### Diagnostics

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

### Safety Rules

- Never upgrade before taking database and data backups.
- Never trust a backup policy until restore has been tested.
- Never expose runner registration tokens in logs or docs.
- Preserve `app.ini`, repositories, LFS objects, attachments, packages, and custom templates.
- Isolate Actions runners by trust boundary.

### Validation

- Validate the access paths affected by the change; an upgrade needs the full
  application smoke test below. Report unavailable checks explicitly.
- Web login and repository browsing work.
- HTTPS clone and SSH clone work.
- Pull works; test pushes and Actions jobs require authorization for those
  remote writes and an appropriate test repository.
- Actions runners register and run a small job when applicable.
- Backup artifacts exist and restore steps are documented.

## Homelab administration

*Member skill: `homelab-admin` — Operate homelab infrastructure spanning networking, DNS, storage, NFS, reverse proxies, or multiple services. Use for cross-system work rather than an isolated host, application, or container problem.*

### Workflow

1. Map the affected hosts, clients, network paths, storage dependencies, and
   service ownership before changing anything.
2. Route an isolated Linux, Forgejo, or Podman problem to its narrower skill;
   keep this skill active when multiple infrastructure layers interact.
3. For authorized changes, determine impact and prepare rollback. Before
   changes that could sever access, verify an alternate recovery path.
4. Validate the affected service, network, storage, and client paths. Inspect
   persistence configuration; reboot only within an authorized maintenance scope.

### Diagnostics

```bash
hostnamectl
ip addr
ip route
systemctl status <service>
journalctl -xeu <service>
ss -tulpn
df -h
lsblk
findmnt
dig <name>
curl -I <url>
```

### Safety Rules

- Never destroy data without explicit approval.
- Never modify firewall or DNS blindly.
- Never change networking without rollback and out-of-band access.
- Treat storage, reverse proxy, and NFS changes as high blast-radius work.
- Prefer incremental config changes over broad rewrites.
- Keep TLS certificate verification enabled. Do not use insecure requests as
  evidence that a certificate or trust-chain problem is fixed.

### Validation

- Changed services and mounts work now and have correct persistence settings.
- Report an actual reboot test separately from configuration inspection.
- DNS resolves from expected clients.
- Reverse proxy routes to the expected backend.
- Logs show no new errors.

## Gotchas

- The members disagree on one thing on purpose: `dwm-titus-debug` and `linux-sysadmin` inspect before they change, while the change skills act. Keep that split — diagnosis is read-only unless the user asks for a fix.
- `wayfinder` is explicit-invocation only in the upstream setup. Loading this pack is not an instruction to run it.
- `code-review` never replaces a review the repository requires; `autofix` fixes findings and does not push or reply without authorisation.

## Source projects

All members come from [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) at commit `b9b7fb0` (MIT, © 2026 titstack contributors): `linux-sysadmin`, `podman-operator`, `forgejo-maintainer`, `homelab-admin`.
