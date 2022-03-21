def initial_state():
    return [''] * 9


def actions(state):
    return [i for i in range(9) if state[i] == '']


def result(state, move, player):
    a = state.copy()
    a[move] = player
    return a


def opponent(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


def is_terminal(state):
    if all([v != '' for v in state]):
        return True
    return _has_line(state, 'X') or _has_line(state, 'O')


def who_won(table):
    x = _has_line(table, 'X')
    o = _has_line(table, 'O')

    if x and not o:
        return 'X'
    if o and not x:
        return 'O'
    return ''


def _has_line(state, player):
    for i in [0, 3, 6]:
        if state[i] == state[i + 1] == state[i + 2] == player:
            return True
    for i in [0, 1, 2]:
        if state[i] == state[i + 3] == state[i + 6] == player:
            return True
    if state[0] == state[3 + 1] == state[2 * 3 + 2] == player:
        return True
    if state[2] == state[3 + 1] == state[2 * 3] == player:
        return True
    return False
