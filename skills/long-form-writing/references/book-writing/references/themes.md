# Colour themes

A theme sets a book's entire palette in one move. The stylesheets
(`assets/book.css`, `assets/book_ornamental.css`) route every colour through CSS
custom properties, so overriding those properties recolours the cover, rules,
headings, tables, callouts, panels, the page surround and the watermark at once
— across the A4 master, the mobile edition, the PDFs and the designed DOCX. The
ornaments' border and vine colours and the poster follow the same theme.

## The shipped themes

| Name | Ground | Primary | Accent | Feel |
|---|---|---|---|---|
| `ember` | warm ivory | maroon | gold + marigold | the original look |
| `sage` | cream | deep forest green | brass | calm, natural |
| `indigo` | cool white | indigo | copper | scholarly |
| `slate` | pale grey | charcoal-teal | teal + amber | modern, technical |
| `plum` | blush white | aubergine | rose-gold | literary, rich |
| `terracotta` | sand | terracotta | ochre | warm, earthy |
| `midnight` | off-white | near-black | silver + brass | minimal |

`ember` is the default, so nothing changes unless you ask for a theme.

## Choosing a theme

Set `BOOK_THEME` in the environment, or put `"theme": "<name>"` in the content
module's `META`. The environment variable wins, so a whole build can be
recoloured without editing any file:

```
BOOK_THEME=sage python3 build_any.py content_book_en out.html
BOOK_THEME=sage python3 build_a4.py content_book_en "Book_-_A4_eBook.html"
BOOK_THEME=sage python3 make_docx_designed.py content_book_en out.docx en
```

Give each book — and each book in a series — its own theme, so a shelf of titles
does not read as one colour. Keep one theme for all languages of a single book,
so the editions match.

## How it works

`themes.py` holds a small `THEMES` dict. Each entry names only the core colours:

```python
"maroon": "#2f5140", "maroon_deep": "#20382b",
"gold": "#a98b4a", "gold_soft": "#c9b177",
"marigold": "#c07a2c", "marigold_soft": "#dc9d55",
"paper": "#f7f5ec", "ink": "#1e241c",
"cover1": "#31513f", "cover2": "#24402f", "cover3": "#152a1d",
```

`resolve(name)` derives everything else — the rules, zebra striping, panel
fills, page surround, watermark colour, footer colour, the darker back-cover
stops, and the on-dark text colours — by blending the core colours. `css_vars`
turns that into a `:root{...}` block the builders append to the stylesheet;
`rgb` gives the DOCX generators the same colours as RGB tuples.

## Adding a theme

Add one entry to `THEMES` in `themes.py`:

- `paper` — the page colour (near-white).
- `ink` — the body text colour (near-black).
- `maroon` / `maroon_deep` — the primary (headings, rules, table headers) and a
  darker shade for emphasis.
- `gold` / `gold_soft` — the secondary accent and a lighter tint.
- `marigold` / `marigold_soft` — the warm accent and a lighter tint (the
  ornamental pack uses these for its diamonds and dividers).
- `cover1` / `cover2` / `cover3` — the three stops of the cover gradient, light
  to dark.

Keep `paper` light and `ink` dark so contrast holds, and keep `maroon` dark
enough to read as a heading colour on `paper`. Everything else is derived, so a
well-chosen set of eight to ten colours is enough for a whole book.

Then check it: build the A4 master and the designed DOCX with `BOOK_THEME` set to
the new name, and run `verify_a4.py` / `verify_any.py` as usual. The watermark
and page-fill gates are colour-independent, so they should pass unchanged.
