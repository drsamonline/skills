---
name: pack-media-design
description: Cover and image work: design a restrained 16:9 YouTube thumbnail around one readable idea while keeping photographed people exactly as they are, and create, composite or export layered images through the photocraft-cli MCP server. Use when a thumbnail, logo, cover or photo composite is needed.
license: MIT
metadata:
  title: "Media pack — thumbnails and image work"
  origin: "ChrisTitusTech/titstack"
  license: "MIT"
  upstream-commit: "b9b7fb03bd347e4b514c5a6ccff397dbc909b65c"
  members: "youtube-thumbnail, photocraft"
---

# Media pack — thumbnails and image work

A pack of 2 related skills from [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack), merged into one document so the whole workflow is in front of you at once. Each member is also kept as its own skill in this repository, and every member's support files are preserved here under `references/<member>/`, `scripts/<member>/` and `assets/<member>/`.

## When to use

- A YouTube thumbnail or video cover is requested or reviewed — always use the thumbnail rules.
- Images need creating, inspecting, editing, compositing or exporting, including logos and layered artwork.

## Which member to follow

| Situation | Skill |
|---|---|
| Design or review a YouTube thumbnail | `youtube-thumbnail` |
| Edit, composite or export an image | `photocraft` |
| A docs site needs a hero image | youtube-thumbnail for the layout rules, then photocraft |

## Method

Pick the member for the situation in the table above, then follow that member's own workflow below. Do not run all of them: each member is written to stand alone, and running a review loop for a one-line edit is the failure mode this pack is meant to prevent.

## YouTube thumbnails

*Member skill: `youtube-thumbnail` — Create, edit, or review YouTube thumbnails. Always use when a YouTube thumbnail or video cover is requested; keep the design restrained and preserve photographed people exactly.*

Create a clear 16:9 thumbnail built around one idea. Favor hierarchy, curiosity,
and an instantly readable subject over visual noise.

### Core Rules

- Use a 1280 x 720 canvas unless the user requests another size.
- Communicate one idea with one dominant focal point.
- Prefer no text when the image communicates the idea. Otherwise use one short
  phrase, normally one to four words. Do not repeat the full video title.
- Keep colors natural and controlled. Do not globally oversaturate the image,
  crush shadows, clip highlights, or push skin tones toward orange or red.
- Preserve photographed people. Do not regenerate, beautify, reshape, repaint,
  relight, recolor, sharpen, smooth, or otherwise alter their face, skin, hair,
  body, expression, clothing, accessories, or silhouette.
- Allow only cropping, uniform scaling, positioning, and a natural drop shadow
  around a person. Do not add strokes, keylines, glows, halos, rim lights, or
  bright outlines around people.
- Never invent or replace a recognizable person when a source photo is
  provided. Use the original pixels.

### Workflow

1. Inspect the title, topic, source images, brand assets, and any reference
   thumbnails. Identify the single visual promise of the video. Before generating
   a background, ask for the PhotoCraft filename unless the user already
   supplied it. Use that basename with a `.pcraft` extension in
   `/media/drive/Video Production/YTthumbnails/`; do not invent a filename.
2. Select the simplest composition that communicates that promise:
   - one subject plus a contextual background;
   - one subject plus one supporting object; or
   - one strong object or scene with optional short text.
3. Establish hierarchy at small size. Make the main subject recognizable before
   adding secondary elements. Keep important content away from the bottom-right
   timestamp area and allow breathing room near every edge.
4. Lock any source person before generating or editing other elements. Generate
   the background or supporting graphics separately, then composite the original
   person over them. If exact pixel preservation cannot be guaranteed, do not
   send the person through a generative edit. As soon as the background is
   generated, import it into PhotoCraft and save the initial layered `.pcraft`
   document at the requested path before continuing the composition. Follow
   the native save checkpoint instructions below.
5. Add text only if it supplies information the image cannot. Use one bold,
   legible type style with strong contrast and minimal effects. Avoid stacked
   captions, tiny labels, punctuation clutter, and multiple competing fonts.
6. Apply restrained finishing. Use selective contrast and color separation
   instead of extreme saturation. For a person, use only a soft, neutral drop
   shadow with modest opacity and blur.
7. Save the editable document as `.pcraft` and export the final thumbnail as
   PNG, JPEG, or WebP at 1280 x 720.

### Image Tool Guidance

- Use the `photocraft` skill and `photocraft-cli` MCP tools for supported image
  inspection, layered assembly, editing, previews, and export. Discover command
  parameters before applying edits. If the connection or capability is missing,
  explain the limitation before selecting another tool; follow explicit user
  tool choices and higher-priority tool requirements.
- Inspect every supplied source image before editing it.
- Use image generation for new backgrounds, objects, textures, or complete
  thumbnails that contain no supplied person.
- Use PhotoCraft's supported non-generative compositing for supplied people. Keep the
  original person layer unchanged apart from crop, uniform scale, position, and
  drop shadow.
- Save the layered `.pcraft` document alongside the final image so the
  composition remains editable.
- When writing an image-generation prompt, explicitly request a clean 16:9
  composition, a restrained natural palette, realistic contrast, negative
  space for optional text, and no embedded typography unless the tool is meant
  to render the final text.
- Do not claim a person was preserved unless the final image was compared with
  the source at full size.

### Native Save Checkpoint

- Use `.pcraft` for every working-document save. Save
  `/media/drive/Video Production/YTthumbnails/<filename>.pcraft` through the
  PhotoCraft MCP's `doc_save` tool using its discovered schema.
- Check that the destination directory is available and within the MCP read
  and write roots before generating the background. If it is not, explain the
  missing mount or MCP configuration; do not silently save elsewhere or broaden
  access.
- Treat the supplied filename as a basename, not a path. If it would replace an
  existing file and replacement has not been authorized, ask for a different
  filename or permission to replace that file.
- Verify the initial `.pcraft` file exists and reopens in PhotoCraft with the
  expected canvas and background layer. Keep subsequent people, text, and
  supporting graphics on separate layers and update the same `.pcraft` file
  as the work progresses.
- Deliver the `.pcraft` working file alongside the final thumbnail and report
  a failed native save or verification as incomplete work, even if the generated
  background is available.

### Visual QA

Before delivery, inspect the full-resolution result and a small thumbnail-sized
preview. Confirm all of the following:

- The concept is understandable within roughly one second.
- The thumbnail contains one clear focal point and no unnecessary decoration.
- Text is absent or limited to one short, readable phrase.
- No person has changed relative to the source.
- People have no outline, glow, halo, rim light, or edge color; any separation
  comes only from a natural drop shadow.
- Saturation and contrast remain controlled, especially in skin tones and
  brand colors.
- The subject and text remain legible at small size and are not obstructed by
  the timestamp area.
- The final file is exactly 16:9 and has no accidental crop, padding, artifacts,
  or embedded watermark.

If any check fails, revise the thumbnail and inspect it again before presenting
the result.

### Delivery QA

Do not treat an internal sandbox path, generated preview reference, or claimed
export as a delivered file. Before finishing:

1. Confirm that the final image exists at a user-accessible local artifact path
   for the current task, using its configured output directory when available.
2. Verify the actual file type, dimensions, and size. When the file was copied
   from another local source, compare hashes to prove the artifact is complete.
3. Present the verified artifact with an absolute local path that the current
   Codex client can render or download.

Treat the task as partially complete and explain the blocker if the image is
visually finished but cannot be exposed as an accessible artifact.

## PhotoCraft image editing

*Member skill: `photocraft` — Create, inspect, edit, composite, and export images through the photocraft-cli MCP server. Use for image work, layered artwork, photo edits, logos, and thumbnail assembly; combine with task-specific design skills when applicable.*

Use the native `photocraft-cli mcp` server for image work. Discover the connected
PhotoCraft tools before editing; a binary on PATH alone does not mean an MCP
connection is available. Follow explicit user tool choices and higher-priority
tool requirements.

### Connection and scope

The titstack default configuration starts the server with read and write roots
set to its startup directory. Install the CLI, rerun the titstack installer to
link this skill and refresh configuration, then restart Codex. No profile is
needed for ordinary CLI or desktop sessions. The optional
`codex --profile photocraft` makes a missing server a startup error. For another client,
configure `photocraft-cli mcp --automation-read-root <artwork-directory>
--automation-write-root <artwork-directory>` using that client's MCP settings.
Use paths within the granted roots; do not broaden them to bypass a denial.

If the connection is unavailable, explain the missing setup before using an
alternative. Do not silently replace the MCP workflow with shell image edits.
AI generation can supply new assets when needed; inspect those assets and use
PhotoCraft for supported assembly, finishing, and export operations.

### Editing workflow

1. Inspect supplied images and establish the required dimensions, format,
   transparency, and output destination. Preserve the source files.
2. Discover tool schemas, then use `session_list` and `doc_inspect` to identify
   existing work. Use `doc_open` for a source or `doc_new` for a new canvas.
   Confirm the target document before mutating a stateful session.
3. Use `command_list` with a relevant filter to discover engine command IDs,
   parameter documentation, and enabled state. Do not guess commands or assume
   every desktop feature is available through headless MCP.
4. Apply supported edits with `command_run`. Keep elements on separate layers
   when future edits or compositing require it. For experiments on existing
   work, discover and use `image.duplicate` to create a separate active copy.
5. Use `command_batch` only for known ordered steps. It is not atomic: successful
   earlier steps remain after failure. Inspect the document and results before
   retrying; undo does not reverse files already written to disk.
6. Render with `doc_render_preview` and inspect the actual image after meaningful
   edits. Check the final export at full resolution as well as its intended
   display size. A successful command is not proof of visual correctness.
7. Save layered work with `doc_save` as `.pcraft` and export the requested image
   with `doc_export`. Save before closing or ending the MCP session. Use new
   output paths unless replacing an existing deliverable is authorized.
8. Verify that the exported artifact exists, has the requested dimensions and
   format, and is accessible to the user. Deliver an absolute local artifact
   link or image embed, not only an MCP preview or a server-relative path.

### Image constraints

- For YouTube thumbnails, also use `youtube-thumbnail` for composition and
  visual acceptance criteria.
- Preserve supplied people as original pixels when identity preservation is
  required. Use separate generated backgrounds or objects and non-generative
  compositing; do not pass the person through generative edits.
- Report unsupported operations or file-access failures accurately. Discover a
  supported alternative before claiming the edit was performed.
- Headless MCP does not require the desktop application. Use desktop-only tools
  only when a separately configured bridge is available and needed.

## Gotchas

- The members disagree on one thing on purpose: `dwm-titus-debug` and `linux-sysadmin` inspect before they change, while the change skills act. Keep that split — diagnosis is read-only unless the user asks for a fix.
- `wayfinder` is explicit-invocation only in the upstream setup. Loading this pack is not an instruction to run it.
- `code-review` never replaces a review the repository requires; `autofix` fixes findings and does not push or reply without authorisation.

## Source projects

All members come from [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) at commit `b9b7fb0` (MIT, © 2026 titstack contributors): `youtube-thumbnail`, `photocraft`.
