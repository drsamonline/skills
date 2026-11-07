# -*- coding: utf-8 -*-
"""Gujarati edition builder.

The generic builder (build_any.py) reads the language from the content module's
META["lang"] and picks the matching kit (`bookkit_gu`), so this file is now just
a thin alias kept for compatibility. Prefer:

    BOOK_DIR=/path/to/project python3 build_any.py content_<book>_gu out.html
"""
import sys
from build_any import build

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    build(sys.argv[1], sys.argv[2])
