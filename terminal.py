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

        right_check = all([right == self.board[i][len(self.board) - 1 - i] and right != '.' for i in
                           range(1, len(self.board))])  # range(start, end) end not call

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
