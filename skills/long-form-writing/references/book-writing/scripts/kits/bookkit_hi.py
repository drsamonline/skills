# -*- coding: utf-8 -*-
"""Hindi front/back-matter kit (mirrors bookkit.py)."""

SERIES = [
    {"num": 1, "word": "एक", "title": "घंटी के बाद",
     "subtitle": "हमें जो सिखाया गया, उसे अनलर्न करने का मनोविज्ञान",
     "title_html": "घंटी के<br/>बाद",
     "blurb": "संकेत, नतीजे और पुरानी कहानियाँ कैसे हमारी प्रतिक्रियाएँ गढ़ती हैं, और उन्हें बदलने का चार-चरणीय तरीका।"},
    {"num": 2, "word": "दो", "title": "ख़ामोश इनाम",
     "subtitle": "राहत, बचाव, और उनसे बनी आदतें",
     "title_html": "ख़ामोश<br/>इनाम",
     "blurb": "हमारी सबसे ज़िद्दी आदतों के पीछे छिपे अदृश्य इनाम पर एक गहरी नज़र: राहत, और वह बचाव जिसे वह चुपचाप बढ़ाती है।"},
    {"num": 3, "word": "तीन", "title": "नई पगडंडियाँ",
     "subtitle": "ऐसा व्यवहार बनाना जो टिके",
     "title_html": "नई<br/>पगडंडियाँ",
     "blurb": "एक बदली हुई प्रतिक्रिया को ऐसी टिकाऊ, आत्म-निर्भर आदत में कैसे बदलें जो तनाव और समय के साथ बनी रहे।"},
]

AUTHOR = "डॉ. सोहिल मोमिन"
CONTACT = "sohilmomin2000@gmail.com"
YEAR = "2026"
BRAND = "द अनलर्निंग सीरीज़"

# Per-language labels for the designed DOCX (make_docx_designed.py).
L10N = {
    "series": "द अनलर्निंग सीरीज़ · पुस्तक {w}",
    "author": AUTHOR,
    "c_rights": "© 2026 डॉ. सोहिल मोमिन. सर्वाधिकार सुरक्षित।",
    "c_ed": "प्रथम संस्करण, 2026।",
    "c_no": "इस प्रकाशन के किसी भी हिस्से को लेखक की लिखित अनुमति के बिना कॉपी, संग्रहित या प्रसारित नहीं किया जा सकता, सिवाय समीक्षा या शोध-कार्य में छोटे उद्धरणों के।",
    "c_disc": "यह किताब सीखने और व्यवहार के बारे में सामान्य जानकारी देती है। यह किसी योग्य मानसिक-स्वास्थ्य विशेषज्ञ के निदान या इलाज का विकल्प नहीं है।",
    "c_case": "इस किताब की केस-सामग्री केवल उदाहरण के लिए है और कई लोगों की बातों को मिलाकर बनाई गई है।",
    "contact": "संपर्क: sohilmomin2000@gmail.com",
    "about_h": "लेखक के बारे में",
    "fore_h": "प्रस्तावना",
    "safety_l": "मानसिक सुरक्षा पर एक टिप्पणी",
    "safety_p": "यह किताब कंडीशंड डर, बचाव की आदत और बेबसी के बारे में है। ज़्यादातर पाठकों के लिए यह सुरक्षित है। अगर आप भावनाओं में डूब रहे हैं या तकलीफ़ महसूस कर रहे हैं, तो कृपया किसी लाइसेंस्ड मानसिक-स्वास्थ्य विशेषज्ञ या भरोसेमंद व्यक्ति से बात करें। इन पन्नों में लिखी कोई बात किसी योग्य क्लिनिशियन की देखभाल की जगह नहीं ले सकती।",
    "toc_h": "विषय-सूची", "gloss_h": "शब्दावली", "idx_h": "अनुक्रमणिका", "bib_h": "ग्रंथ-सूची",
    "font": "Noto Sans Devanagari",
}

ABOUT_HTML = """
<div class="page-content">
  <div class="front-h">लेखक के बारे में</div>
  <div class="author-body" style="max-width:560px;">
    <p><strong>डॉ. सोहिल मोमिन</strong>, बी.एच.एम.एस., वडोदरा, गुजरात में रहने वाले एक होम्योपैथिक चिकित्सक हैं। उन्होंने सत्रह वर्ष से अधिक समय टीचिंग अस्पतालों, ओपीडी और निजी प्रैक्टिस में बिताया है, जहाँ उन्होंने व्यस्त क्लिनिक चलाए, क्लिनिकल टीमों और इंटर्नों का मार्गदर्शन किया, और अस्पताल मान्यता, क्लिनिकल ऑडिट तथा मानक संचालन प्रक्रियाओं (एसओपी) का समन्वय किया। वे वडोदरा की चैरिटी फ़ॉर ह्यूमैनिटी ट्रस्ट के अध्यक्ष हैं, जो स्वास्थ्य जाँच शिविर, चिकित्सा शिविर और सामुदायिक सेवा चलाती है।</p>
    <p>वे एक प्रकाशित लेखक और अनुवादक हैं: उनके क्लिनिकल लेख Hpathy.com International Journal, The Homoeopathic Heritage और Vital Informer में छपे हैं, और उन्होंने अंग्रेज़ी से गुजराती में दो पूरी किताबें अनुवाद की हैं। उन्होंने Amazon KDP पर अस्पताल प्रशासन की पुस्तिकाएँ और क्लिनिकल ऑडिट ढाँचे प्रकाशित किए हैं, और द अनलर्निंग सीरीज़ उनका यह लेखन है कि लोग कैसे सीखते हैं, कैसे अनलर्न करते हैं और कैसे बदलते हैं। वे रेज़िडेंट मेडिकल ऑफ़िसर और अस्पताल प्रशासक के रूप में कार्यरत हैं।</p>
  </div>
</div>
"""

def cover(meta):
    return f"""
<div class="page-content">
  <div class="bigname">{BRAND} &middot; पुस्तक {meta['word']}</div>
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
    <div class="imprint">{BRAND} &middot; पुस्तक {meta['word']}</div>
  </div>
</div>
"""

def copyright_page(meta):
    return f"""
<div class="page-content">
  <div class="center-page">
    <div class="copy-page" style="max-width:470px;">
      <p><strong>{meta['title']}: {meta['subtitle']}</strong></p>
      <p>&copy; {YEAR} {AUTHOR}. सर्वाधिकार सुरक्षित।</p>
      <p>प्रथम संस्करण, {YEAR}।</p>
      <p>इस प्रकाशन के किसी भी हिस्से को लेखक की लिखित अनुमति के बिना, किसी भी रूप में या किसी भी तरीके (इलेक्ट्रॉनिक या मेकैनिकल) से कॉपी, संग्रहित या प्रसारित नहीं किया जा सकता, सिवाय समीक्षा या शोध-कार्य में छोटे उद्धरणों के।</p>
      <p>यह किताब सीखने और व्यवहार के बारे में सामान्य जानकारी देती है। यह किसी योग्य मानसिक-स्वास्थ्य विशेषज्ञ के निदान या इलाज का विकल्प नहीं है। यदि आप किसी कठिनाई में हैं, तो कृपया अपने क्षेत्र के किसी लाइसेंस्ड क्लिनिशियन या भरोसेमंद सहायता सेवा से संपर्क करें।</p>
      <p>इस किताब की केस-सामग्री केवल उदाहरण के लिए है और कई लोगों की बातों को मिलाकर बनाई गई है। इसमें किसी भी पहचाने जा सकने वाले जीवित व्यक्ति का वर्णन नहीं है।</p>
      <p>संपर्क: {CONTACT}</p>
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
  <div class="front-h">प्रस्तावना</div>
  <h2 style="margin-top:0;">{meta['foreword_head']}</h2>
  {pre}
  <div class="callout">
    <div class="clabel">मानसिक सुरक्षा पर एक टिप्पणी</div>
    <p>यह किताब कंडीशंड डर, बचाव की आदत और बेबसी के बारे में है। ज़्यादातर पाठकों के लिए, इन विषयों के बारे में पढ़ना सुरक्षित और उपयोगी है। लेकिन कुछ लोगों के लिए, यह ऐसी बातें जगा सकती है जिन्हें किसी किताब के बजाय किसी प्रशिक्षित सुनने वाले से सुनना बेहतर होता है।</p>
    <p>अगर आपको लगे कि आप भावनाओं में डूब रहे हैं, खुद को अलग-थलग महसूस कर रहे हैं, या बिना तकलीफ़ के इस किताब को नीचे नहीं रख पा रहे हैं, तो कृपया थोड़ा रुकें और किसी लाइसेंस्ड मानसिक-स्वास्थ्य विशेषज्ञ या अपनी ज़िंदगी के किसी भरोसेमंद व्यक्ति से बात करें। अगर आप किसी संकट में हैं, तो अपने स्थानीय आपातकालीन नंबर या अपने क्षेत्र की किसी क्राइसिस लाइन से संपर्क करें। इन पन्नों में लिखी कोई भी बात किसी योग्य क्लिनिशियन की देखभाल की जगह नहीं ले सकती, और यहाँ दी गई किसी भी एक्सरसाइज़ को इलाज की जगह नहीं करना चाहिए।</p>
    <p>अपने नर्वस सिस्टम की क्षमता के हिसाब से पढ़ें। जल्दी पढ़ने का कोई इनाम नहीं है।</p>
  </div>
  {post}
</div>
"""

def back_cover(meta):
    return f"""
<div class="page-content">
  <h2>{meta['title']}</h2>
  {''.join(f'<p>{p}</p>' for p in meta['back_paras'])}
  <div class="series-line">{BRAND} &middot; पुस्तक {meta['word']}</div>
</div>
"""

def series_page(current_num):
    cards = []
    for b in SERIES:
        mark = " &middot; यह पुस्तक" if b["num"] == current_num else ""
        cards.append(f"""<div class="series-card">
        <div class="sc-title">{b['title']}{mark}</div>
        <div class="sc-sub">पुस्तक {b['word']} &middot; {b['subtitle']}</div>
        <p>{b['blurb']}</p>
      </div>""")
    return f"""
<div class="page-content">
  <div class="center-page" style="align-items:stretch; text-align:left;">
    <div class="series">
      <h1>इस श्रृंखला में भी</h1>
      <p class="intro">द अनलर्निंग सीरीज़ सीखने की रिसर्च के नतीजों को आसान और काम के तरीकों में बदलती है। हर किताब अपने आप में पूरी है और उसे अलग से भी पढ़ा जा सकता है।</p>
      {''.join(cards)}
      <p style="font-size:13px; color:var(--ink-faint); margin-top:16px;">तीनों किताबें द अनलर्निंग सीरीज़ का हिस्सा हैं।</p>
    </div>
  </div>
</div>
"""

def build_specials(meta):
    return {"cover": cover(meta), "title": title_page(meta), "copyright": copyright_page(meta),
            "dedication": dedication(meta), "about": ABOUT_HTML, "foreword": foreword(meta)}

def build_back(meta):
    return {"backcover": back_cover(meta), "series": series_page(meta["num"])}
