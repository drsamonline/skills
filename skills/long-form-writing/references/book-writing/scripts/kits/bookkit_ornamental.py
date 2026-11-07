# -*- coding: utf-8 -*-
"""Front/back matter for *Life Is a Comedy*."""
import ornaments

AUTHOR = "Dr. Sohil Momin"
CONTACT = "sohilmomin2000@gmail.com"
YEAR = "2026"


def cover(meta):
    return f'''
<div class="page-content">
  <div class="cover-inner">
    <div class="cover-garland">{ornaments.marigold_garland(n=11, w=520)}</div>
    <div class="cover-kicker">{meta['kicker']}</div>
    <h1>{meta['title_html']}</h1>
    <div class="cover-sub">{meta['subtitle']}</div>
    <div class="cover-rule"></div>
    <div class="cover-marigold">{ornaments.marigold_motif(size=56)}</div>
    <div class="cover-author">{AUTHOR}</div>
    <div class="cover-imprint">{meta['imprint']}</div>
  </div>
</div>
'''


def title_page(meta):
    return f'''
<div class="page-content">
  <div class="center-page title-page">
    <div class="orn-monogram">{ornaments.monogram("SM", size=104)}</div>
    <h1>Life Is a Comedy</h1>
    <div class="subtitle">A Tragedy Told Lightly</div>
    <div class="orn-flourish">{ornaments.rule_flourish()}</div>
    <div class="author">{AUTHOR}</div>
    <div class="imprint">{meta['imprint']} &middot; A Memoir</div>
  </div>
</div>
'''


def copyright_page(meta):
    return f'''
<div class="page-content">
  <div class="center-page">
    <div class="copy-page">
      <p class="cp-title">Life Is a Comedy: A Tragedy Told Lightly</p>
      <p>&copy; {YEAR} {AUTHOR}. All rights reserved.</p>
      <p>First edition, {YEAR}.</p>
      <p>No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means — electronic, mechanical, photocopying, recording, or otherwise — without the prior written permission of the author, except for brief quotations in a review or scholarly work.</p>
      <p class="cp-note">This is a work of memoir. Scenes and conversations are rendered from memory, and memory is not a court of record.</p>
      <p>Cover and interior design set in EB Garamond and Cinzel.</p>
      <p>Contact: {CONTACT}</p>
    </div>
  </div>
</div>
'''


def epigraph(meta):
    return f'''
<div class="page-content">
  <div class="epigraph">
    <div class="orn-marigold">{ornaments.marigold_motif(size=64)}</div>
    <div class="e-label">Before the Curtain</div>
    <blockquote>&ldquo;Life is a comedy. The tragedy is the timing. The laugh, if you&rsquo;re brave enough to let it out, is the curtain call.&rdquo;</blockquote>
    <div class="e-src">From the Epilogue</div>
  </div>
</div>
'''


def back_cover(meta):
    return meta.get("_back_html", "")


def build_front(meta, about_html, back_html):
    return {
        "cover": cover(meta),
        "title": title_page(meta),
        "copyright": copyright_page(meta),
        "epigraph": epigraph(meta),
    }


def back_cover(meta):
    return meta.get("_back_html", "")
