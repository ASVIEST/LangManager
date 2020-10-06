import ast

with open('langs.txt') as f:
    global langs
    langs = f.read()
    langs = langs.replace('#encoding ISO 639-1', '')
    langs = langs.replace('\n', '')
langs = ast.literal_eval(langs)

lan = ''

enpath = 'en.txt'
rupath = 'ru.txt'
zhpath = 'zh.txt'
frpath = 'fr.txt'
knpath = 'kn.txt'
japath = 'ja.txt'
plpath = 'pl.txt'
depath = 'de.txt'
itpath = 'it.txt'

#select language
def lang(language='en'):
    global lan
    lan = langs[language]

def lan():
    return lan

def format_to_pydictionary(path='test.txt'):
    f = open(path)
    text = f.read()
    text = text.replace(';', ',')
    text = text.replace('\n', '')
    lengh = len(text)
    text = '{' + text + '}'
    if text[lengh] == ',':
        text = text[:lengh] + text[lengh + 1:]
    return text


#create dictions
def en_translate(path):
    global translate_en
    translate_en = format_to_pydictionary(path)
    translate_en = ast.literal_eval(translate_en)
    
def ru_translate(path):
    global translate_ru
    translate_ru = format_to_pydictionary(path)
    translate_ru = ast.literal_eval(translate_ru)

def zh_translate(path):
    global translate_zh
    translate_zh = format_to_pydictionary(path)
    translate_zh = ast.literal_eval(translate_zh)

def fr_translate(path):
    global translate_fr
    translate_fr = format_to_pydictionary(path)
    translate_fr = ast.literal_eval(translate_fr)

def kn_translate(path):
    global translate_kn
    translate_kn = format_to_pydictionary(path)
    translate_kn = ast.literal_eval(translate_kn)

def ja_translate(path):
    global translate_ja
    translate_ja = format_to_pydictionary(path)
    translate_ja = ast.literal_eval(translate_ja)

def pl_translate(path):
    global translate_pl
    translate_pl = format_to_pydictionary(path)
    translate_pl = ast.literal_eval(translate_pl)

def de_translate(path):
    global translate_de
    translate_de = format_to_pydictionary(path)
    translate_de = ast.literal_eval(translate_de)

def it_translate(path):
    global translate_it
    translate_it = format_to_pydictionary(path)
    translate_it = ast.literal_eval(translate_it)

#change path
def filepath_en(path):
    global enpath
    enpath = path

def filepath_ru(path):
    global rupath
    rupath = path

def filepath_zh(path):
    global zhpath
    zhpath = path

def filepath_fr(path):
    global frpath
    frpath = path

def filepath_kn(path):
    global knpath
    knpath = path

def filepath_ja(path):
    global knpath
    knpath = path

def filepath_pl(path):
    global plpath
    plpath = path

def filepath_de(path):
    global depath
    depath = path

def filepath_it(path):
    global itpath
    itpath = path

def translate_get(text=''):
    if lan == 'english':
        en_translate(enpath)
        translate = translate_en[text]
        return translate
    if lan == 'russian':
        ru_translate(rupath)
        translate = translate_ru[text]
        return translate
    if lan == 'chinese':
        zh_translate(zhpath)
        translate = translate_zh[text]
        return translate
    if lan == 'french':
        fr_translate(frpath)
        translate = translate_fr[text]
        return translate
    if lan == 'kannada':
        kn_translate(knpath)
        translate = translate_kn[text]
        return translate
    if lan == 'japanese':
        ja_translate(knpath)
        translate = translate_ja[text]
        return translate
    if lan == 'polish':
        pl_translate(plpath)
        translate = translate_pl[text]
        return translate
    if lan == 'german':
        de_translate(depath)
        translate = translate_de[text]
        return translate
    elif lan == 'italian':
        it_translate(itpath)
        translate = translate_it[text]
        return translate
