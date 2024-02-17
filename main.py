from GameBoard import GameBoard

game_board = GameBoard()

# Game loop
game_board.print_game_map()
while True:
    direction = input("Move (up, down, left, right): ").lower()
    if direction in ["up", "down", "left", "right"]:
        game_board.move_character(direction)
        game_board.move_enemy_towards_player()
        game_board.print_game_map()
        game_board.check_for_events()
    else:
        print("Invalid direction. Please choose 'up', 'down', 'left', or 'right'.")




