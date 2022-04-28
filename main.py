from cProfile import label
from tkinter import *
from grid import a
import time

root = Tk()
root.config(bg='white')
root.minsize(540, 590)
root.maxsize(540, 590)
root.title("Sudoku")

canvas = Canvas(root, width=540, height=540, bg='white')
canvas.pack(side=BOTTOM)

variables = {}

def printnum(row, col, num, color):
    variables['sv'+str(row)+str(col)].set(num)

def printBoard():
    for i in range(9):
        for j in range(9):
            if (a[i][j] != -1):
                printnum(j, i, a[i][j], "black")                
            else:
                printnum(j, i, "", "black")

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
            printnum(row, col, "h", 'red')

            if solvesudoku(grid, row, col+1):
                return True

        grid[row][col] = -1
    return False

def solvedef():
    if (solvesudoku(a, 0, 0)):
        printBoard()

for i in range(9):
    for j in range(9):
        variables['l'+str(i)+str(j)] = 'l'+str(i)+str(j)
        variables['sv'+str(i)+str(j)] = StringVar()
        variables['l'+str(i)+str(j)] = Label(canvas, textvariable=variables['sv'+str(i)+str(j)], bg="white", font=('arial', 16)).place(x=i*60+20, y=j*60+15)

printBoard()

#graphics
resetb = Button(root, text='RESET',  bg='white', command=printBoard)
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