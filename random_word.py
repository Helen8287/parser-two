import requests
from bs4 import BeautifulSoup


#Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"

    try:
        response = requests.get(url)
        print(response.text)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find_all('div', id='random_word')
        word_definition = soup.find_all('div', id='random_word_definition')

        return {
            "english_word" : english_words,
            "word_definition" : word_definition
        }
    except:
        print("Произошла ошибка")


#Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")

    # Создаём функцию, чтобы использовать результат функции-словаря
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово?")

        if user == word:
            print("Все хорошо!")
        else:
            print(f'Ответ неверный, было загадано это слово - {word}')

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y\n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()






