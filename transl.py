from translate import Translator

# Указываем язык перевода с английского на русский
translator = Translator(to_lang="ru")

while True:
    # Просим пользователя ввести текст для перевода
    text_to_translate = input("Введите текст на английском для перевода (или 'exit' для выхода): ")

    # Проверяем, хочет ли пользователь выйти из программы
    if text_to_translate.lower() == 'exit':
        break

    # Перевод текста
    translated = translator.translate(text_to_translate)

    # Выводим оригинальный и переведенный текст
    print(f"Оригинальный текст: {text_to_translate}")
    print(f"Переведенный текст: {translated}\n")

