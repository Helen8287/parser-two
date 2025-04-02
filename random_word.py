import requests
from bs4 import BeautifulSoup
from translate import Translator

translator = Translator(to_lang="ru")

#Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"

    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find('div', id='random_word').text.strip()
        # Получаем описание слова
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        # Переводим слово и описание на русский
        translated_word = translator.translate(english_words)
        translated_definition = translator.translate(word_definition)


        # Чтобы программа возвращала словарь

        return {
            "english_word" : english_words,
            "word_definition" : word_definition,
            "translated_word": translated_word,
            "translated_definition": translated_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


#Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")

    # Создаём функцию, чтобы использовать результат функции-словаря
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")
        translated_word = word_dict.get("translated_word")
        translated_definition = word_dict.get("translated_definition")

        # Начинаем игру
        print(f"Значение слова (перевод) - {translated_definition}")
        user = input("Что это за слово на английском?")

        if user == word:
            print("Ответ верный!")
        else:
            print(f'Ответ неверный, было загадано это слово - {word} ({translated_word})')

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()






