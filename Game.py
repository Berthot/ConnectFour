from Board import Board


class Game:

    def __init__(self):
        self.board = Board()
        self.__has_winner = True
        self.__player = True  # True player1[K] False player2[J]

    def start(self):
        self.board.create_new_board()

    @property
    def player_name(self):
        # True player1[K] False player2[J]
        return 'K' if self.__player else 'J'

    @property
    def has_winner(self):
        return self.__has_winner

    def player_play(self, placed_on: int):
        return not self.board.value_can_be_set(placed_on, self.__player)

    def win(self):
        possible_wins = [
            self.validate_horizon(),
            self.validate_vertical()
        ]
        if any(possible_wins):
            return True
        self.__player = not self.__player
        return False

    def validate_horizon(self):
        horizon = self.board.get_horizon
        return self.validate_list(horizon)

    def validate_vertical(self):
        vertical = self.board.get_vertical
        return self.validate_list(vertical)

    def validate_horizon1(self):
        horizon1 = self.board.get_horizon()
        return self.validate_list(horizon1)

    def validate_list(self, array):
        seq = 0
        for x in array:
            if x == self.__player:
                seq += 1
            else:
                seq = 0
            if seq >= 4:
                return True
        return False
