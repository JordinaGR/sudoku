from cProfile import label
from tkinter import *
from grid import a, noneditedBoarda, b, noneditedBoardb
import time

root = Tk()
root.config(bg='white')
root.minsize(540, 590)
root.maxsize(540, 590)
root.title("Sudoku")

canvas = Canvas(root, width=540, height=540, bg='white')
canvas.pack(side=BOTTOM)

labels = []
c = 0

def printBoard(arr):
    array = []
    for i in range(9):
        for j in range(9):
            array.append(arr[i][j])

    for x, l in zip(array, labels):
        if x != -1:
            l.config(text=str(x))
        else:
            l.config(text=' ')

def resetfunc():
    global c
    c += 1
    if (c % 2 == 0):
        printBoard(noneditedBoarda)
    else:
        printBoard(noneditedBoardb)

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num:
            return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solvesudoku(grid, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        col = 0
        row += 1

    if grid[row][col] != -1:
        return solvesudoku(grid, row, col+1)
    
    for i in range(1, 10):
        if is_valid(grid, row, col, i):
            grid[row][col] = i

            if solvesudoku(grid, row, col+1):
                return True

        grid[row][col] = -1
    return False

def solvedef():
    global c
    bo = b
    if c % 2 == 0:
        bo = a

    if (solvesudoku(bo, 0, 0)):
        printBoard(bo)

for i in range(9):
    for j in range(9):
        l = Label(canvas, text=' ', font=('arial', 16), bg='white')
        l.place(x=j*60+20, y=i*60+15)
        labels.append(l)

printBoard(a)

#graphics
resetb = Button(root, text='RESET',  bg='white', command=resetfunc)
resetb.place(x=20, y=10)

solveb = Button(root, text='SOLVE',  bg='white', command=solvedef)
solveb.place(x=100, y=10)

canvas.create_line(0, 1, 540, 1, width=1)
for i in range(10):
    if i == 3 or i == 6:
        canvas.create_line(0, i*60, 540, i*60, width=1.9)
    else:
        canvas.create_line(0, i*60, 540, i*60, width=1)

canvas.create_line(0, 0, 0, 540, width=1)
for i in range(10):
    if i == 3 or i == 6:
        canvas.create_line(i*60, 0, i*60, 540, width=1.9)
    else:
        canvas.create_line(i*60, 0, i*60, 540, width=1)

root.mainloop()