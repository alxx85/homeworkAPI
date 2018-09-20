import requests
import glob

API_KEY = 'trnsl.1.1.20180920T113850Z.92049bcc23fb364d.f4cb39e658d9dcb3afeefb4211dcc8c170a986f7' #'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(path_text, path_result,lang, to_lang = 'ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """
    with open(path_text) as f:
        text = f.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_text = response.json()
    print(json_text['text'])

    with open(path_result, 'w') as f:
        f.write(str(json_text['text']))
    return #''.join(json_['text'])

    print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

def new_filename(old_filename):
  file_new = str(old_filename).lower()
  file_new = file_new[:len(file_new)-4] + '_rus.txt'
  return file_new

def language(filename):
  file_lang = str(filename).lower()
  file_lang = file_lang[len(file_lang)-6:len(file_lang)-4]
  return file_lang


files = glob.glob("*.txt")
for file in files:
    if '_rus' not in str(file):
        print(file)
        new_file = new_filename(file)
        lang_file = language(file)
        translate_it(file, new_file, lang_file)

#requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))
