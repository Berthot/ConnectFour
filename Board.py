class Board:

    def __init__(self):
        self.__board = []
        self._columns = 0
        self.lines = 0
        self.__last_row = -1
        self.__last_item = -1
        # self.__player = True  # True player1[K] False player2[J]

    def create_new_board(self, columns=7, rows=6):
        self._columns = columns
        self.lines = rows
        for row in range(0, rows):
            self.__board.append([])
            for column in range(0, columns):
                self.__board[row].append(None)
        self.__board[1][3] = True
        self.__board[2][2] = True
        self.__board[3][1] = True

    def __str__(self):
        text = ''
        header = [f'{x} | ' for x in range(1, self.lines + 2)]
        text += 'X | ' + ''.join(header) + '\n'
        acc = 0
        for i in self.__board:
            first_line = True
            acc += 1
            for item in i:
                if item is None:
                    name = '-'
                else:
                    name = 'K' if item else 'J'
                if first_line:
                    text += f"{acc} | {name} | "
                    first_line = False
                    continue
                text += f"{name} | "
            text += '\n'

        return text

    def __set_value(self, x, y, value):
        self.__board[x][y] = value
        print(f'{value} [{x}] [{y}]')

    def value_can_be_set(self, position: int, player: bool):
        pos = position - 1
        column = [x[pos] for x in self.__board if x[pos] is None]
        if self.__line_full(column):
            print("valor not available")
            return False
        self.__set_value(len(column) - 1, pos, player)
        self.__last_row = len(column) - 1
        self.__last_item = pos

        return True

    def get_position(self, x: int, y: int):
        try:
            return self.__board[x][y]
        except IndexError:
            return None

    @property
    def board_full(self):
        return all([self.__line_full(x) for x in self.__board])

    @staticmethod
    def __line_full(line: list):
        return all([x is not None for x in line])

    def get_board(self):
        return [*self.__board]

    @property
    def get_horizon(self):
        return self.__board[self.__last_row]

    @property
    def get_vertical(self):
        return [self.__board[x][self.__last_item] for x in range(6)]

    @property
    def get_diagonal(self):
        # 5-0 > 4-1 > 3-2 > 2-3 > 1-4 > 0-5
        result = []
        row = self.__last_row     # 5
        items = self.__last_item  # 0
        while row != 0:
            if items == 7:
                break
            result.append(self.__board[row][items])
            row -= 1
            items += 1
        return result


if __name__ == '__main__':
    board = Board()

    board.create_new_board()

    # board.value_can_be_set(1, 'K')

    # print(board.board_full())

    print(board)
