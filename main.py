from src.action import optimal_move as student_optimal
from src.action import server_optimal
from src.terminal import *


def board_from_string(board_str):
    return [list(row.strip()) for row in board_str.strip().splitlines()]


def display(board):
    print(f"+{'-' * len(board)}+")
    for row in board:
        print(f'|{"".join(row)}|')
    print(f"+{'-' * len(board)}+")


def opponent(player):
    return 'X' if player == 'O' else 'O'


def apply(move, board, player):
    board[move[0]][move[1]] = player


if __name__ == '__main__':
    board_str = """\
        ...
        ...
        ...
        """

    board = board_from_string(board_str)
    player = student = 'X'
    display(board)

    while not Terminal(board).is_terminal():
        move_function = student_optimal if player == student else server_optimal
        move = move_function(board, player)
        print(f"{player} plays {move}:")
        apply(move, board, player)
        display(board)
        player = opponent(player)
