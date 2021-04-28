class Board:

    def __init__(self):
        self.__board = []
        self._columns = 0
        self.lines = 0

    def create_new_board(self, columns=7, lines=6):
        self._columns = columns
        self.lines = lines
        for line in range(0, lines):
            self.__board.append([])
            for column in range(0, columns):
                self.__board[line].append('-')
        self.__board[5][0] = 'J'

    def __str__(self):
        text = ''
        header = [f'{x} | ' for x in range(1, self.lines + 2)]
        text += 'X | ' + ''.join(header) + '\n'
        acc = 0
        for i in self.__board:
            first_line = True
            acc += 1
            for item in i:
                if first_line:
                    text += f"{acc} | {item} | "
                    first_line = False
                    continue
                text += f"{item} | "
            text += '\n'

        return text

    def set_value(self, line, column, value):
        self.__board[line][column] = value

    def set_new_ball(self, position: int, player: str):
        pos = position - 1
        column = [x[pos] for x in self.__board if x[pos] == '-']
        if self.__line_full(column):
            print("valor not available")
            return False
        self.set_value(len(column) - 1, pos, player)
        return True

    def board_full(self):
        return all([self.__line_full(x) for x in self.__board])

    @staticmethod
    def __line_full(line: list):
        return all([x != '-' for x in line])

    def get_board(self):
        return [*self.__board]


if __name__ == '__main__':
    board = Board()

    board.create_new_board()

    board.set_new_ball(1, 'K')

    # print(board.board_full())

    print(board)
