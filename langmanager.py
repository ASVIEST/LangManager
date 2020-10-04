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


def translate_get(text=''):
    if lan == 'english':
        en_translate(enpath)
        translate = translate_en[text]
        return translate
    if lan == 'russian':
        ru_translate(rupath)
        translate = translate_ru[text]
        return translate
    elif lan == 'chinese':
        zh_translate(zhpath)
        translate = translate_zh[text]
        return translate
