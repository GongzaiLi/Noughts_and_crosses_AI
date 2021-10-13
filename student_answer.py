import copy
import math


class Terminal:
    def __init__(self, board):
        self.board = board
        self.winner_player = None

    def is_row_has_win(self):
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != '.':
                self.winner_player = row[0]
                return True
        return False

    def is_col_has_win(self):
        for col_i, col in enumerate(self.board[0]):
            if all([col == row[col_i] and col != '.' for row in self.board]):
                self.winner_player = col
                return True
        return False

    def is_cross_has_win(self):
        left = self.board[0][0]
        right = self.board[0][-1]
        left_check = all([left == self.board[i][i] and left != '.' for i in range(1, len(self.board))])

        right_check = all([left == self.board[i][i] and right != '.' for i in
                           range(len(self.board) - 1, 0, -1)])  # range(start, end) end not call

        if left_check:
            self.winner_player = left
            return True
        if right_check:
            self.winner_player = right
            return True
        return False

    def game_over(self):
        return all([col != '.' for row in self.board for col in row])

    def is_terminal(self):

        if self.is_row_has_win() or self.is_col_has_win() or self.is_cross_has_win():
            return True
        if self.game_over():
            self.winner_player = None
            return True
        return False


def action(board, player):
    act = []
    for row_i, row in enumerate(board):
        for col_i, col in enumerate(row):
            if col == ".":
                copy_board = copy.deepcopy(board)
                copy_board[row_i][col_i] = player
                act.append(copy_board)
    return act


def max_value(board, alpha, bate, player):
    terminal = Terminal(board)
    if terminal.is_terminal():
        if terminal.winner_player is None:
            return 0
        return 1 if player == terminal.winner_player else -1
    v = -math.inf

    for state in action(board, 'X'):
        v = max(v, min_value(state, alpha, bate, player))
        alpha = max(alpha, v)

        if alpha >= bate: return v

    return v


def min_value(board, alpha, bate, player):
    terminal = Terminal(board)
    if terminal.is_terminal():
        if terminal.winner_player is None:
            return 0
        return 1 if player == terminal.winner_player else -1

    v = math.inf
    for state in action(board, 'O'):
        v = min(v, max_value(state, alpha, bate, player))

        bate = min(bate, v)
        if alpha >= bate:

            return v
    return v


def alpha_bate_search(board, player):
    """
    todo
    """
    alpha = -math.inf
    bate = math.inf
    v = max_value(board, alpha, bate, player)
    return v


print(alpha_bate_search([['.', '.'], ['.', '.']], 'X'))


def optimal_move(board, player):
    """
    note
    1: make sure the board does not get accidentally modified in your function.
    2: You will need to do pruning in order to meet the required time constraint.
    3: (????) If allocating and deallocating memory (creating new boards in each stack frame) is slowing down your program,
        you can keep track moves in stack frames and work with only one board
        (i.e. move, make the recursive call, and then 'unmove' all on the same board).
    """
    # check winner / \ | -
    # generator the game tree?
    best_move = []
    copy_board = copy.deepcopy(board)

    # If multiple moves are equally good, the function must return one that has the lowest row number and then the lowest column number.

    # The size of the search space will be roughly about that of an empty board with n=3.
    # compute the optimal move in less than a second.
    # return (raw, col)
