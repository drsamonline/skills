# When you only have the PDF, not the source

The clean fix needs the source: you re-render from HTML with static fonts. If a
book exists only as a finished PDF, your options change. Be honest with yourself
about which case you are in before promising anything.

## Decide which case you are in

```bash
python3 scripts/fontaudit.py book.pdf
```

- **Type 3 fonts present** → you cannot repair the PDF itself in any reliable
  way. Go to the options below.
- **Fonts embedded, no Type 3** → nothing to fix. The rejection was about
  something else: trim, bleed, spine, page count, margins. Audit those instead.

## Option 1 — find the source (best)

Most books built this way have an HTML master, a DOCX, or a LaTeX/Markdown
source somewhere. Search before giving up:

```bash
find . -name '*.html' -o -name '*.docx' -o -name '*.tex' -o -name '*.md' | head
```

If you find the HTML master and its stylesheet, the fix is the normal path:
`fontfix.py` then `printrender.py`. You get a clean file and a repeatable build.

## Option 2 — re-render from the DOCX

If the DOCX master is the real source, convert it with LibreOffice, which
embeds fonts as TrueType:

```bash
soffice --headless --convert-to pdf book.docx
python3 scripts/fontaudit.py book.pdf
```

LibreOffice generally does not produce Type 3, but it re-flows the book, so the
page count — and therefore the spine and the cover — will change. Recompute the
cover afterwards.

## Option 3 — flatten the pages to images (last resort)

You can rasterise the Type 3 pages into images and rebuild the PDF. This always
works, and it always costs you:

- the text stops being selectable or searchable
- the file gets much larger (roughly 10–20× for a text book)
- at anything under 300 DPI the type looks soft on paper

Only do this if the book is out of print elsewhere and you just need a file the
printer will accept.

```bash
pdftoppm -r 300 -png book.pdf page          # one PNG per page
python3 -c "import img2pdf,sys; open('flat.pdf','wb').write(img2pdf.convert(sorted(__import__('glob').glob('page-*.png'))))"
```

Check the result: `pdfinfo flat.pdf` must report the same page size, and
`pdffonts flat.pdf` will report **no fonts at all** — that is expected, and it
is acceptable to printers because there is no font to embed.

## Option 4 — ask the original builder

If the book was produced by a tool or a person, the source almost certainly
still exists. Rebuilding from source is faster and better than any repair, and
it fixes the cause rather than the symptom.

## What not to do

- **Do not try to convert Type 3 to TrueType inside the PDF.** There is no
  reliable tool for it; the glyph programs would have to be re-outlined into a
  font, which loses hinting and often changes spacing.
- **Do not re-save through a "PDF optimiser".** Most of them preserve Type 3,
  and some strip embedding entirely, which is worse.
- **Do not assume a passing screen preview means a passing print file.** Type 3
  looks perfect on screen. That is the whole problem.
