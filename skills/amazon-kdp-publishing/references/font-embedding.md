# Font embedding — the Type 3 trap

A KDP interior can be rejected for fonts even when every font is "embedded" and
the PDF looks perfect on screen. The cause is **Type 3**, and it is worth
understanding because it is invisible until a printer refuses the file.

`kdp_build.py` now checks every file it produces and reports the result in
`07_QA_Report.md`. If that section says FAIL, do not upload.

## What the types mean

| Embedded as | Print services |
|---|---|
| CID TrueType / TrueType | **accepted** — what you want |
| Type 1 / CFF | accepted |
| **Type 3** | **rejected** — glyphs are drawing procedures, not a font |
| not embedded | **rejected** |

Type 3 is valid PDF and renders correctly everywhere. That is why it slips
through: the file opens, looks right, and dies at the printer.

## Why Chromium makes them

Chromium writes a **variable font** as Type 3. Google Fonts serves most families
as variable fonts now, so an `@font-face` pointing at a Google Fonts woff2 will
do it.

Measured on a real 750-page interior set in EB Garamond:

| Setup | Type 3 fonts |
|---|---|
| `@font-face` with base64 woff2 (variable) | **11** |
| the same font installed as a system font, still variable | **4** |
| **static instances installed as system fonts** | **0** |

The middle row is the trap. Installing the font is not enough — a variable font
stays variable. The axis must be pinned.

## The fix

```python
from fontTools.varLib.instancer import instantiateVariableFont
static = instantiateVariableFont(variable_font, {"wght": 400})
```

That drops the `fvar` table and bakes the weight in. Chromium then embeds it as
CID TrueType.

Three things must all be true:

1. **The font is a static instance.** Not the variable original.
2. **`@font-face` is gone from the CSS.** If the web font is still declared it
   wins over the system font and you are back to Type 3. The builder's
   `build_interior.py` inlines whatever CSS you give it, so hand it a copy with
   the `@font-face` blocks removed.
3. **fontconfig actually sees the font.** A minimal container may not scan
   `~/.local/share/fonts`:

   ```bash
   export FONTCONFIG_FILE=~/.config/fontconfig/fonts.conf
   fc-cache -f
   fc-match "EB Garamond"      # must name YOUR font, not a fallback
   ```

   If `fc-match` names a fallback, the render succeeds and is set in the wrong
   typeface. This is how a cover ends up in Liberation Serif while you believe
   it is Garamond.

The companion skill **`print-font-safety`** automates all three
(`fontfix.py`, `printrender.py`, `fontaudit.py`). Use it rather than
re-deriving this.

## Cover fonts are a separate failure

The cover builder's font stack used to be `Georgia, 'Times New Roman', serif`.
On a machine with neither, it silently fell back to Liberation Serif — a
perfectly plausible serif, and the wrong one. The stack now leads with
`'EB Garamond'`, but the same rule applies to any cover you customise: **name
the font you actually installed**, and check `pdffonts` on the cover too.

## Verifying

```bash
pdffonts interior.pdf
```

Every row must show `emb = yes` and a type of `CID TrueType`, `TrueType` or
`Type 1`. Any `Type 3` and it is not ready.

`scripts/fontaudit.py` automates that and exits non-zero, so it can gate a build:

```bash
python3 scripts/fontaudit.py build/            # a whole folder
```

## Side effect worth knowing

Changing from a variable font to a static instance shifts metrics very slightly.
A 749-page book became 750 pages. **Recompute the spine and rebuild the cover**
whenever the font changes — a cover cut for the old page count will not wrap.
