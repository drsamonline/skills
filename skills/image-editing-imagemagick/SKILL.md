---
name: image-editing-imagemagick
description: "Process and manipulate images from the command line with ImageMagick: resize, crop, convert formats, compose, batch-process folders, strip metadata, and read image information. Use when a task involves thumbnails, wallpapers, format conversion, or bulk image operations. Not for generative editing."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Image editing with ImageMagick"
  category: "media-design"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "image-manipulation-image-magick"
---

# Image editing with ImageMagick

A small, dependable toolbox for the mechanical parts of image work. Nearly every mistake here is a quoting mistake or a missing dimension check, so the method is deliberately literal.

## When to use

- Images need resizing, cropping, conversion or batch treatment.
- Thumbnails, contact sheets, wallpapers or web-sized assets are wanted.
- Image dimensions, colour space or metadata must be read.

## Method

1. Resolve the executable first: prefer `magick` on PATH, fall back to the common install location, and use `convert` only on ImageMagick 6 systems.
2. Read the image information (dimensions, format, colourspace) before processing, so an unnecessary upscale or a wrong-format conversion is caught early.
3. Quote every path — spaces and brackets in filenames are the usual failure.
4. Resize with an explicit geometry and a filter choice; keep aspect ratio unless the user asked for a crop.
5. For batch work, write the loop against a glob, process into a separate output directory, and print a per-file result line.
6. Strip or preserve metadata deliberately; state which you did.
7. Verify the output dimensions and file size after the run, not just the exit code.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`image-manipulation-image-magick`](references/image-manipulation-image-magick/) | The ImageMagick command reference: executable resolution, info, resize, batch, conversion and metadata. |

## Key files / entry points

- `references/image-manipulation-image-magick/` — command reference for info, resize, convert, crop, compose and batch patterns.

## Gotchas

- Unquoted paths break on spaces.
- Upscaling from a small source is a silent quality loss — check dimensions first.
- `convert` and `magick` are not interchangeable across major versions.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `image-manipulation-image-magick` — no licence file shipped with the source
