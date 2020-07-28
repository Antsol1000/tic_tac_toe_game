from tkinter import *

root = Tk()
root.title("TIC TAC TOE GAME")

sign = ['X', 'O']
ptr = 0

buttons = []
sings = [""]*9


def check(board):
    for i in range(3):
        if board[3*i] == board[3*i+1] == board[3*i+2] and board[i] != "":
            return board[i]
        if board[i] == board[i+3] == board[i+6] and board[i] != "":
            return board[i]
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
    buttons.insert(button_ptr, Button(root, padx=50, pady=50, text=char))
    sings.pop(button_ptr)
    sings.insert(button_ptr, char)
    for i in range(9):
        buttons[i].grid(row=i // 3, column=i % 3)
    position = check(sings)
    if position != "go":
        if position == "draw":
            Label(root, text="There is a draw this time!", padx=50, pady=50).grid(row=3,column=1)
        else:
            Label(root, text=position+" won this time!", padx=50, pady=50).grid(row=3, column=1)


buttons = [Button(root, padx=50, pady=50, command=lambda: click(0)),
           Button(root, padx=50, pady=50, command=lambda: click(1)),
           Button(root, padx=50, pady=50, command=lambda: click(2)),
           Button(root, padx=50, pady=50, command=lambda: click(3)),
           Button(root, padx=50, pady=50, command=lambda: click(4)),
           Button(root, padx=50, pady=50, command=lambda: click(5)),
           Button(root, padx=50, pady=50, command=lambda: click(6)),
           Button(root, padx=50, pady=50, command=lambda: click(7)),
           Button(root, padx=50, pady=50, command=lambda: click(8))]

for i in range(9):
    buttons[i].grid(row=i // 3, column=i % 3)

root.mainloop()
