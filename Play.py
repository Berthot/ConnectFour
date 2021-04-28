import os

from Game import Game


def clear_terminal(actual_board):
    # os.system('cls' if os.name == 'nt' else 'clear')
    # os.system('clear')
    print('\n' * 20)
    print(actual_board)


def get_position():
    while True:
        try:
            var = int(input("Insert the position between 1 - 7: "))
            if var in range(1, 8):
                return var
        except ValueError:
            print("Invalid value, please select number between 1 - 7: ")


if __name__ == '__main__':
    game = Game()
    game.start()
    print(game.board)
    while game.has_winner:
        print(f"Turn player {game.player_name}.")
        position = get_position()
        if game.player_play(position):
            continue
        print(game.board)

        if game.win():
            print(game.board)
            print(f"Player {game.player_name} WINS!")
            break
        # clear_terminal(game.board)
