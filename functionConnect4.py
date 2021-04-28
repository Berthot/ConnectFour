import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

def put(board,n):
    n -= 1
    acc = 5
    for i in board:
        if i[n] != 0:
            acc -= 1
    return [n,acc]

def print_board(board):
    print(board)
    print("\n")

def write_one(board,coordinate):
    board[coordinate[1],coordinate[0]] = 1

def write_two(board,coordinate):
    board[coordinate[1],coordinate[0]] = 2

def verification(board):
    #vertical
    for i in range(0, 3):
        for i1 in range(0, 7):
            if board[i, i1] == board[i+1, i1] == board[i+2, i1] == board[i+3, i1] != 0:
                return True

    #horizontal
    for a in range(0, 4):
        for a1 in range(0, 6):
            if board[a1, a] == board[a1, a+1] == board[a1, a+2] == board[a1, a+3] != 0:
                return True

    #vertical \
    for b in range(0 ,3):
        for b1 in range(0, 4):
            if board[b,b1] == board[b+1,b1+1] == board[b+2,b1+2] == board[b+3,b1+3] != 0:
                return True
    #vertical /
    #for b in range(0, 3):
    #    for b1 in range(3, 7):
    #        if board[b, b1] == board[b+1, b1-1] == board[b+2, b1-2] == board[b+3, b1-3] != 0:
    #            print("talvez seja um erro")
    #            return True

def print_winner(player):
    if player == 1:
        return f" jogador 2 venceu !!!"
    elif player == 2:
        return f" jogador 1 venceu !!!"