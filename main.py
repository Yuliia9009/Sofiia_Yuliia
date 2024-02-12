class IslandExplorerGame:
    def __init__(self):
        self.player_name = ""
        self.player_age = 0
        self.player_lives = 5
        self.crystals_found = 0
        self.locations = ["Пляж", "Лагуна", "Джунгли", "Вулкан"]
        self.task_completed = False

    def start_game(self):
        self.player_name = input("Введите ваше имя: ")
        self.player_age = int(input("Введите ваш возраст: "))

        if self.player_age < 6:
            print("Ошибка! Игра предназначена для игроков старше 6 лет.")
            return

        print(f"Добро пожаловать, {self.player_name}! Начинаем игру на острове {self.locations[0]}.")

        helpers = {
            "Пляж": "Помощник на пляже: здесь вы найдете сундук с кристаллами.",
            "Лагуна": "Помощник у лагуны: кристаллы спрятаны где-то вокруг.",
            "Джунгли": "Помощник в джунглях: осторожно, здесь могут быть ловушки.",
            "Вулкан": "Помощник на вулкане: ищите сундук в горячих и опасных местах."
        }

        for location in self.locations:
            self.current_location = location
            self.task_completed = False
            print(helpers[self.current_location])
            while not self.task_completed and self.player_lives > 0:
                self.explore_location()
                if not self.task_completed:
                    print("Продолжаем исследование...")

        if self.crystals_found == 12:
            print("Вы нашли сундуки с кристаллами на всех островах! Поздравляем с победой!")
        else:
            print("Игра окончена. Вы проиграли.")

    def explore_location(self):
        print(f"Вы находитесь на острове {self.current_location}.")
        print("Ваше задание: найти сундук с кристаллами.")

        found_chest = input("Нажмите 'Y', если нашли сундук, или 'N', если не нашли: ").lower()

        if found_chest == 'y':
            self.task_completed = True
            self.crystals_found += 3
            print("Вы нашли сундук с кристаллами! Задание выполнено!")
            print(f"Теперь у вас {self.crystals_found} кристаллов.")
        else:
            print("Вы продолжаете искать...")
            self.player_lives -= 1
            if self.player_lives == 0:
                print("У вас закончились жизни. Игра окончена.")


# Создаем экземпляр игры и запускаем игру
game = IslandExplorerGame()
game.start_game()