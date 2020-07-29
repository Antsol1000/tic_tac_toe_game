from tkinter import *
import status
import tkinter.font as font

root = Tk()
root.title("TIC TAC TOE GAME")

sign = ['X', 'O']
score = {'X': 0, 'O': 0}

# last_ptr contains who start last game
last_ptr = 0
# ptr point who has the move
ptr = 0

# board is list which represents the state of buttons
board = [""] * 9
buttons = []

symbol_font = font.Font(size=20, weight='bold')
com_font = font.Font(size=11)


def new_game():
    """
    this function reset all variables to start a new game
    it displays clear buttons ready to click
    """
    global ptr, buttons, board, last_ptr
    ptr = last_ptr % 2
    board = [""] * 9

    # display first row with scoreboard and initial statement
    Label(root, text="Good Luck!", width=11, height=2, font=com_font).grid(row=0, column=1)
    Label(root, text="X score: " + str(score['X']), width=11, height=2, font=com_font).grid(row=0, column=0)
    Label(root, text="O score: " + str(score['O']), width=11, height=2, font=com_font).grid(row=0, column=2)

    # create and display buttons
    buttons = [Button(root, width=6, height=3, font=symbol_font, command=lambda: click(0)),
               Button(root, width=6, height=3, font=symbol_font, command=lambda: click(1)),
               Button(root, width=6, height=3, font=symbol_font, command=lambda: click(2)),
               Button(root, width=6, height=3, font=symbol_font, command=lambda: click(3)),
               Button(root, width=6, height=3, font=symbol_font, command=lambda: click(4)),
               Button(root, width=6, height=3, font=symbol_font, command=lambda: click(5)),
               Button(root, width=6, height=3, font=symbol_font, command=lambda: click(6)),
               Button(root, width=6, height=3, font=symbol_font, command=lambda: click(7)),
               Button(root, width=6, height=3, font=symbol_font, command=lambda: click(8))]
    for j in range(9):
        buttons[j].grid(row=j // 3 + 1, column=j % 3)


def click(button_ptr):
    """
    it's called when clicking the button
    it puts the sign into the button and makes it DISABLED
    at the end it calls status.check()
    :param button_ptr: number of button
    """
    global sign, ptr, buttons, board, last_ptr

    # char represents the current sign
    char = sign[ptr % 2]
    ptr += 1

    # put the sign into proper field either buttons or board
    buttons[button_ptr]['text'] = char
    if char == 'X':
        buttons[button_ptr]['disabledforeground'] = "#ff0000"
    else:
        buttons[button_ptr]['disabledforeground'] = "#0000ff"
    buttons[button_ptr]['state'] = DISABLED
    board.pop(button_ptr)
    board.insert(button_ptr, char)

    # check the position
    position = status.check(board)
    if position != "go":
        last_ptr += 1

        # make the buttons DISABLED
        for j in range(9):
            if board[j] == "":
                buttons[j]['state'] = DISABLED

        # edit the scoreboard
        if position == "draw":
            score['X'] += 0.5
            score['O'] += 0.5
            Label(root, text="There is a draw!", width=11, height=2, font=com_font).grid(row=0, column=1)
        else:
            score[position] += 1
            Label(root, text=position + " won this time!", width=11, height=2, font=com_font).grid(row=0, column=1)

        # display new scoreboard and "Play again!" button
        Label(root, text="X score: " + str(score['X']), width=11, height=2, font=com_font).grid(row=0, column=0)
        Label(root, text="O score: " + str(score['O']), width=11, height=2, font=com_font).grid(row=0, column=2)
        Button(root, text="Play again!", bd=4, command=lambda: new_game()).grid(row=4, column=1)


# start the game
new_game()

root.mainloop()
