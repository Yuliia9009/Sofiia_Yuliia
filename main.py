import random
import time
import compose_sentence
import riddles
from riddles import riddles_data
import tic_tac_toe

# Функция для чтения слов поддержки из файла
def read_support_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        support_words = file.readlines()
    return [word.strip() for word in support_words]

def get_shuffled_string(input_string):
    shuffled_string = ''.join(random.sample(input_string, len(input_string)))
    return shuffled_string

def play_guess_riddle(level, lives, current_level):
    riddles.guess_riddle(riddles_data)

    print("Хочешь попробовать себя в игре в крестики-нолики или отдохнуть перед следующей загадкой? (продолжить/отдохнуть): ")
    choice = input().lower()
    if choice == "продолжить":
        return 1  # Вернуть идентификатор уровня, в данном случае 1, чтобы обозначить, что игра была на первом уровне
    else:
        rest()  # Выводим историю пирата
        return 0  # Вернуть 0, чтобы обозначить, что игра была отменена

    save_progress(current_level, lives)  # Используем текущее значение уровня для сохранения прогресса

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

# Функция чтения истории пирата из файла
def rest():
    print("Пиратский призрак: Давай отдохнем!")
    pirate_story = read_pirate_story("pirate_story.txt")  # Получаем историю пирата из файла
    print_with_pause(pirate_story)  # Печатаем историю с паузой
    play_tic_tac_toe()  # Запускаем игру в крестики-нолики

# Функция для игры в ti tac toe
def play_tic_tac_toe(level, lives, current_level):
    tic_tac_toe.tic_tac_toe()
    return 2
    save_progress(current_level, lives)  # Используем текущее значение уровня для сохранения прогресса

# Функция для сбора записки
def play_compose_sentence(level, lives, current_level):
    # Загрузка количества жизней из файла
    _, lives = load_progress()  # Получаем только количество жизней из возвращаемого кортежа
    # Устанавливаем количество попыток для сбора записки равным количеству жизней
    attempts = lives

    # Чтение слов поддержки из файла
    support_words = read_support_words("support_words.txt")

    while attempts > 0:
        print("\nПопыток собрать записку:", attempts)

        # Вызываем функцию из compose_sentence.py и передаем количество попыток и слова поддержки
        success = compose_sentence.two_parts()

        if success:
            break
        else:
            print("\nПопробуйте снова.")
            # Уменьшаем количество попыток
            attempts -= 1

    if attempts == 0:
        print("\nПиратский призрак: Судьба девочек загублена. Они теперь должны будут заплатить 3200 золотых монет......")
        lives = 0
        level = 0
        save_progress(level, lives)
        print("Хотите заработать еще жизней?")
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
            print("Спасибо за прекрасную игру! Надеюсь, еще поиграем.")
            return
        else:
            print("Неверный выбор.")
    return 3

# Функция для сохранения прогресса
def save_progress(level, lives):
    with open("progress.txt", "w") as file:
        file.write(f"{level}\n")
        file.write(f"{lives}\n")

def load_progress():
    try:
        with open("progress.txt", "r") as file:
            level = int(file.readline().strip())
            lives = int(file.readline().strip())
            return level, lives
    except FileNotFoundError:
        # Если файл прогресса не найден, возвращаем начальные значения
        return 1, 0  # Например, начнем с первого уровня и установим 0 жизней


# Основная функция уровня
def start_level2():
    print("Добро пожаловать на второй уровень - Остров Загадок!")

    # Загрузка уровня и количества жизней
    level, lives = load_progress()

    # Отгадывание загадок
    if play_guess_riddle(level, lives, level):
        lives = + 3  # Пользователь отгадал загадку, увеличиваем количество жизней
        level = 1
        save_progress(level, lives)

    # Запуск игры в крестики-нолики
    board = tic_tac_toe.tic_tac_toe()  # Запускаем игру крестики-нолики и получаем текущее состояние игрового поля
    if tic_tac_toe.check_winner(board):  # Проверяем, есть ли победитель
        lives = + 4  # Если есть, увеличиваем количество жизней на 4
        level = 2
        save_progress(level, lives)  # Сохраняем количество жизней

    # Награда за успешное прохождение
    print("Пиратский призрак: - поздравляю! Ты продержался на уровне и получаешь пиратский сундук! В пиратском сундуке ты нашел 6 кристаллов и недостающую часть записки, которую тебе нужно будет расшифровать.")

    # Запуск сбора записки
    play_compose_sentence(level, lives, level)

    print("Игровой уровень завершен!")

    # Предложение игроку пройти игру еще раз или завершить ее
    while True:
        choice = input("Хотите пройти 2 уровень еще раз? (y/n): ")
        if choice.lower() == 'y':
            start_level2()  # Запуск уровня заново
        elif choice.lower() == 'n':
            print("Спасибо за игру! До новых встреч!")
            break  # Завершение игры
        else:
            print("Пожалуйста, введите 'y' или 'n'.")  # Предупреждение об ошибке ввода

if __name__ == "__main__":
    start_level2()