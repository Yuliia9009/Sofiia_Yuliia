import random

# Функция для чтения загадок из файла
def read_riddles(filename):
    riddles_data = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            riddle, answer = line.strip().split(":")
            riddles_data[riddle] = answer
    return riddles_data

def guess_riddle(riddles):
    print("Добро пожаловать в игру 'Виселица'")
    print("Пиратский призрак: - Вам будет загадано загадку, если отгадаешь, то Вы получишь 3 жизни.")
    riddle, answer = random.choice(list(riddles.items()))
    answer_without_spaces = answer.replace(" ", "")
    guessed_letters = ["_"] * len(answer_without_spaces)  # Загадываемое слово в виде списка букв с подчеркиваниями
    guessed_already = set()  # Множество для хранения уже введенных букв
    failed_attempts = 0

    print("\nЗагадка:", riddle)  # Выводим загадку

    while True:
        print("Отгадай слово:", ' '.join(guessed_letters))  # Отображение слова с подчеркиваниями
        print_hangman(failed_attempts)  # Отображение виселицы
        guess = input("Введите букву: ")

        if len(guess) != 1 or not guess.isalpha() or not all('а' <= char.lower() <= 'я' for char in guess):
            print("Пожалуйста, введите одну русскую букву.")
            continue

        guess = guess.lower()

        if guess in guessed_already:
            print("Вы уже вводили эту букву.")
            continue

        guessed_already.add(guess)

        if guess in answer_without_spaces.lower():
            for i, letter in enumerate(answer_without_spaces):
                if letter.lower() == guess:
                    guessed_letters[i] = letter  # Заменяем подчеркивание на угаданную букву
            if "_" not in guessed_letters:
                print("Пиратский Призрак: - поздравляю! Вы отгадали слово:", answer)
                print("Я даю Вам как и обещал 3 жизни.")
                return True
        else:
            print("Такой буквы нет в слове.")
            failed_attempts += 1

            if failed_attempts >= 6:
                print("У вас закончились попытки. Вы проиграли.")
                print_hangman(failed_attempts)
                print("Загаданное слово было:", answer)
                return False

            print("Осталось попыток:", 6 - failed_attempts)

def print_hangman(failed_attempts):
    hangman_parts = [
        [
            "   ____ ",
            "  |    |",
            "  |",
            "  |",
            "  |",
            "__|__   "
        ],
        [
            "   ____ ",
            "  |    |",
            "  |    O",
            "  |",
            "  |",
            "__|__   "
        ],
        [
            "   ____ ",
            "  |    |",
            "  |    O",
            "  |    |",
            "  |",
            "__|__   "
        ],
        [
            "   ____ ",
            "  |    |",
            "  |    O",
            "  |   /|",
            "  |",
            "__|__   "
        ],
        [
            "   ____ ",
            "  |    |",
            "  |    O",
            "  |   /|\\",
            "  |",
            "__|__   "
        ],
        [
            "   ____ ",
            "  |    |",
            "  |    O",
            "  |   /|\\",
            "  |   /",
            "__|__   "
        ],
        [
            "   ____ ",
            "  |    |",
            "  |    O",
            "  |   /|\\",
            "  |   / \\",
            "__|__   "
        ]
    ]

    for line in hangman_parts[failed_attempts]:
        print(line)

riddles_data = {
    "Что летает без крыльев и поет без горла?": "облако",
    "Что всегда идет, но никогда не приходит?": "время",
    "Что летает без крыльев?": "время",
    "Что можно видеть снаружи, но нельзя увидеть изнутри?": "печка",
    "Что можно сломать, но нельзя исправить?": "мечта",
    "Что не имеет тела, но может сделать вас плакать?": "голос",
    "Какое слово становится короче, если добавить к нему букву 'и'?": "время",
    "Что бывает один раз в минуту, дважды в мгновение и ни разу в тысячелетие?": "буква",
    "Какой шаг вы можете сделать, не двигаясь?": "шагом",
    "Что легче, чем перышко; но крепче всех?": "время"
}
if __name__ == "__main__":
    guess_riddle(riddles_data)
