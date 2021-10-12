import math


def max_value(state, alpha, bate):
    if type(state) is not list:
        return state
    v = -math.inf
    for node in state:
        v = max(v, min_value(node, alpha, bate))
        alpha = max(alpha, v)
        if alpha >= bate: return v
    return v


def min_value(state, alpha, bate):
    if type(state) is not list:
        return state
    v = math.inf
    for node in state:
        v = min(v, max_value(node, alpha, bate))
        bate = min(bate, v)
        if alpha >= bate: return v
    return v


def alpha_bate_search(state):
    """
    todo
    """
    alpha = -math.inf
    bate = math.inf
    v = max_value(state, alpha, bate)
    return v


def optimal_move(board, player):
    """
    """
    # generator the game tree?
    game_tree = [ for i in ]
