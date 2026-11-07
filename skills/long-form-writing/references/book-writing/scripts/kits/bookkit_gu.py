# -*- coding: utf-8 -*-
"""Gujarati front/back-matter kit (mirrors bookkit_hi.py)."""

SERIES = [
    {"num": 1, "word": "એક", "title": "ઘંટ વાગ્યા પછી",
     "subtitle": "આપણને જે શીખવવામાં આવ્યું તેને અનલર્ન કરવાનું મનોવિજ્ઞાન",
     "title_html": "ઘંટ વાગ્યા<br/>પછી",
     "blurb": "સંકેત, પરિણામો અને જૂની વાર્તાઓ આપણી પ્રતિક્રિયાઓ કેવી રીતે ઘડે છે, અને એ બદલવાની ચાર-ચાલની રીત."},
    {"num": 2, "word": "બે", "title": "શાંત ઇનામ",
     "subtitle": "રાહત, ટાળવું, અને એનાથી બનતી ટેવો",
     "title_html": "શાંત<br/>ઇનામ",
     "blurb": "આપણી સૌથી જિદ્દી ટેવો પાછળ છુપાયેલા અદૃશ્ય ઇનામ પર એક નજીકની નજર: રાહત, અને એ ચૂપચાપ ધરાવતું ટાળવું."},
    {"num": 3, "word": "ત્રણ", "title": "નવા રસ્તા",
     "subtitle": "એવું વર્તન બનાવવું જે ટકે",
     "title_html": "નવા<br/>રસ્તા",
     "blurb": "એક બદલાયેલી પ્રતિક્રિયાને ટકાઉ, સ્વયં-ટકતી ટેવમાં કેવી રીતે ફેરવવી જે તણાવ અને સમય સાથે ટકે."},
]

AUTHOR = "ડૉ. સોહિલ મોમિન"
CONTACT = "sohilmomin2000@gmail.com"
YEAR = "2026"
BRAND = "ધ અનલર્નિંગ સીરીઝ"

# Per-language labels for the designed DOCX (make_docx_designed.py).
L10N = {
    "series": "ધ અનલર્નિંગ સીરીઝ · પુસ્તક {w}",
    "author": AUTHOR,
    "c_rights": "© 2026 ડૉ. સોહિલ મોમિન. સર્વ હકો સ્વાધીન.",
    "c_ed": "પ્રથમ આવૃત્તિ, 2026.",
    "c_no": "આ પ્રકાશનનો કોઈ પણ ભાગ લેખકની લેખિત પરવાનગી વગર નકલ, સંગ્રહિત કે પ્રસારિત કરી શકાય નહીં, સિવાય કે સમીક્ષા કે શૈક્ષણિક કાર્યમાં ટૂંકા અવતરણો માટે.",
    "c_disc": "આ પુસ્તક શીખવા અને વર્તન વિશે સામાન્ય માહિતી આપે છે. તે લાયક માનસિક-આરોગ્ય નિષ્ણાતના નિદાન કે સારવારનો વિકલ્પ નથી.",
    "c_case": "આ પુસ્તકની કેસ-સામગ્રી ફક્ત ઉદાહરણ માટે છે અને ઘણા લોકોની વાતો ભેગી કરીને બનાવેલી છે.",
    "contact": "સંપર્ક: sohilmomin2000@gmail.com",
    "about_h": "લેખક વિશે",
    "fore_h": "પ્રસ્તાવના",
    "safety_l": "માનસિક સલામતી પર એક નોંધ",
    "safety_p": "આ પુસ્તક કન્ડિશન્ડ ડર, ટાળવાની ટેવ અને અસહાયતા વિશે છે. મોટા ભાગના વાચકો માટે આ સુરક્ષિત છે. જો તમે લાગણીઓમાં ડૂબી રહ્યા હો કે તકલીફ અનુભવો, તો કૃપા કરીને લાઇસન્સ પ્રાપ્ત માનસિક-આરોગ્ય નિષ્ણાત કે ભરોસાપાત્ર વ્યક્તિ સાથે વાત કરો. આ પાનાંમાં લખેલી કોઈ પણ વાત લાયક ક્લિનિશિયનની સંભાળની જગ્યા લઈ શકે નહીં.",
    "toc_h": "સૂચિ", "gloss_h": "શબ્દાવલી", "idx_h": "અનુક્રમણિકા", "bib_h": "ગ્રંથસૂચિ",
    "font": "Noto Sans Gujarati",
}

ABOUT_HTML = """
<div class="page-content">
  <div class="front-h">લેખક વિશે</div>
  <div class="author-body" style="max-width:560px;">
    <p><strong>ડૉ. સોહિલ મોમિન</strong>, બી.એચ.એમ.એસ., વડોદરા, ગુજરાતમાં રહેતા એક હોમિયોપેથિક ચિકિત્સક છે. તેમણે સત્તર વર્ષથી વધુ સમય ટીચિંગ હોસ્પિટલો, ઓપીડી અને ખાનગી પ્રેક્ટિસમાં વિતાવ્યો છે, જ્યાં તેમણે વ્યસ્ત ક્લિનિક ચલાવ્યાં, ક્લિનિકલ ટીમો અને ઇન્ટર્નોને માર્ગદર્શન આપ્યું, અને હોસ્પિટલ માન્યતા, ક્લિનિકલ ઓડિટ તથા સ્ટાન્ડર્ડ ઓપરેટિંગ પ્રોસિજર (એસઓપી)નું સંકલન કર્યું. તેઓ વડોદરાની ચેરિટી ફોર હ્યુમેનિટી ટ્રસ્ટના પ્રમુખ છે, જે આરોગ્ય તપાસ શિબિરો, તબીબી કેમ્પ અને સામૂહિક સેવા ચલાવે છે.</p>
    <p>તેઓ એક પ્રકાશિત લેખક અને અનુવાદક છે: તેમના ક્લિનિકલ લેખો Hpathy.com International Journal, The Homoeopathic Heritage અને Vital Informerમાં પ્રકાશિત થયા છે, અને તેમણે અંગ્રેજીથી ગુજરાતીમાં બે આખાં પુસ્તકોનો અનુવાદ કર્યો છે. તેમણે Amazon KDP પર હોસ્પિટલ વ્યવસ્થાપનની પુસ્તિકાઓ અને ક્લિનિકલ ઓડિટ માળખાં પ્રકાશિત કર્યાં છે, અને ધ અનલર્નિંગ સીરીઝ એ તેમનું લેખન છે કે લોકો કેવી રીતે શીખે છે, અનલર્ન કરે છે અને બદલાય છે. તેઓ રેસિડેન્ટ મેડિકલ ઓફિસર અને હોસ્પિટલ એડમિનિસ્ટ્રેટર તરીકે કાર્યરત છે.</p>
  </div>
</div>
"""

def cover(meta):
    return f"""
<div class="page-content">
  <div class="bigname">{BRAND} &middot; પુસ્તક {meta['word']}</div>
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
    <div class="imprint">{BRAND} &middot; પુસ્તક {meta['word']}</div>
  </div>
</div>
"""

def copyright_page(meta):
    return f"""
<div class="page-content">
  <div class="center-page">
    <div class="copy-page" style="max-width:470px;">
      <p><strong>{meta['title']}: {meta['subtitle']}</strong></p>
      <p>&copy; {YEAR} {AUTHOR}. સર્વ હકો સ્વાધીન.</p>
      <p>પ્રથમ આવૃત્તિ, {YEAR}.</p>
      <p>આ પ્રકાશનનો કોઈ પણ ભાગ લેખકની લેખિત પરવાનગી વગર, કોઈ પણ સ્વરૂપમાં કે કોઈ પણ રીતે (ઇલેક્ટ્રોનિક કે યાંત્રિક) નકલ, સંગ્રહિત કે પ્રસારિત કરી શકાય નહીં, સિવાય કે સમીક્ષા કે શૈક્ષણિક કાર્યમાં ટૂંકા અવતરણો માટે.</p>
      <p>આ પુસ્તક શીખવા અને વર્તન વિશે સામાન્ય માહિતી આપે છે. તે લાયક માનસિક-આરોગ્ય નિષ્ણાતના નિદાન કે સારવારનો વિકલ્પ નથી. જો તમે મુશ્કેલીમાં હો, તો કૃપા કરીને તમારા વિસ્તારના લાઇસન્સ પ્રાપ્ત ક્લિનિશિયન કે ભરોસાપાત્ર સહાય સેવાનો સંપર્ક કરો.</p>
      <p>આ પુસ્તકની કેસ-સામગ્રી ફક્ત ઉદાહરણ માટે છે અને ઘણા લોકોની વાતો ભેગી કરીને બનાવેલી છે. તેમાં કોઈ ઓળખી શકાય તેવી જીવતી વ્યક્તિનું વર્ણન નથી.</p>
      <p>સંપર્ક: {CONTACT}</p>
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
  <div class="front-h">પ્રસ્તાવના</div>
  <h2 style="margin-top:0;">{meta['foreword_head']}</h2>
  {pre}
  <div class="callout">
    <div class="clabel">માનસિક સલામતી પર એક નોંધ</div>
    <p>આ પુસ્તક કન્ડિશન્ડ ડર, ટાળવાની ટેવ અને અસહાયતા વિશે છે. મોટા ભાગના વાચકો માટે, આ વિષયો વિશે વાંચવું સુરક્ષિત અને ઉપયોગી છે. પણ કેટલાક માટે, તે એવી વસ્તુઓ જગાડી શકે છે જે પુસ્તકને બદલે કોઈ તાલીમબદ્ધ સાંભળનાર સાથે વહેંચવી જોઈએ.</p>
    <p>જો તમને લાગે કે તમે લાગણીઓમાં ડૂબી રહ્યા છો, પોતાને અલગ પડેલા અનુભવો છો, અથવા તકલીફ વગર આ પુસ્તક મૂકી શકતા નથી, તો કૃપા કરીને થોડું અટકો અને લાઇસન્સ પ્રાપ્ત માનસિક-આરોગ્ય નિષ્ણાત કે તમારા જીવનની કોઈ ભરોસાપાત્ર વ્યક્તિ સાથે વાત કરો. જો તમે સંકટમાં હો, તો તમારા સ્થાનિક ઇમરજન્સી નંબર કે તમારા વિસ્તારની કોઈ ક્રાઇસિસ લાઇનનો સંપર્ક કરો. આ પાનાંમાં લખેલી કોઈ પણ વાત લાયક ક્લિનિશિયનની સંભાળની જગ્યા લઈ શકે નહીં, અને અહીં આપેલી કોઈ પણ કસરત સારવારની જગ્યાએ ન કરવી.</p>
    <p>તમારા નર્વસ સિસ્ટમની ક્ષમતા પ્રમાણે વાંચો. ઝડપથી વાંચવાનું કોઈ ઇનામ નથી.</p>
  </div>
  {post}
</div>
"""

def back_cover(meta):
    return f"""
<div class="page-content">
  <h2>{meta['title']}</h2>
  {''.join(f'<p>{p}</p>' for p in meta['back_paras'])}
  <div class="series-line">{BRAND} &middot; પુસ્તક {meta['word']}</div>
</div>
"""

def series_page(current_num):
    cards = []
    for b in SERIES:
        mark = " &middot; આ પુસ્તક" if b["num"] == current_num else ""
        cards.append(f"""<div class="series-card">
        <div class="sc-title">{b['title']}{mark}</div>
        <div class="sc-sub">પુસ્તક {b['word']} &middot; {b['subtitle']}</div>
        <p>{b['blurb']}</p>
      </div>""")
    return f"""
<div class="page-content">
  <div class="center-page" style="align-items:stretch; text-align:left;">
    <div class="series">
      <h1>આ શ્રેણીમાં પણ</h1>
      <p class="intro">ધ અનલર્નિંગ સીરીઝ શીખવાના સંશોધનનાં તારણોને સરળ, ઉપયોગી અભ્યાસમાં ફેરવે છે. દરેક પુસ્તક સ્વયં પૂર્ણ છે અને એકલું વાંચી શકાય છે.</p>
      {''.join(cards)}
      <p style="font-size:13px; color:var(--ink-faint); margin-top:16px;">ત્રણેય પુસ્તકો ધ અનલર્નિંગ સીરીઝનો ભાગ છે.</p>
    </div>
  </div>
</div>
"""

def build_specials(meta):
    return {"cover": cover(meta), "title": title_page(meta), "copyright": copyright_page(meta),
            "dedication": dedication(meta), "about": ABOUT_HTML, "foreword": foreword(meta)}

def build_back(meta):
    return {"backcover": back_cover(meta), "series": series_page(meta["num"])}
