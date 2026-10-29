---
name: remotion-captions
description: Transcribing, displaying and animating captions
license: see LICENSE-NOTICE.md
metadata:
  title: "remotion captions"
  origin: "remotion-dev/skills"
  upstream-path: "skills/remotion-captions/SKILL.md"
  upstream-commit: "30d4553ecd46fbc5212fd0ff006ae43af522158b"
  category: "media-design"
---

All captions must be processed in JSON. The captions must use the [`Caption`](https://www.remotion.dev/docs/captions/caption.md) type which is the following:

```ts
import type { Caption } from "@remotion/captions";
```

This is the definition:

```ts
type Caption = {
  text: string;
  startMs: number;
  endMs: number;
  timestampMs: number | null;
  confidence: number | null;
  pageBreakAfter?: boolean;
};
```

## Generating captions

To transcribe video and audio files to generate captions, load the [transcribe-captions.md](transcribe-captions.md) file for more instructions.

## Displaying captions

To display captions in your video, load the [display-captions.md](display-captions.md) file for more instructions.

## Importing captions

To import captions from a .srt file, load the [import-srt-captions.md](import-srt-captions.md) file for more instructions.

## Post-creation

After you're done, load this skill: Remotion Best Practices

If not alreay done, open the Remotion Studio, unless instructed otherwise.

## Provenance

Imported from [remotion-dev/skills](https://github.com/remotion-dev/skills) at commit `30d4553`, path `skills/remotion-captions/SKILL.md`. The upstream repository publishes no licence file; included at the catalogue owner's direction, all rights with its authors — see `LICENSE-NOTICE.md`.
