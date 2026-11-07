---
name: diagram-generator
description: "Turn a description into an Excalidraw `.excalidraw` JSON diagram: flowcharts, system architecture, relationship maps, mind maps, org and process diagrams. Use when asked to 'create a diagram', 'draw a flowchart', 'visualise this process', or to output a file that opens directly in Excalidraw."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Diagram generator (Excalidraw)"
  category: "media-design"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "excalidraw-diagram-generator"
---

# Diagram generator (Excalidraw)

The output is a JSON scene, not an image: it opens in Excalidraw and stays editable. That means layout is explicit — coordinates, sizes, arrows bound to elements — and the skill's value is the layout discipline plus the element-count limits that keep a diagram readable.

## When to use

- A process, architecture, relationship map or mind map should be drawn and remain editable.
- The user wants a file they can open in Excalidraw rather than a rendered picture.

## Method

1. Understand the request and pick the diagram type from the intent: flowchart for order of steps, architecture for components and boundaries, relationship map for data flow between entities (no process order), mind map for hierarchy from one centre.
2. Extract the structured information first — nodes, edges, groups, labels — before writing any JSON.
3. Choose a layout: vertical flow for processes, grid for relationship maps, radial for mind maps. Keep spacing even; do not let elements overlap or arrows cross where avoidable.
4. Generate the JSON with bound arrows (start/end element ids), `fontFamily: 5` on every text element, and explicit widths and heights.
5. Keep the element count inside the readability guidance; split a diagram that exceeds it rather than shrinking the type.
6. For cloud or vendor architectures, use the pre-made icon libraries so the icons are standard rather than hand-drawn.
7. Save with the edit suffix enabled so an existing file is never overwritten, and tell the user how to open it.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`excalidraw-diagram-generator`](references/excalidraw-diagram-generator/) | Diagram type selection, JSON generation rules, layouts, element-count guidance and worked examples. |

## Key files / entry points

- `references/excalidraw-diagram-generator/` — the JSON schema, element rules, layout patterns, examples and troubleshooting.

## Gotchas

- A relationship diagram must not imply process order — use plain connections.
- Text without `fontFamily: 5` looks inconsistent next to Excalifont labels.
- Icon JSON is large; keep it out of context and let the script splice it in.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `excalidraw-diagram-generator` — no licence file shipped with the source
