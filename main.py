import random
import time
import re
import textwrap
import compose_sentence
import riddles
from riddles import riddles_data
import tic_tac_toe
FILENAME_PROGRESS = "progress.txt"

# Функция загрузки прогресса игры
def load_progress():
    try:
        with open("progress.txt", "r") as file:
            level = None
            lives = None
            for line in file:
                match_level = re.match(r"level: (\d+)", line)
                match_lives = re.match(r"lives: (\d+)", line)
                if match_level:
                    level = int(match_level.group(1))
                elif match_lives:
                    lives = int(match_lives.group(1))
            if level is not None and lives is not None:
                return level, lives
            else:
                raise ValueError("Неполные данные о прогрессе")
    except FileNotFoundError:
        print("Файл прогресса не найден.")
        return 1, 0  # Возвращаем начальные значения

# Функция сохранения прогресса игры
def save_progress(level, lives):
    current_level, current_lives = load_progress()
    lives += current_lives
    with open("progress.txt", "w") as file:
        file.write(f"level: {level}\n")
        file.write(f"lives: {lives}\n")

# Обнулить прогресс
def reset_progress():
    with open("progress.txt", "w") as file:
        file.write("level: 0\n")
        file.write("lives: 0\n")

# Функция для чтения слов поддержки из файла
def read_support_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        support_words = file.readlines()
    return [word.strip() for word in support_words]

def get_shuffled_string(input_string):
    shuffled_string = ''.join(random.sample(input_string, len(input_string)))
    return shuffled_string

# Функция игры в Виселицу
def play_guess_riddle(level, lives, current_level):
    while True:
        riddles.guess_riddle(riddles_data)

        print("Пиратский Призрак: - Хотите попробовать себя в игре в крестики-нолики или отдохнуть перед следующей загадкой? (продолжить/отдохнуть): ")
        choice = input().lower()
        if choice == "продолжить":
            return 1
        else:
            rest(level, lives, current_level)
            return 1

            save_progress(current_level, lives)  # Используем текущее значение уровня для сохранения прогресса

# Функция чтения истории пирата из файла
def rest(level, lives, current_level):
    print("Пиратский призрак: давай отдохнем!")
    pirate_story = read_pirate_story("pirate_story.txt")
    print_with_pause(pirate_story)
    choice = input("Пиратский Призрак: - если готовы продолжить игру, то нажмите Enter: ").lower()
    if choice == "":
        return 1
    else:
        print("Пиратский Призрак: - подождем пока Вы восстановитесь для продолжения игры")

# Функция для чтения истории призрачного пирата из файла
def read_pirate_story(filename):
    with open(filename, "r", encoding="utf-8") as file:
        pirate_story = file.read()
    return pirate_story

# Функция для печати истории медленно
def print_with_pause(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Функция для игры в ti tac toe
def play_tic_tac_toe(level, lives, current_level):
    tic_tac_toe.tic_tac_toe()
    return 2

    save_progress(current_level, lives)

# Функция для сбора записки
def play_compose_sentence(level, lives, current_level):
    # Загрузка количества жизней из файла
    _, lives = load_progress()
    # Устанавливаем количество попыток для сбора записки равным количеству жизней
    attempts = lives

    support_words = read_support_words("support_words.txt")

    while attempts > 0:
        print("\nПиратский Призрак: - попыток собрать записку:", attempts)

        # Вызываем функцию из compose_sentence.py и передаем количество попыток и слова поддержки
        success = compose_sentence.two_parts()

        if success:
            break
        else:
            print("\nПиратский Призрак: - попробуйте снова.")
            attempts -= 1

    if attempts == 0:
        print("\nПиратский призрак: Судьба девочек загублена. Они теперь должны будут заплатить 3200 золотых монет......")
        lives = 0
        level = 0
        save_progress(level, lives)
        print("Пиратский Призрак: - хотите заработать еще жизней?")
        print("1. Игра в загадки")
        print("2. Игра в крестики-нолики")
        print("3. Выйти")
        choice = input("Введите номер игры (1/2/3): ")

        if choice == "1":
            # Вызов игры в загадки
            play_guess_riddle()
        elif choice == "2":
            # Вызов игры в крестики-нолики
            play_tic_tac_toe()
        elif choice == "3":
            print("Пиратский Призрак: - спасибо за прекрасную игру! Надеюсь, еще поиграем.")
            return
        else:
            print("Пиратский Призрак: - неверный выбор.")
    return 3

# Основная функция уровня
def start_level2():
    print("*" * 130)
    text = """
                             _                   _     _____       _                    _
                            | |                 | |   |_   _|     | |                  | |
                            | |       ___   ___ | |_    | |   ___ | |  __ _  _ __    __| |
                            | |      / _ \ / __|| __|   | |  / __|| | / _` || '_ \  / _` |
                            | |____ | (_) |\__ \| |_   _| |_ \__ \| || (_| || | | || (_| |
                            |______| \___/ |___/ \__| |_____||___/|_| \__,_||_| |_| \__,_|"""

    print(text)
    print("*" * 130)
    print("Добро пожаловать на второй уровень игры - Остров Загадок!👋")
    while True:  # Цикл для повторных проходов уровня
        # Запрос на готовность игрока
        ready = input("Пиратский Призрак: - готовы ли вы приступить к игре? (нажмите Enter для продолжения)")

        if ready == "":
            level, lives = load_progress()

            # Отгадывание загадок
            if play_guess_riddle(level, lives, level):
                lives += 3
                level = 1
                save_progress(level, lives)

                # Запускаем игру крестики-нолики
                board = tic_tac_toe.tic_tac_toe()
                if tic_tac_toe.check_winner(board):  # Проверяем, есть ли победитель
                    lives += 4
                    level = 2
                    save_progress(level, lives)

                # Награда за успешное прохождение
                text = ("Пиратский призрак: - поздравляю! Ты продержался на уровне и получаешь пиратский сундук!\n"
                        "В пиратском сундуке ты нашел 6 кристаллов и недостающую часть записки, которую тебе нужно будет расшифровать.")
                wrapped_text = textwrap.fill(text, width=120)
                print(wrapped_text)
                choice = input("Для продолжения нажмите Enter: ").lower()
                if choice == "":
                    # Запуск сбора записки
                    if not play_compose_sentence(level, lives, level):
                        break  # Если пользователь выбирает выход из игры, завершаем цикл

                # Предложение игроку пройти игру еще раз или завершить ее
                while True:
                    choice = input("Хотите пройти остров Загадок еще раз? (да/нет): ")
                    if choice.lower() == 'да':
                        break  # Прерываем внутренний цикл, чтобы начать игру заново
                    elif choice.lower() == 'нет':
                        print("Спасибо за игру!")
                        print("*" * 130)
                        text = """
                                                 _                   _     _____       _                    _
                                                | |                 | |   |_   _|     | |                  | |
                                                | |       ___   ___ | |_    | |   ___ | |  __ _  _ __    __| |
                                                | |      / _ \ / __|| __|   | |  / __|| | / _` || '_ \  / _` |
                                                | |____ | (_) |\__ \| |_   _| |_ \__ \| || (_| || | | || (_| |
                                                |______| \___/ |___/ \__| |_____||___/|_| \__,_||_| |_| \__,_|"""

                        print(text)
                        print("*" * 130)
                        reset_progress()
                        return  # Завершаем функцию, выходя из неё
                    else:
                        print("Пожалуйста, введите 'да' или 'нет'.")
        else:
            print("Хорошо, когда будете готовы, просто нажмите Enter.")

        # После завершения игры предлагаем отдохнуть
        if not rest(level, lives, level):
            break  # Если пользователь выбирает выход из игры, завершаем цикл

if __name__ == "__main__":
    start_level2()
