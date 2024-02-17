class GameBoard:
    def __init__(self, rows=20, cols=20):
        self.rows = rows
        self.cols = cols
        self.game_map = [["." for _ in range(cols)] for _ in range(rows)]
        self.player_position = None
        self.enemy_positions = {}
        self.treasure_positions = {}
        self.final_treasure_position = None
        self.player_inventory = []  # Initialize the player's inventory as an empty list
        self.init_map()
        self.insert_characters()

    def check_for_events(self):
        # Check if player found a treasure
        if tuple(self.player_position) in self.treasure_positions:
            print("Treasure found!")
            self.on_treasure_found()

        if tuple(self.player_position) in self.enemy_positions:
            self.on_enemy_collision()

        if self.final_treasure_position and tuple(self.player_position) == self.final_treasure_position:
            self.on_final_treasure_found()

    def init_map(self):
        for i in range(self.cols):
            self.game_map[0][i] = 'X'  # Top wall
            self.game_map[self.rows - 1][i] = 'X'  # Bottom wall
        for i in range(self.rows):
            self.game_map[i][0] = 'X'  # Left wall
            self.game_map[i][self.cols - 1] = 'X'  # Right wall

    def insert_characters(self):
        self.player_position = [5, 5]
        self.game_map[5][5] = 'P'  # Player

        enemy_positions = [(2, 7)]  # Add more tuples as needed
        for pos in enemy_positions:
            self.enemy_positions[pos] = 'E'
            self.game_map[pos[0]][pos[1]] = 'E'

        self.treasure_positions[(3, 3)] = 'T'
        self.game_map[3][3] = 'T'  # Treasure

    def move_character(self, direction):
        movements = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        move = movements[direction]
        new_position = [self.player_position[0] + move[0], self.player_position[1] + move[1]]

        if self.is_valid_move(new_position):
            self.game_map[self.player_position[0]][self.player_position[1]] = "."
            self.player_position = new_position
            self.game_map[new_position[0]][new_position[1]] = 'P'
        else:
            print("Move not allowed.")

    def is_valid_move(self, position):
        return 0 <= position[0] < self.rows and 0 <= position[1] < self.cols and self.game_map[position[0]][
            position[1]] != 'X'

    def move_enemy_towards_player(self):
        for enemy_pos in list(self.enemy_positions.keys()):
            new_enemy_position = list(enemy_pos)

            if self.player_position[1] > enemy_pos[1]:
                new_enemy_position[1] += 1
            elif self.player_position[1] < enemy_pos[1]:
                new_enemy_position[1] -= 1
            elif self.player_position[0] > enemy_pos[0]:
                new_enemy_position[0] += 1
            elif self.player_position[0] < enemy_pos[0]:
                new_enemy_position[0] -= 1

            if self.is_valid_move(new_enemy_position):
                self.game_map[enemy_pos[0]][enemy_pos[1]] = '.'
                del self.enemy_positions[enemy_pos]
                self.enemy_positions[tuple(new_enemy_position)] = 'E'
                self.game_map[new_enemy_position[0]][new_enemy_position[1]] = 'E'

    def print_game_map(self):
        tile_symbols = {
            "wall": "██",
            "player": "⬤ ",
            "ground": "  ",
            "treasure": "◆ ",
            "enemy": "☠ ",
            "chest": "C"
        }

        visual_map = [["  " for _ in range(self.cols)] for _ in range(self.rows)]  # Initialize with ground symbols

        # Place walls
        for i in range(self.cols):
            visual_map[0][i] = tile_symbols["wall"]  # Top wall
            visual_map[self.rows - 1][i] = tile_symbols["wall"]  # Bottom wall
        for i in range(self.rows):
            visual_map[i][0] = tile_symbols["wall"]  # Left wall
            visual_map[i][self.cols - 1] = tile_symbols["wall"]  # Right wall

        # Place player, enemies, and treasures based on their positions
        visual_map[self.player_position[0]][self.player_position[1]] = tile_symbols["player"]
        for enemy_pos in self.enemy_positions:
            visual_map[enemy_pos[0]][enemy_pos[1]] = tile_symbols["enemy"]
        for treasure_pos in self.treasure_positions:
            visual_map[treasure_pos[0]][treasure_pos[1]] = tile_symbols["treasure"]
        if self.final_treasure_position:
            visual_map[self.final_treasure_position[0]][self.final_treasure_position[1]] = tile_symbols["chest"]


        # Print the visual representation
        for row in visual_map:
            print("".join(row))

    def on_treasure_found(self):
        self.player_inventory.append("sleeping dart")
        print("You obtained a sleeping dart!")
        # Remove the treasure and trigger any additional events, such as spawning more enemies
        del self.treasure_positions[tuple(self.player_position)]
        print("Press enter to continue...")
        input()

    def on_enemy_collision(self):
        print("You've encountered an enemy!")
        if "sleeping dart" in self.player_inventory:
            # Use the sleeping dart to avoid the confrontation
            enemy_pos = tuple(self.player_position)
            if enemy_pos in self.enemy_positions:
                self.remove_enemy(enemy_pos)
                self.player_inventory.remove("sleeping dart")
                print("You used a sleeping dart to escape the enemy!")
        else:
            self.confront_enemy()

    def remove_enemy(self, enemy):
        del self.enemy_positions[enemy]
        if not self.enemy_positions:
            self.spawn_final_treasure()

    def confront_enemy(self):
        print("The enemy blocks your path!")
        print("1: Try to reason with the enemy.")
        print("2: Attempt a sneak attack.")
        choice = input("Choose your action (1 or 2): ")

        if choice == "1":
            print("You attempt to reason with the enemy...")
            print("The enemy is not convinced and attacks you. Game Over!")
            exit()
        elif choice == "2":
            print("You attempt a sneak attack...")
            # Successful sneak attack
            enemy_pos = tuple(self.player_position)
            if enemy_pos in self.enemy_positions:
                self.remove_enemy(enemy_pos)
            print("Success! The enemy is taken by surprise and defeated.")
        else:
            print("Confused, you hesitate. The enemy seizes the moment and attacks. Game Over!")
            exit()

    def spawn_final_treasure(self):
        self.final_treasure_position = (10, 10)
        self.game_map[10][10] = 'F'  # Mark the final treasure on the map
        print("All gueards dead, magical treasure appears in the middle of the room")
        self.print_game_map()

    def on_final_treasure_found(self):
        crystals = 100  # Example amount
        note = "The journey is the treasure."
        self.write_treasure_contents_to_file(crystals, note)
        print("You've found the final treasure containing crystals and a note!")
        print("well done!")
        exit()


    def write_treasure_contents_to_file(self, crystals, note):
        with open("treasure_contents.txt", "w") as file:
            file.write(f"Crystals: {crystals}\n")
            file.write(f"Note: {note}\n")


