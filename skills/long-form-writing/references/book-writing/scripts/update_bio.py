# -*- coding: utf-8 -*-
"""Replace the placeholder author bio with the real one, in every source file.
Bio facts come only from Dr. Momin's resume."""
import re, os

BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")

# Ordering rule (assets/author-bio-template.md): practice and service lead;
# job titles always go last. Two paragraphs, as the template's "long" shape.
EN = [
    "Dr. Sohil Momin, BHMS, is a homoeopathic physician based in Vadodara, Gujarat. He has spent more than seventeen years in teaching hospitals, outpatient departments, and private practice, managing high-volume clinics, supervising clinical teams and interns, and coordinating hospital accreditation, clinical audits, and standard operating procedures. He is President of the Charity for Humanity Trust in Vadodara, which runs health screening drives, medical camps, and community outreach.",
    "He is a published author and translator: his clinical articles have appeared in Hpathy.com International Journal, The Homoeopathic Heritage, and Vital Informer, and he has translated two complete books from English into Gujarati. He has written hospital administration manuals and clinical audit frameworks published on Amazon KDP, and The Unlearning Series is his writing on how people learn, unlearn, and change, and how those lessons can be put to work in ordinary life. He serves as Resident Medical Officer and healthcare administrator.",
]

HI = [
    "डॉ. सोहिल मोमिन, बी.एच.एम.एस., वडोदरा, गुजरात में रहने वाले एक होम्योपैथिक चिकित्सक हैं। उन्होंने सत्रह वर्ष से अधिक समय टीचिंग अस्पतालों, ओपीडी और निजी प्रैक्टिस में बिताया है, जहाँ उन्होंने व्यस्त क्लिनिक चलाए, क्लिनिकल टीमों और इंटर्नों का मार्गदर्शन किया, और अस्पताल मान्यता, क्लिनिकल ऑडिट तथा मानक संचालन प्रक्रियाओं (एसओपी) का समन्वय किया। वे वडोदरा की चैरिटी फ़ॉर ह्यूमैनिटी ट्रस्ट के अध्यक्ष हैं, जो स्वास्थ्य जाँच शिविर, चिकित्सा शिविर और सामुदायिक सेवा चलाती है।",
    "वे एक प्रकाशित लेखक और अनुवादक हैं: उनके क्लिनिकल लेख Hpathy.com International Journal, The Homoeopathic Heritage और Vital Informer में छपे हैं, और उन्होंने अंग्रेज़ी से गुजराती में दो पूरी किताबें अनुवाद की हैं। उन्होंने Amazon KDP पर अस्पताल प्रशासन की पुस्तिकाएँ और क्लिनिकल ऑडिट ढाँचे प्रकाशित किए हैं, और द अनलर्निंग सीरीज़ उनका यह लेखन है कि लोग कैसे सीखते हैं, कैसे अनलर्न करते हैं और कैसे बदलते हैं। वे रेज़िडेंट मेडिकल ऑफ़िसर और अस्पताल प्रशासक के रूप में कार्यरत हैं।",
]

GU = [
    "ડૉ. સોહિલ મોમિન, બી.એચ.એમ.એસ., વડોદરા, ગુજરાતમાં રહેતા એક હોમિયોપેથિક ચિકિત્સક છે. તેમણે સત્તર વર્ષથી વધુ સમય ટીચિંગ હોસ્પિટલો, ઓપીડી અને ખાનગી પ્રેક્ટિસમાં વિતાવ્યો છે, જ્યાં તેમણે વ્યસ્ત ક્લિનિક ચલાવ્યાં, ક્લિનિકલ ટીમો અને ઇન્ટર્નોને માર્ગદર્શન આપ્યું, અને હોસ્પિટલ માન્યતા, ક્લિનિકલ ઓડિટ તથા સ્ટાન્ડર્ડ ઓપરેટિંગ પ્રોસિજર (એસઓપી)નું સંકલન કર્યું. તેઓ વડોદરાની ચેરિટી ફોર હ્યુમેનિટી ટ્રસ્ટના પ્રમુખ છે, જે આરોગ્ય તપાસ શિબિરો, તબીબી કેમ્પ અને સામૂહિક સેવા ચલાવે છે.",
    "તેઓ એક પ્રકાશિત લેખક અને અનુવાદક છે: તેમના ક્લિનિકલ લેખો Hpathy.com International Journal, The Homoeopathic Heritage અને Vital Informerમાં પ્રકાશિત થયા છે, અને તેમણે અંગ્રેજીથી ગુજરાતીમાં બે આખાં પુસ્તકોનો અનુવાદ કર્યો છે. તેમણે Amazon KDP પર હોસ્પિટલ વ્યવસ્થાપનની પુસ્તિકાઓ અને ક્લિનિકલ ઓડિટ માળખાં પ્રકાશિત કર્યાં છે, અને ધ અનલર્નિંગ સીરીઝ એ તેમનું લેખન છે કે લોકો કેવી રીતે શીખે છે, અનલર્ન કરે છે અને બદલાય છે. તેઓ રેસિડેન્ટ મેડિકલ ઓફિસર અને હોસ્પિટલ એડમિનિસ્ટ્રેટર તરીકે કાર્યરત છે.",
]

def about_html(head, paras, first_bold=True):
    ps = []
    for i, p in enumerate(paras):
        if i == 0 and first_bold:
            name, rest = p.split(",", 1)
            ps.append(f"    <p><strong>{name}</strong>,{rest}</p>")
        else:
            ps.append(f"    <p>{p}</p>")
    return ('\n<div class="page-content">\n  <div class="front-h">' + head + '</div>\n'
            '  <div class="author-body" style="max-width:560px;">\n' + "\n".join(ps) +
            '\n  </div>\n</div>\n')

NEW_HTML = {
    "bookkit.py":     ('ABOUT_HTML', about_html("About the Author", EN)),
    "content_a.py":   ('SPECIALS["about"]', about_html("About the Author", EN)),
    "bookkit_hi.py":  ('ABOUT_HTML', about_html("लेखक के बारे में", HI)),
    "bookkit_gu.py":  ('ABOUT_HTML', about_html("લેખક વિશે", GU)),
}

for fname, (var, body) in NEW_HTML.items():
    path = os.path.join(BOOK, fname)
    s = open(path).read()
    pat = re.compile(re.escape(var) + r'\s*=\s*""".*?"""', re.S)
    new, n = pat.subn(lambda m: f'{var} = """{body}"""', s, count=1)
    assert n == 1, f"no match in {fname}"
    open(path, "w").write(new)
    print(f"{fname}: about block replaced")

# --- docx label dicts: replace the three about_p lists in order (en, hi, gu) ---
path = os.path.join(BOOK, "make_docx_designed.py")
s = open(path).read()
lists = [EN, HI, GU]
counter = {"i": 0}

def repl(m):
    lang = lists[counter["i"]]
    counter["i"] += 1
    items = ",\n               ".join('"' + x.replace('"', '\\"') + '"' for x in lang)
    return '"about_p": [' + items + '],'

s2, n = re.subn(r'"about_p": \[.*?\],', repl, s, flags=re.S)
assert n == 3, f"expected 3 about_p lists, found {n}"
open(path, "w").write(s2)
print(f"make_docx_designed.py: {n} about_p lists replaced")
