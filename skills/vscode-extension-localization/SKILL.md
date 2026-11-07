---
name: vscode-extension-localization
description: "Localise a VS Code extension the way the platform expects: the three localization approaches (package manifest strings, the `vscode-nls` runtime bundle, and the language-pack/bundle mechanism), when to use each, and how to keep them consistent as new resources appear. Use when an extension must support multiple languages or its strings need externalising."
license: "per source — see references/*/LICENSE"
metadata:
  title: "VS Code extension localization"
  category: "code-quality"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "vscode-ext-localization"
---

# VS Code extension localization

Three mechanisms, chosen by the kind of resource being localised — not one mechanism applied everywhere. The rule that keeps them coherent: when a new localizable resource is created or updated, the matching localization is updated in the same change.

## When to use

- An extension needs to ship in more than one language.
- Strings are hard-coded and must be externalised.
- An existing localisation has drifted from the manifest or the bundle.

## Method

1. Classify each string by resource: manifest contributions (commands, titles, descriptions, configuration) versus runtime strings (messages, prompts, errors).
2. For manifest contributions, use the `package.nls.json` / `package.nls.<locale>.json` mechanism and reference keys from `package.json`.
3. For runtime strings, use the `vscode-nls` bundle (`out/nls.metadata.*`) generated at build time; never hand-edit generated metadata.
4. Keep one key convention and never reuse a key for a different meaning across locales.
5. Localise in the same change as the code: a new string and its key land together.
6. Never concatenate localised fragments to build a sentence — word order differs by language; use whole-sentence placeholders.
7. Verify by launching the extension with a non-English locale and checking both the command palette entries and the runtime messages.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`vscode-ext-localization`](references/vscode-ext-localization/) | The three VS Code localization approaches, selection rules, and the keep-in-sync convention. |

## Key files / entry points

- `references/vscode-ext-localization/` — the three approaches, when each applies, and the consistency rule.

## Gotchas

- Concatenated fragments produce broken grammar in most languages.
- Editing generated NLS metadata is overwritten on the next build.
- A key reused for two meanings cannot be translated correctly.
- Manifest strings are invisible until the extension host reloads.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `vscode-ext-localization` — no licence file shipped with the source
