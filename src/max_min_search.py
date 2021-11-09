from src.terminal import *
from src.util import *
import math


def max_value(board, alpha, bate, player):
    terminal = Terminal(board)
    if terminal.is_terminal():
        return utility(terminal)
    v = -math.inf

    for state, _ in successors(board, 'X'):
        v = max(v, min_value(state, alpha, bate, player))
        alpha = max(alpha, v)

        if alpha >= bate:
            return v

    return v


def min_value(board, alpha, bate, player):
    terminal = Terminal(board)
    if terminal.is_terminal():
        return utility(terminal)

    v = math.inf
    for state, _ in successors(board, 'O'):
        v = min(v, max_value(state, alpha, bate, player))

        bate = min(bate, v)
        if alpha >= bate:
            return v
    return v
