import numpy as np
import functionConnect4 as fc
import functionConnect4_Pygames as fcp
import pygame
import sys

winner = False
player = 1

board = fc.create_board()

pygame.init()

x = 492
y = 490
screen = pygame.display.set_mode((x,y))

squares = []

board_img = pygame.image.load("board.png")
arrow_img = pygame.image.load("arrow.png")

arrow_direction = 1

def arrow(y):
    screen.blit(arrow_img,(y,0))

def paint_square(x,y,player):
    size = 62
    if player == 1:
        square = pygame.Rect(x,y,size,size)
        return screen,[255, 0, 0,255],square

    else:
        square = pygame.Rect(x, y, size, size)
        return screen, [255,255,0, 255], square
#pygame.draw.rect(screen, [52, 58, 235, 255], square)
while not winner:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                arrow_direction = fcp.move_LEFT(arrow_direction)

            if event.key == pygame.K_RIGHT:
                arrow_direction = fcp.move_RIGHT(arrow_direction)

            if event.key == pygame.K_DOWN:
                if player == 1:
                    coordinate = fc.put(board,arrow_direction)
                    fc.write_one(board,coordinate)
                    squares.append(paint_square(fcp.arrowhead(arrow_direction), fcp.grid_space(coordinate[1]),player))
                    player = 2
                else:
                    coordinate = fc.put(board, arrow_direction)
                    fc.write_two(board,coordinate)
                    squares.append(paint_square(fcp.arrowhead(arrow_direction), fcp.grid_space(coordinate[1]), player))
                    player = 1
        winner = fc.verification(board)



    for i in squares:
        pygame.draw.rect(i[0], i[1], i[2])
    arrow(fcp.arrowhead(arrow_direction))
    screen.blit(board_img, (0, 60))
    pygame.display.update()
print(fc.print_winner(player))