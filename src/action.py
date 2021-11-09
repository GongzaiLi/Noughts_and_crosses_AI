from src.max_min_search import *

def sort_helper(v):
    return -v[0], v[1]


def optimal_move(board, player):
    """
    action function ++
    note
    1: make sure the board does not get accidentally modified in your function.
    2: You will need to do pruning in order to meet the required time constraint.
    3: (????) If allocating and deallocating memory (creating new boards in each stack frame) is slowing down your program,
        you can keep track moves in stack frames and work with only one board
        (i.e. move, make the recursive call, and then 'unmove' all on the same board).
    """
    first_moves = successors(board, player)
    v = []
    for n_board, move, in first_moves:
        alpha = -math.inf
        bate = math.inf
        v.append((min_value(n_board, alpha, bate, player), move))
    v.sort(key=sort_helper)
    return v[0][-1]


def sort_helper_for_server(v):
    return v[0], v[1]


def server_optimal(board, player):
    """
    action function ++
    note
    1: make sure the board does not get accidentally modified in your function.
    2: You will need to do pruning in order to meet the required time constraint.
    3: (????) If allocating and deallocating memory (creating new boards in each stack frame) is slowing down your program,
        you can keep track moves in stack frames and work with only one board
        (i.e. move, make the recursive call, and then 'unmove' all on the same board).
    """
    first_moves = successors(board, player)

    v = []
    for n_board, move, in first_moves:
        alpha = -math.inf
        bate = math.inf
        v.append((max_value(n_board, alpha, bate, player), move))
    v.sort(key=sort_helper_for_server)

    return v[0][-1]
