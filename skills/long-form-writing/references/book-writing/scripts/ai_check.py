# -*- coding: utf-8 -*-
"""AI-tell and plagiarism heuristics for a manuscript.

Reports measurable, honest numbers — it does NOT claim any AI detector's output
and it does NOT certify originality. It measures:

  * sentence-length burstiness (mean, sd, min/max, short/long counts)
  * em-dash density per 1,000 words
  * stock "AI-tell" phrases
  * internal n-gram repetition (whole-book dedup)
  * verbatim overlap with a supplied draft (the author's own carried-forward text)
  * the inventory of quoted phrases (must all be short and attributed)

Usage:
    python3 ai_check.py <content_module> [--draft path/to/supplied.html|.md|.txt]
                        [--json out.json] [--report out.md]

Exit code is 0 always; read the printed numbers (or the JSON) and fix the flags.
"""
import re, io, sys, json, collections


def strip_tags(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&[a-z]+;", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def load_module_text(path):
    """Text of the flow sections + back matter of a content module."""
    import importlib.util, os as _os
    d = _os.path.dirname(_os.path.abspath(path))
    if d not in sys.path:
        sys.path.insert(0, d)
    spec = importlib.util.spec_from_file_location("m", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    secs = [m.INTRO] + list(m.CHAPTERS) + [m.CLOSING]
    text = " ".join(strip_tags(b) for s in secs for b in s["blocks"])
    extra = " ".join(strip_tags("%s %s" % (t, d)) for t, d in getattr(m, "GLOSSARY", []))
    extra += " " + " ".join(strip_tags(r) for r in getattr(m, "BIBLIOGRAPHY", []))
    return text, extra


def words(t):
    return re.findall(r"[A-Za-z0-9'’-]+", t.lower())


def sentences(text):
    t = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'A-Z0-9])", t)
    return [p.strip() for p in parts if len(p.strip()) > 1]


def ngrams(ws, n):
    return [" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1)]


BANNED = ["delve", "tapestry", "underscore", "testament", "realm", "navigate",
          "robust", "leverage", "comprehensive", "ever-evolving", "shed light",
          "foster", "seamless", "crucial", "pivotal", "multifaceted", "moreover",
          "furthermore", "it is important to note", "in conclusion", "a testament to"]


def analyse(module_path, draft_path=None):
    new, extra = load_module_text(module_path)
    nw = words(new)
    sents = sentences(new)
    lens = [len(words(s)) for s in sents] or [0]
    mean = sum(lens) / len(lens)
    sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5
    em = new.count("—") + new.count("–")
    low = new.lower()
    rep = collections.Counter(ngrams(nw, 6))
    out = {
        "words": len(nw),
        "sentences": len(sents),
        "mean_sentence_len": round(mean, 2),
        "sentence_len_sd": round(sd, 2),
        "min_sentence": min(lens),
        "max_sentence": max(lens),
        "short_sentences_lt6": sum(1 for x in lens if x < 6),
        "long_sentences_gt25": sum(1 for x in lens if x > 25),
        "em_dashes": em,
        "em_dashes_per_1000": round(1000.0 * em / max(1, len(nw)), 2),
        "banned_hits": {b: low.count(b) for b in BANNED if low.count(b)},
        "internal_6gram_repeats": sum(1 for c in rep.values() if c > 1),
        "repeat_examples": [g for g, c in rep.items() if c > 1][:12],
        "quotes": re.findall(r'"([^"]{8,200})"', new),
    }
    if draft_path:
        try:
            raw = io.open(draft_path, encoding="utf-8", errors="ignore").read()
            ow = words(strip_tags(raw))
            oset = set(ngrams(ow, 8))
            retained = [g for g in ngrams(nw, 8) if g in oset]
            out["draft_words"] = len(ow)
            out["retained_8grams_from_draft"] = len(retained)
            out["retained_examples"] = retained[:8]
        except OSError as e:
            out["draft_error"] = str(e)
    return out


def verdict(d):
    """A short, honest reading of the numbers."""
    notes = []
    notes.append("burstiness sd %.1f (human-like is high; flat machine prose ~4-6)" % d["sentence_len_sd"])
    notes.append("em-dash density %.2f / 1000 (cap ~6)" % d["em_dashes_per_1000"])
    notes.append("stock AI phrases: %d" % sum(d["banned_hits"].values()))
    notes.append("internal 6-gram repeats: %d (should be structural only)" % d["internal_6gram_repeats"])
    if "retained_8grams_from_draft" in d:
        notes.append("verbatim overlap with supplied draft: %d 8-grams (author's own text)"
                     % d["retained_8grams_from_draft"])
    return notes


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    mod = argv[1]
    draft = None
    jout = rout = None
    i = 2
    while i < len(argv):
        if argv[i] == "--draft":
            draft = argv[i + 1]; i += 2
        elif argv[i] == "--json":
            jout = argv[i + 1]; i += 2
        elif argv[i] == "--report":
            rout = argv[i + 1]; i += 2
        else:
            i += 1
    d = analyse(mod, draft)
    print(json.dumps(d, indent=1))
    print("\nREADING:")
    for n in verdict(d):
        print("  -", n)
    if jout:
        io.open(jout, "w", encoding="utf-8").write(json.dumps(d, indent=1))
    if rout:
        lines = ["# AI-tell and plagiarism heuristics", "",
                 "Measured numbers (not a detector verdict, not a guarantee):", ""]
        lines += ["- %s: **%s**" % (k, v) for k, v in d.items() if k not in ("quotes", "repeat_examples", "retained_examples")]
        lines += ["", "Reading:"] + ["- " + n for n in verdict(d)]
        io.open(rout, "w", encoding="utf-8").write("\n".join(lines))


if __name__ == "__main__":
    main(sys.argv)
