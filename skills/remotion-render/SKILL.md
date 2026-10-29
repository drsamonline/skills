---
name: remotion-render
description: Full list of options: https://www.remotion.dev/docs/cli/render.md
license: see LICENSE-NOTICE.md
metadata:
  title: "remotion render"
  origin: "remotion-dev/skills"
  upstream-path: "skills/remotion-render/SKILL.md"
  upstream-commit: "30d4553ecd46fbc5212fd0ff006ae43af522158b"
  category: "media-design"
  description-source: "derived from the body — upstream ships no usable description"
---

## General rendering strategy

Render a video using:

```
npx remotion render
```

Full list of options: https://www.remotion.dev/docs/cli/render.md

Render a still using:

```
npx remotion still
```

Full list of options: https://www.remotion.dev/docs/cli/still.md

To render several frames as images in one call, use `render --frames`:

```
npx remotion render [composition-id] out/frames --frames=0,30,90 --image-format=png
```

See https://www.remotion.dev/docs/cli/render.md#--frames for more options.

## Transparent videos

See [Transparent videos](./transparent-videos.md) for rendering out a video with transparency.

## Provenance

Imported from [remotion-dev/skills](https://github.com/remotion-dev/skills) at commit `30d4553`, path `skills/remotion-render/SKILL.md`. The upstream repository publishes no licence file; included at the catalogue owner's direction, all rights with its authors — see `LICENSE-NOTICE.md`.
