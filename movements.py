
def arrowhead(n):
    return n * (490 / 7) - 62


def move_RIGHT(arrow_direction):
    if arrow_direction < 7:
        arrow_direction += 1
    return arrow_direction


def move_LEFT(arrow_direction):
    if arrow_direction > 1:
        arrow_direction -= 1
    return arrow_direction


def grid_space(n):
    list_number = [70, 140, 210, 280, 350, 420]
    return list_number[n]
