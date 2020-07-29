from tkinter import *

root = Tk()
root.title("TIC TAC TOE GAME")

sign = ['X', 'O']
ptr = 0

sings = [""]*9


def check(board):
    for j in range(3):
        if board[3 * j] == board[3 * j + 1] == board[3 * j + 2] and board[3 * j] != "":
            return board[3 * j]
        if board[j] == board[j + 3] == board[j + 6] and board[j] != "":
            return board[j]
    if board[0] == board[4] == board[8] and board[4] != "":
        return board[4]
    if board[2] == board[4] == board[6] and board[4] != "":
        return board[4]
    if "" not in board:
        return "draw"
    return "go"


def click(button_ptr):
    global sign, ptr, buttons, sings

    char = sign[ptr % 2]
    ptr += 1

    buttons.pop(button_ptr)
    buttons.insert(button_ptr, Button(root, width=20, height=10, text=char, state=DISABLED))

    sings.pop(button_ptr)
    sings.insert(button_ptr, char)

    for j in range(9):
        buttons[j].grid(row=j // 3, column=j % 3)

    position = check(sings)
    if position != "go":
        if position == "draw":
            Label(root, text="There is a draw!", width=15, height=5).grid(row=3, column=1)
        else:
            Label(root, text=position+" won this time!", width=15, height=5).grid(row=3, column=1)


buttons = [Button(root, width=20, height=10, command=lambda: click(0)),
           Button(root, width=20, height=10, command=lambda: click(1)),
           Button(root, width=20, height=10, command=lambda: click(2)),
           Button(root, width=20, height=10, command=lambda: click(3)),
           Button(root, width=20, height=10, command=lambda: click(4)),
           Button(root, width=20, height=10, command=lambda: click(5)),
           Button(root, width=20, height=10, command=lambda: click(6)),
           Button(root, width=20, height=10, command=lambda: click(7)),
           Button(root, width=20, height=10, command=lambda: click(8))]

for i in range(9):
    buttons[i].grid(row=i // 3, column=i % 3)

root.mainloop()
