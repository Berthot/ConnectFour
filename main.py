import time

import util
import movements
import pygame
import sys

winner = False
player = 1

board = util.create_board()

pygame.init()

x = 492
y = 490
screen = pygame.display.set_mode((x, y))

squares = []

board_img = pygame.image.load("board.png")
arrow_img = pygame.image.load("arrow.png")

arrow_position = 1


def arrow(y):
    screen.blit(arrow_img, (y, 0))


def paint_square(x, y, player):
    size = 62
    if player == 1:
        square = pygame.Rect(x, y, size, size)
        return screen, [255, 0, 0, 255], square

    else:
        square = pygame.Rect(x, y, size, size)
        return screen, [255, 255, 0, 255], square


def check_column_full(position):
    for row in board:
        if row[position - 1] == 0:
            return False
    return True


def place_disc():
    global player
    if check_column_full(arrow_position):
        return
    if player == 1:
        coordinate = util.put(board, arrow_position)
        util.write_one(board, coordinate)
        squares.append(paint_square(movements.arrowhead(arrow_position), movements.grid_space(coordinate[1]), player))
        player = 2
    else:
        coordinate = util.put(board, arrow_position)
        util.write_two(board, coordinate)
        squares.append(paint_square(movements.arrowhead(arrow_position), movements.grid_space(coordinate[1]), player))
        player = 1


if __name__ == '__main__':
    while not winner:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    arrow_position = movements.move_LEFT(arrow_position)

                if event.key == pygame.K_RIGHT:
                    arrow_position = movements.move_RIGHT(arrow_position)

                if event.key == pygame.K_DOWN:
                    place_disc()
                    winner = util.is_over(board)
                    # winner = util.is_over(board)

        for i in squares:
            pygame.draw.rect(i[0], i[1], i[2])
        arrow(movements.arrowhead(arrow_position))
        screen.blit(board_img, (0, 60))
        pygame.display.update()
    print(util.winner_text(player))
    time.sleep(15)
