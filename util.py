def create_board():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    return board


def put(board, n):
    n -= 1
    acc = 5
    for i in board:
        if i[n] != 0:
            acc -= 1
    return [n, acc]


def print_board(board):
    print(board)
    print("\n")


def write_one(board, coordinate):
    board[coordinate[1]][coordinate[0]] = 1
    print([coordinate[1]],[coordinate[0]])


def write_two(board, coordinate):
    board[coordinate[1]][coordinate[0]] = 2
    print([coordinate[1]],[coordinate[0]])


def winner_text(player):
    if player == 1:
        return f" jogador 2 venceu !!!"
    elif player == 2:
        return f" jogador 1 venceu !!!"


def is_over(board):
    """
    :autor Valdemar ceccon
    """
    lines = ["".join([str(c) for c in column]) for column in board]

    for line in lines:
        if check_four(line):
            return True

    columns = ["".join([str(c) for c in x]) for x in map(list, zip(board))]

    for col in columns:
        if check_four(col):
            return True

    diags = ["".join([str(c) for c in column]) for column in diagonals(board)]


    for diag in diags:
        if check_four(diag):
            return True

    anti_diags = ["".join([str(c) for c in column]) for column in antidiagonals(board)]

    for anti_diag in anti_diags:
        if check_four(anti_diag):
            return True

    return False


def check_four(row_string):
    return '1' * 4 in row_string or '2' * 4 in row_string


def diagonals(matrix):
    h, w = len(matrix), len(matrix[0])
    return [[matrix[h - p + q - 1][q]
             for q in range(max(p - h + 1, 0), min(p + 1, w))]
            for p in range(h + w - 1)]


def antidiagonals(matrix):
    h, w = len(matrix), len(matrix[0])
    return [[matrix[p - q][q]
             for q in range(max(p - h + 1, 0), min(p + 1, w))]
            for p in range(h + w - 1)]
