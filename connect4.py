import functionConnect4 as fc


winner = False
player = 1

board = fc.create_board()

while not winner:
    if player == 1:
        print("Player 1, sua vez de jogar")
        n1 = int(input("Digite um numero de [1,7] : "))
        coordinate = fc.put(board,n1)
        fc.write_one(board,coordinate)
        fc.print_board(board)
        player = 2

    elif player == 2:
        print("Player 2, sua vez de jogar, 0,7")
        n2 = int(input("Digite um numero de [1,7] : "))
        coordinate = fc.put(board, n2)
        fc.write_two(board, coordinate)
        fc.print_board(board)
        player = 1
    winner = fc.verification(board)
fc.print_winner(player)

