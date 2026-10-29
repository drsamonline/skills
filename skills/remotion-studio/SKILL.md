---
name: remotion-studio
description: When creating or editing a video, start Studio and open its preview as soon as the project can run, before building the composition. Keep it open while you work so the user can see changes and steer.
license: see LICENSE-NOTICE.md
metadata:
  title: "remotion studio"
  origin: "remotion-dev/skills"
  upstream-path: "skills/remotion-studio/SKILL.md"
  upstream-commit: "30d4553ecd46fbc5212fd0ff006ae43af522158b"
  category: "media-design"
  description-source: "derived from the body — upstream ships no usable description"
---

When creating or editing a video, start Studio and open its preview as soon as the project can run, before building the composition. Keep it open while you work so the user can see changes and steer.

In Cursor, run Studio without `--no-open` so the browser opens automatically:

```bash
npx remotion studio
```

In other agent clients, you can also let Studio open the browser automatically with the command above. If you have an in-app browser and intend to use it, run:

```bash
npx remotion studio --no-open
```

If the Studio is already opened, the URL will be printed and the command will exit.
Otherwise, a long-running process will start, and the URL will be printed.

When using `--no-open`, open the exact printed URL in the in-app browser and verify that Studio loads. Once a composition exists, verify that its video preview loads. Do not use `--no-open` if you cannot open the URL in the in-app browser.

## Useful flags

| Argument          | Purpose                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------- |
| `--log=<level>`   | Set `error`, `warn`, `info` (default), or `verbose` logging.                                  |
| `--port=<number>` | Request a Studio server port; otherwise Remotion finds a free port.                           |
| `--force-new`     | Start another Studio instance even when one is already running for the same project and port. |

## Provenance

Imported from [remotion-dev/skills](https://github.com/remotion-dev/skills) at commit `30d4553`, path `skills/remotion-studio/SKILL.md`. The upstream repository publishes no licence file; included at the catalogue owner's direction, all rights with its authors — see `LICENSE-NOTICE.md`.
