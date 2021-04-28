from Board import Board
import typing


class Game:

    def __init__(self):
        self.board = Board()

    def start(self, columns=7, lines=6):
        self.board.create_new_board(columns, lines)

    def end_game(self) -> bool:
        self.board = self.board
        return False

    def move(self, position: int, player: str):
        self.board.set_new_ball(position, player)
        return self.board

    def win(self):
        for line in self.board:
            for item in line:
                pass

