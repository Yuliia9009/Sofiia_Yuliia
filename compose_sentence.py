import random

# Функция для получения случайного слова поддержки из файла
def get_random_support_word():
    with open("support_words.txt", "r", encoding="utf-8") as file:
        support_words = file.readlines()
    return random.choice(support_words).strip()

# Функция для получения первой строки из файла с перемешанными буквами
def get_shuffled_note_part1():
    with open("note_part.txt", "r") as file:
        lines = file.readlines()
        note_part1 = next((line.split(']')[1].strip() for line in lines if line.startswith("[1]")), "")
        # Разбиваем строку на слова, перемешиваем буквы в каждом слове и объединяем их обратно в строку
        shuffled_words = [''.join(random.sample(word, len(word))) for word in note_part1.split()]
        return ' '.join(shuffled_words)

# Функция для получения второй строки из файла с перемешанными буквами
def get_shuffled_note_part2():
    with open("note_part.txt", "r") as file:
        lines = file.readlines()
        note_part2 = next((line.split(']')[1].strip() for line in lines if line.startswith("[2]")), "")
        # Разбиваем строку на слова, перемешиваем буквы в каждом слове и объединяем их обратно в строку
        shuffled_words = [''.join(random.sample(word, len(word))) for word in note_part2.split()]
        return ' '.join(shuffled_words)

def compose_sentence(note_part1, note_part2):
    print("Составьте предложение из двух частей записки:")
    print("Первая часть записки:", note_part1)
    print("Вторая часть записки:", note_part2)
    user_sentence = input("Введите свое предложение: ")
    return user_sentence

# Функция для сбора записки
def two_parts():
    # Получаем первую часть записки
    note_part1 = get_shuffled_note_part1()
    # Получаем вторую часть записки
    note_part2 = get_shuffled_note_part2()

    correct_sentence = "Поздравляем! София и Юлия сдали экзамен!"

    # Составляем предложение из двух частей записки
    composed_sentence = compose_sentence(note_part1, note_part2)

    # Проверяем правильность составленного предложения
    if composed_sentence.lower() == correct_sentence.lower():
        print("Пиратский призрак: Ты справился! Теперь ты знаешь какую оценку мы хотим.")
        return True
    else:
        print("Пиратский призрак: Не волнуйся, ты сможешь это разгадать!")
        return False

if __name__ == "__main__":
    two_parts()