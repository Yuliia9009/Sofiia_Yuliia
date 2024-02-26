import random
import time

# Функция для печати истории призрачного пирата из файла
def print_with_pause(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def print_rules(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print_with_pause(line)

def print_board(board):
    for i in range(len(board)):
        row = " | ".join(board[i])
        print(row)
        if i < len(board) - 1:
            print("-" * (len(row) + 1))

def check_winner(board):
    # Проверяем строки
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Проверяем столбцы
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Проверяем диагонали
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    print("Добро пожаловать в игру 'Крестики-нолики'!")
    print_rules("rules.txt")  # Печать правил игры
    board = [[" " for _ in range(3)] for _ in range(3)]  # Инициализация игрового поля
    current_player = "X"  # Игрок, который делает текущий ход
    winner = None  # Победитель

    print("\nПиратский призрак - игра началась, удачи тебе мой друг!")

    while not winner:  # Пока нет победителя
        print_board(board)  # Выводим игровое поле на экран
        if current_player == "X":  # Ход пользователя
            try:
                row = int(input(f"Игрок {current_player}, выберите строку (1-3): ")) - 1
                col = int(input(f"Игрок {current_player}, выберите столбец (1-3): ")) - 1
            except ValueError:
                print("Неверный ввод! Попробуйте еще раз.")
                continue
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":  # Если введены корректные координаты и ячейка свободна
                board[row][col] = current_player  # Ставим символ текущего игрока в выбранную ячейку
                if check_winner(board):  # Проверяем, есть ли победитель
                    winner = current_player  # Если есть, устанавливаем победителя
                    print(f"Игрок {winner} выиграл!")
                elif check_draw(board):  # Проверяем, есть ли ничья
                    winner = "Draw"  # Если есть, объявляем ничью
                    print("Ничья!")
                else:
                    current_player = "O"  # Меняем игрока на компьютера
            else:
                print("Неверные координаты! Попробуйте еще раз.")
        else:  # Ход компьютера
            time.sleep(1)  # Задержка для имитации "мышления" компьютера
            computer_row, computer_col = random.randint(0, 2), random.randint(0, 2)  # Случайные координаты для хода компьютера
            while board[computer_row][computer_col] != " ":  # Если выбранная ячейка уже занята
                computer_row, computer_col = random.randint(0, 2), random.randint(0, 2)  # Генерируем новые координаты
            print(f"Ход Пиратского призрака: строка {computer_row + 1}, столбец {computer_col + 1}")
            board[computer_row][computer_col] = "O"  # Ставим символ "O" в выбранную ячейку
            if check_winner(board):  # Проверяем, есть ли победитель
                winner = "O"  # Если есть, устанавливаем победителя
            elif check_draw(board):  # Проверяем, есть ли ничья
                winner = "Draw"  # Если есть, объявляем ничью
            else:
                current_player = "X"

    print_board(board)  # Выводим конечное состояние игрового поля
    return board  # Возвращаем текущее состояние игрового поля

def check_draw(board):
    for row in board:
        if " " in row:  # Если есть пустая ячейка
            return False  # Нет ничьи
    return True  # Все ячейки заняты, это ничья

if __name__ == "__main__":
    board = tic_tac_toe()  # Получаем текущее состояние игрового поля
    if check_winner(board):  # Проверяем, есть ли победитель
        winner = "X"  # Если есть, устанавливаем победителя
