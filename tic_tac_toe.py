from tkinter import *
import status

root = Tk()
root.title("TIC TAC TOE GAME")

sign = ['X', 'O']
last_ptr = 0
ptr = 0

board = [""] * 9
buttons = []


def new_game():
    global ptr, buttons, board, last_ptr
    ptr = last_ptr % 2
    board = [""] * 9
    Label(root, text="Good Luck!", width=16, height=2).grid(row=0, column=1)
    buttons = [Button(root, width=16, height=8, command=lambda: click(0)),
               Button(root, width=16, height=8, command=lambda: click(1)),
               Button(root, width=16, height=8, command=lambda: click(2)),
               Button(root, width=16, height=8, command=lambda: click(3)),
               Button(root, width=16, height=8, command=lambda: click(4)),
               Button(root, width=16, height=8, command=lambda: click(5)),
               Button(root, width=16, height=8, command=lambda: click(6)),
               Button(root, width=16, height=8, command=lambda: click(7)),
               Button(root, width=16, height=8, command=lambda: click(8))]
    for j in range(9):
        buttons[j].grid(row=j // 3 + 1, column=j % 3)


def click(button_ptr):
    global sign, ptr, buttons, board, last_ptr

    char = sign[ptr % 2]
    ptr += 1

    buttons.pop(button_ptr)
    buttons.insert(button_ptr, Button(root, width=16, height=8, text=char, state=DISABLED))

    board.pop(button_ptr)
    board.insert(button_ptr, char)

    for j in range(9):
        buttons[j].grid(row=j // 3 + 1, column=j % 3)

    position = status.check(board)
    if position != "go":
        last_ptr += 1

        for j in range(9):
            if board[j] == "":
                buttons.pop(j)
                buttons.insert(j, Button(root, width=16, height=8, state=DISABLED))
        for j in range(9):
            buttons[j].grid(row=j // 3 + 1, column=j % 3)

        if position == "draw":
            Label(root, text="There is a draw!", width=16, height=2).grid(row=0, column=1)
        else:
            Label(root, text=position + " won this time!", width=16, height=2).grid(row=0, column=1)
        Button(root, text="Play again!", bd=4, command=lambda: new_game()).grid(row=4, column=1)


new_game()

root.mainloop()
