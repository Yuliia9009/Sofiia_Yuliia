class IslandExplorerGame:
    def __init__(self):
        # Инициализация игры
        self.player_name = ""  # Имя игрока
        self.player_age = 0  # Возраст игрока
        self.player_lives = 5  # Количество жизней игрока
        self.crystals_found = 0  # Количество найденных кристаллов
        self.locations = ["Пляж", "Джунгли", "Водопад", "Древние Руины"]  # Список доступных локаций
        self.task_completed = False  # Флаг, показывающий, выполнено ли задание на текущей локации
        self.current_location = ""  # Текущая локация

    def start_game(self):
        # Начало игры
        self.player_name = input("Введите ваше имя: ")  # Получаем имя игрока
        self.player_age = int(input("Введите ваш возраст: "))  # Получаем возраст игрока

        if self.player_age < 6:
            # Проверка возраста игрока
            print("Ошибка! Игра предназначена для игроков старше 6 лет.")
            return

        print(f"Добро пожаловать, {self.player_name}! Начинаем игру на острове {self.locations[0]}.")

        helpers = {
            "Пляж": "Меня зовут Капитан Чарльз, я Ваш помощник на пляже: здесь вы найдете сундук с кристаллами.",
            "Джунгли": "Меня зовут Лора Робинс, я Ваш помощник в джунглях: осторожно, здесь могут быть ловушки.",
            "Водопад": "А я Пиратский призрак, я Ваш помощник у водопада: ищите сундук в горячих и опасных местах.",
            "Древние Руины": "Здесь скрыты древние тайны и опасности. Помощников нет, вы наедине со своими испытаниями."
        }

        for location in self.locations:
            # Проходим по всем доступным локациям
            self.current_location = location
            self.task_completed = False
            print(helpers[self.current_location])  # Выводим информацию о текущей локации и ее помощнике
            while not self.task_completed and self.player_lives > 0:
                # Пока задание на текущей локации не выполнено и у игрока есть жизни
                self.explore_location()  # Проводим исследование локации
                if not self.task_completed:
                    print("Продолжаем исследование...")

        if self.crystals_found == 12:
            # Проверка на количество найденных кристаллов
            print("Вы нашли сундуки с кристаллами на всех островах! Поздравляем с победой!")
        else:
            print("Игра окончена. Вы проиграли.")

    def explore_location(self):
        # Исследование локации
        print(f"Вы находитесь на острове {self.current_location}.")
        print("Ваше задание: найти сундук с кристаллами.")

        found_chest = input("Нажмите 'Y', если нашли сундук, или 'N', если не нашли: ").lower()

        if found_chest == 'y':
            # Проверка на нахождение сундука
            self.task_completed = True  # Задание выполнено
            self.crystals_found += 3  # Увеличиваем количество найденных кристаллов
            print("Вы нашли сундук с кристаллами! Задание выполнено!")
            print(f"Теперь у вас {self.crystals_found} кристаллов.")
        else:
            print("Вы продолжаете искать...")
            self.player_lives -= 1  # Уменьшаем количество жизней
            if self.player_lives == 0:
                print("У вас закончились жизни. Игра окончена.")


# Создаем экземпляр игры и запускаем игру
game = IslandExplorerGame()
game.start_game()
