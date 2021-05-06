def legal_move(board):
    list_legal_move = []
    for i in reversed(range(0, 7)):
        acc = 5
        for i1 in range(0, 6):
            if board[i1][i] != 0 and 1 and acc > 0:
                acc -= 1
        if acc >= 0:
            list_legal_move.append([acc, i])
    list_legal_move.reverse()
    return list_legal_move


def walk_move(x, y):
    if x > 0:
        return [x - 1, y]


def all_walk(move_list):
    list_rolled = []
    for move in move_list:
        list_rolled.append(walk_move(move[0], move[1]))
    return list_rolled


def write_all(legal_move, all_walk):
    import copy
    all_lista = []
    for i in range(len(legal_move)):
        legal_move_copy = copy.deepcopy(legal_move)
        legal_move_copy[i] = all_walk[i]
        all_lista.append(legal_move_copy)
    return all_lista
