import requests


def translation_of_news(file_name, lang_for_translate, file_result):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    """
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    key = "trnsl.1.1.20181204T063748Z.e91a70705695696d.b39566d90088909ff6e32030d64e63d7863b7381"

   
    with open(file_name, encoding="utf-8") as f:
        text_file = f.read()

    languages = lang_for_translate + "-" + file_result

    params = {
        "key": key,
        "lang": languages,
        "text": text_file,
    }

    response = requests.post(url, data=params, timeout=30)
    translated_text = ' '.join(body.get("text", []))
    print(translated_text)
    with open(translated_file_name, "w", encoding="utf-8") as tf:
        tf.write(translated_text)


if __name__ == "__main__":
    lang_for_translate = input("Введите язык документа, например de, es, fr: ").lower()
    file_result = input("Введите на какой язык нужно перевести документ, например ru: ").lower()
    file_name = input("Пожалуйста, введите имя файла: ")
    translated_file_name = file_result + file_name
    translation_of_news(file_name, lang_for_translate, file_result)