def check(table):
    """
    this function check the status of board in tic tac toe game
    :param table: tic tac toe board
    :return "X" - win "X", "O" - win "O", "draw" - draw, "go" - available to play
    """
    for j in range(3):
        # check for win in rows
        if table[3 * j] == table[3 * j + 1] == table[3 * j + 2] and table[3 * j] != "":
            return table[3 * j]
        # check for win in columns
        if table[j] == table[j + 3] == table[j + 6] and table[j] != "":
            return table[j]

    # check for win in diagonals
    if table[0] == table[4] == table[8] and table[4] != "":
        return table[4]
    if table[2] == table[4] == table[6] and table[4] != "":
        return table[4]

    if "" not in table:
        return "draw"
    return "go"
