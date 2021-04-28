import os

from Game import Game


def clear_terminal():
    # os.system('cls' if os.name == 'nt' else 'clear')
    # os.system('clear')
    print('\n' * 20)


if __name__ == '__main__':
    game = Game()
    game.start()
    clear_terminal()
    print(game.board)
    # while game.end_game():
    #     game.move(0, 'J')
    #     game.move(0, 'K')
