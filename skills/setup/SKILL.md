---
name: setup
description: Run initial NanoClaw setup. Use when user wants to install NanoClaw, configure it, or go through first-time setup. Triggers on "setup", "install", "configure nanoclaw", or first-time setup requests.
license: MIT
metadata:
  title: "setup"
  origin: "nanocoai/nanoclaw"
  upstream-path: ".claude/skills/setup/SKILL.md"
  upstream-commit: "acc2b1c8f52a954368cfaf04b61c32f9a1efc280"
  category: "engineering-workflow"
---

# NanoClaw Setup

Tell the user to run `bash nanoclaw.sh` in their terminal. That script handles the full end-to-end setup — dependencies, container image, OneCLI vault, Anthropic credential, service, first agent, and optional channel wiring.

If they hit an error partway through, the script offers Claude-assisted recovery inline and resumes from where it stopped.

## Provenance

Imported from [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) at commit `acc2b1c`, path `.claude/skills/setup/SKILL.md`. Licensed MIT — the full text is in `LICENSE`.
