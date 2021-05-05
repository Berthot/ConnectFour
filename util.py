def create_board():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
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


def write_two(board, coordinate):
    board[coordinate[1]][coordinate[0]] = 2


def verification_bla(board):
    # vertical
    for i in range(0, 3):
        for i1 in range(0, 7):
            if board[i, i1] == board[i + 1, i1] == board[i + 2, i1] == board[i + 3, i1] != 0:
                return True

    # horizontal
    for a in range(0, 4):
        for a1 in range(0, 6):
            if board[a1, a] == board[a1, a + 1] == board[a1, a + 2] == board[a1, a + 3] != 0:
                return True

    # vertical \
    for b in range(0, 3):
        for b1 in range(0, 4):
            if board[b, b1] == board[b + 1, b1 + 1] == board[b + 2, b1 + 2] == board[b + 3, b1 + 3] != 0:
                return True

    # vertical /
    for j in range(0, 3):
        for k in range(0, 4):
            if board[j, k] == board[j + 1, k - 1] == board[j + 2, k - 2] == board[j + 3, k - 3] != 0:
                return True


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
    print(diags)

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
