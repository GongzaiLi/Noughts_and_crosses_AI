from student_answer import optimal_move as student_optimal


def board_from_string(board_str):
    return [list(row.strip()) for row in board_str.strip().splitlines()]


def display(board):
    print(f"+{'-' * len(board)}+")
    for row in board:
        print(f'|{"".join(row)}|')
    print(f"+{'-' * len(board)}+")


class Terminal:
    def __init__(self, board):
        self.board = board
        self.winner_player = None

    def is_row_has_win(self):
        for row in self.board:
            if row.count(row[0]) == len(row):
                self.winner_player = row[0]
                return True
        return False

    def is_col_has_win(self):
        for col_i, col in enumerate(self.board[0]):
            if all([col == row[col_i] for row in self.board]):
                self.winner_player = col
                return True
        return False

    def is_cross_has_win(self):
        left = self.board[0][0]
        right = self.board[0][-1]
        left_check = all([left == self.board[i][i] for i in range(1, len(self.board))])
        right_check = all([left == self.board[i][i] for i in range(len(self.board), 1, -1)])
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
    print(board)
    display(board)

    while not Terminal(board).is_terminal():
        move_function = student_optimal if player == student else server_optimal
        move = move_function(board, player)
        print(f"{player} plays {move}:")
        apply(move, board, player)
        display(board)
        player = opponent(player)
