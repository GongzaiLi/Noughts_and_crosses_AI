from student_answer import optimal_move as student_optimal


def board_from_string(board_str):
    return [list(raw.strip()) for raw in board_str.strip().splitlines()]


def display(board):
    print(f"+{'-' * len(board)}+")
    for raw in board:
        print(f'|{"".join(raw)}|')
    print(f"+{'-' * len(board)}+")


def is_terminal(board):
    return all([col != '.' for raw in board for col in raw])


def opponent(player):
    return 'X' if player == 'O' else 'O'


def apply(move, board, player):
    board[move[0]][move[1]] = player


if __name__ == '__main__':

    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        board_str = """\
        ...
        ...
        ...
        """

        board = board_from_string(board_str)
        player = student = 'X'
        print(board)
        display(board)
        while not is_terminal(board):
            move_function = student_optimal if player == student else server_optimal
            move = move_function(board, player)
            print(f"{player} plays {move}:")
            apply(move, board, player)
            display(board)
            player = opponent(player)
