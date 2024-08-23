import random as rnd
from home_11 import check_queens


def generate_board():
    rows = [i for i in range(1, 9)]
    cols = [j for j in range(1, 9)]
    rnd.shuffle(cols)
    return list(zip(rows, cols))


def generate_boards():
    boards_list = []
    while len(boards_list) < 4:
        board = generate_board()
        if check_queens(board):
            boards_list.append(f'{board = }')
    return boards_list

print(generate_boards())