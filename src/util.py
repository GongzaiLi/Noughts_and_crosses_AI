import copy


def successors(board, player):
    act = []
    for row_i, row in enumerate(board):
        for col_i, col in enumerate(row):
            if col == ".":
                copy_board = copy.deepcopy(board)
                copy_board[row_i][col_i] = player
                act.append([copy_board, (row_i, col_i)])
    return act


def utility(terminal):
    if terminal.winner_player is None:
        return 0
    return 1 if "X" == terminal.winner_player else -1
