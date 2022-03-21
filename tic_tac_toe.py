from tkinter import *
import tkinter.font as font
from game import *
from alpha_beta import alpha_beta

root = Tk()
root.title("TIC TAC TOE GAME")
root.iconbitmap("./icon.ico")

sign = ['X', 'O']
score = {'X': 0, 'O': 0}

# last_ptr contains who start last game
last_ptr = 0
# ptr point who has the move
ptr = 0

# board is list which represents the state of buttons
board = initial_state()
buttons = []

symbol_font = font.Font(size=20, weight='bold')
com_font = font.Font(size=11)

bot = False


def change_bot():
    global bot
    bot = not bot
    if bot and sign[ptr % 2] == 'O':
        click(alpha_beta('O', board))


again_button = Button(root, text="Play Again!", bd=4, state=DISABLED, command=lambda: new_game())
again_button.grid(row=4, column=0)
exit_button = Button(root, text="Exit", bd=4, command=lambda: root.destroy())
exit_button.grid(row=4, column=2)
bot_button = Button(root, text="AI", bd=4, command=lambda: change_bot())
bot_button.grid(row=4, column=1)


def show_scoreboard():
    Label(root, text=f"X score: {score['X']}", width=11, height=2, font=com_font).grid(row=0, column=0)
    Label(root, text=f"O score: {score['O']}", width=11, height=2, font=com_font).grid(row=0, column=2)


def new_game():
    global ptr, buttons, board, last_ptr, again_button
    # made again_button disabled to click
    # only able to reset after game
    again_button['state'] = DISABLED
    ptr = last_ptr % 2
    board = [""] * 9

    # display first row with scoreboard and initial statement
    Label(root, text="Good Luck!", width=11, height=2, font=com_font).grid(row=0, column=1)
    show_scoreboard()

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

    if bot and sign[ptr % 2] == 'O':
        click(alpha_beta(sign[ptr % 2], board))


def click(button_ptr):
    global sign, ptr, buttons, board, last_ptr, again_button

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
    if is_terminal(board):
        # end of the game making again_button active
        again_button['state'] = NORMAL
        last_ptr += 1

        # make the buttons DISABLED
        for j in range(9):
            if board[j] == "":
                buttons[j]['state'] = DISABLED

        # edit the scoreboard
        winner = who_won(board)
        if winner == '':
            score['X'] += 0.5
            score['O'] += 0.5
            Label(root, text="There is a draw!", width=11, height=2, font=com_font).grid(row=0, column=1)
        else:
            score[winner] += 1
            Label(root, text=f"{winner} won this time!", width=11, height=2, font=com_font).grid(row=0, column=1)

        # display new scoreboard
        show_scoreboard()

    elif bot and sign[ptr % 2] == 'O':
        click(alpha_beta(sign[ptr % 2], board))


if __name__ == '__main__':
    # start the game
    new_game()
    root.mainloop()
