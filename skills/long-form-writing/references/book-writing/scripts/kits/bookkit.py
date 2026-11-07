# -*- coding: utf-8 -*-
"""Shared front/back-matter kit for the Unlearning Series.
All three books use identical CSS and the same structural templates.
"""

SERIES = [
    {"num": 1, "word": "One", "title": "After the Bell",
     "subtitle": "The psychology of unlearning what was taught to us",
     "title_html": "After<br/>the Bell",
     "blurb": "How signals, consequences, and old stories install our reactions, and the four-move loop for changing them."},
    {"num": 2, "word": "Two", "title": "The Quiet Reward",
     "subtitle": "Relief, avoidance, and the habits they build",
     "title_html": "The Quiet<br/>Reward",
     "blurb": "A closer look at the invisible payment behind our most stubborn patterns: relief, and the avoidance it quietly funds."},
    {"num": 3, "word": "Three", "title": "Laying New Tracks",
     "subtitle": "Building the behaviour that lasts",
     "title_html": "Laying New<br/>Tracks",
     "blurb": "How to turn a single changed response into a durable, self-sustaining practice that survives stress and time."},
]

AUTHOR = "Dr. Sohil Momin"
CONTACT = "sohilmomin2000@gmail.com"
YEAR = "2026"

# Per-language labels for the designed DOCX (make_docx_designed.py). Any book
# supplies its own via this dict; the generator falls back to generic defaults.
L10N = {
    "series": "The Unlearning Series · Book {w}",
    "author": AUTHOR,
    "c_rights": "© 2026 Dr. Sohil Momin. All rights reserved.",
    "c_ed": "First edition, 2026.",
    "c_no": "No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic or mechanical, without the prior written permission of the author, except for brief quotations in a review or scholarly work.",
    "c_disc": "This book presents general information about learning and behaviour. It is not a substitute for diagnosis or treatment by a qualified mental-health professional.",
    "c_case": "The case material in this book is illustrative and composite. It does not describe any identifiable living person.",
    "contact": "Contact: sohilmomin2000@gmail.com",
    "about_h": "About the Author",
    "fore_h": "Foreword",
    "safety_l": "A note on psychological safety",
    "safety_p": "This book deals with conditioned fear, avoidance, and helplessness. For most readers this is safe and useful. If you find yourself flooded or unable to put the book down without distress, please pause and reach out to a licensed mental-health professional or a trusted person. Nothing here is a substitute for care from a qualified clinician.",
    "toc_h": "Contents", "gloss_h": "Glossary", "idx_h": "Index", "bib_h": "Bibliography",
    "font": "EB Garamond",
}

ABOUT_HTML = """
<div class="page-content">
  <div class="front-h">About the Author</div>
  <div class="author-body" style="max-width:560px;">
    <p><strong>Dr. Sohil Momin</strong>, BHMS, is a homoeopathic physician based in Vadodara, Gujarat. He has spent more than seventeen years in teaching hospitals, outpatient departments, and private practice, managing high-volume clinics, supervising clinical teams and interns, and coordinating hospital accreditation, clinical audits, and standard operating procedures. He is President of the Charity for Humanity Trust in Vadodara, which runs health screening drives, medical camps, and community outreach.</p>
    <p>He is a published author and translator: his clinical articles have appeared in Hpathy.com International Journal, The Homoeopathic Heritage, and Vital Informer, and he has translated two complete books from English into Gujarati. He has written hospital administration manuals and clinical audit frameworks published on Amazon KDP, and The Unlearning Series is his writing on how people learn, unlearn, and change, and how those lessons can be put to work in ordinary life. He serves as Resident Medical Officer and healthcare administrator.</p>
  </div>
</div>
"""

def cover(meta):
    return f"""
<div class="page-content">
  <div class="bigname">The Unlearning Series &middot; Book {meta['word']}</div>
  <div class="sheet-rule"></div>
  <h1>{meta['title_html']}</h1>
  <div class="subtitle">{meta['subtitle']}</div>
  <div class="author">{AUTHOR}</div>
  <div class="imprint">{meta['imprint']}</div>
</div>
"""

def title_page(meta):
    return f"""
<div class="page-content">
  <div class="center-page title-page">
    <h1>{meta['title']}</h1>
    <div class="subtitle">{meta['subtitle']}</div>
    <div class="author">{AUTHOR}</div>
    <div class="imprint">The Unlearning Series &middot; Book {meta['word']}</div>
  </div>
</div>
"""

def copyright_page(meta):
    return f"""
<div class="page-content">
  <div class="center-page">
    <div class="copy-page" style="max-width:470px;">
      <p><strong>{meta['title']}: {meta['subtitle']}</strong></p>
      <p>&copy; {YEAR} {AUTHOR}. All rights reserved.</p>
      <p>First edition, {YEAR}.</p>
      <p>No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic or mechanical, without the prior written permission of the author, except for brief quotations in a review or scholarly work.</p>
      <p>This book presents general information about learning and behaviour. It is not a substitute for diagnosis or treatment by a qualified mental-health professional. If you are in distress, please reach out to a licensed clinician or a trusted support service in your area.</p>
      <p>The case material in this book is illustrative and composite. It does not describe any identifiable living person.</p>
      <p>Contact: {CONTACT}</p>
    </div>
  </div>
</div>
"""

def dedication(meta):
    return f"""
<div class="page-content">
  <div class="center-page dedication">
    <p>{meta['dedication']}</p>
  </div>
</div>
"""

def foreword(meta):
    pre = "".join(f"<p>{p}</p>" for p in meta['foreword_pre'])
    post = "".join(f"<p>{p}</p>" for p in meta['foreword_post'])
    return f"""
<div class="page-content">
  <div class="front-h">Foreword</div>
  <h2 style="margin-top:0;">{meta['foreword_head']}</h2>
  {pre}
  <div class="callout">
    <div class="clabel">A note on psychological safety</div>
    <p>This book deals with conditioned fear, avoidance, and helplessness. For most readers, reading about these subjects is safe and useful. For some, it can stir up material that deserves a trained listener rather than a paperback.</p>
    <p>If you find yourself flooded, dissociating, or unable to put the book down without distress, please pause and reach out to a licensed mental-health professional or a trusted person in your life. If you are in crisis, contact your local emergency number or a crisis line in your region. Nothing in these pages is a substitute for care from a qualified clinician, and no exercise here should be attempted in place of treatment.</p>
    <p>Read at the pace your nervous system can hold. There is no prize for speed.</p>
  </div>
  {post}
</div>
"""

def back_cover(meta):
    return f"""
<div class="page-content">
  <h2>{meta['title']}</h2>
  {''.join(f'<p>{p}</p>' for p in meta['back_paras'])}
  <div class="series-line">The Unlearning Series &middot; Book {meta['word']}</div>
</div>
"""

def series_page(current_num):
    cards = []
    for b in SERIES:
        mark = " &middot; This book" if b["num"] == current_num else ""
        cards.append(f"""<div class="series-card">
        <div class="sc-title">{b['title']}{mark}</div>
        <div class="sc-sub">Book {b['word']} &middot; {b['subtitle']}</div>
        <p>{b['blurb']}</p>
      </div>""")
    return f"""
<div class="page-content">
  <div class="center-page" style="align-items:stretch; text-align:left;">
    <div class="series">
      <h1>Also in This Series</h1>
      <p class="intro">The Unlearning Series turns the findings of learning research into plain, usable practice. Each book stands alone and can be read on its own.</p>
      {''.join(cards)}
      <p style="font-size:13px; color:var(--ink-faint); margin-top:16px;">All three titles are part of the Unlearning Series.</p>
    </div>
  </div>
</div>
"""

def build_specials(meta):
    return {
        "cover": cover(meta),
        "title": title_page(meta),
        "copyright": copyright_page(meta),
        "dedication": dedication(meta),
        "about": ABOUT_HTML,
        "foreword": foreword(meta),
    }

def build_back(meta):
    return {
        "backcover": back_cover(meta),
        "series": series_page(meta["num"]),
    }
