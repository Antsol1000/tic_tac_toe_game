from game import *

MINUS_INF = -10e9
PLUS_INF = 10e9


def alpha_beta(player, state):
    value, move = max_ab(player, player, state, MINUS_INF, PLUS_INF)
    return move


def max_ab(root_player, current_player, state, alpha, beta):
    if is_terminal(state):
        return utility(root_player, who_won(state)), None
    v, move = MINUS_INF, None
    for a in actions(state):
        v2, a2 = min_ab(root_player, opponent(current_player), result(state, a, current_player), alpha, beta)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta:
            return v, move
    return v, move


def min_ab(root_player, current_player, state, alpha, beta):
    if is_terminal(state):
        return utility(root_player, who_won(state)), None
    v, move = PLUS_INF, None
    for a in actions(state):
        v2, a2 = max_ab(root_player, opponent(current_player), result(state, a, current_player), alpha, beta)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha:
            return v, move
    return v, move


def utility(player, score):
    if score == player:
        return 1
    elif score == '':
        return 0
    else:
        return -1
