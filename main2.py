from glob import glob
from tkinter import *
import time

from matplotlib.pyplot import text
from gridsfile import a, noneditedBoarda, b, noneditedBoardb
import numpy as np

root = Tk()
root.config(bg='white')
root.minsize(540, 590)
root.maxsize(540, 590)
root.title("Sudoku")

canvas = Canvas(root, width=540, height=540, bg='white')
canvas.pack(side=BOTTOM)
notsolvableLabel = Label(root, text=' ', bg='white')
notsolvableLabel.place(x=200, y=10)

labels = []
delay = 1
c = 0

def printcell(x, y): # given coordinates return index to acces labels
    return int(x*9 + y)

def resetboard():  # reset whole board
    global c, a, b
    c += 1
    if c % 2 == 0:
        board = noneditedBoarda
    else:
        board = noneditedBoardb

    notsolvableLabel.config(text=' ')

    for i in range(9):
        for j in range(9):
            if board[i][j] != -1:
                labels[printcell(i, j)].config(text=board[i][j], font='Arial 18 bold')
            if board[i][j] == -1:
                            labels[printcell(i, j)].config(text=' ')

    a = np.array(noneditedBoarda)
    b = np.array(noneditedBoardb)

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

def paintsquare(x, y, color):
    global canvas
    canvas.create_rectangle(x*60, y*60, (x*60)+60, (y*60)+60, fill=color)
    tx = labels[printcell(x, y)].cget('text')
    print(tx)
    labels[printcell(x, y)].config(text=tx)
    canvas.update_idletasks()
    time.sleep(delay)

def solvesudoku(grid, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        col = 0
        row += 1
    
    if grid[row][col] != -1:
        return solvesudoku(grid, row, col+1)
    
    paintsquare(row, col, 'red')

    for i in range(1, 10):
        if is_valid(grid, row, col, i):
            grid[row][col] = i

            paintsquare(row, col, 'white')
            labels[printcell(row, col)].config(text=i, bg='white')  
            canvas.update_idletasks()
            time.sleep(delay)

            if solvesudoku(grid, row, col+1):
                return True

        grid[row][col] = -1

        paintsquare(row, col, 'white')


    return False

def solvedef():
    global c
    if c % 2 == 0:
        bo = a
    else:
        bo = b
    
    if (not solvesudoku(bo, 0, 0)):
        notsolvableLabel.config(text='NOT SOLVABLE')

for i in range(9):  # create all labels for each cell
    for j in range(9):
        l = Label(canvas, text=' ', font=('arial', 16), bg='white')
        l.place(x=j*60+20, y=i*60+15)
        labels.append(l)

resetboard()

#graphics
resetb = Button(root, text='RESET',  bg='white', command=lambda:resetboard())
resetb.place(x=20, y=10)

solveb = Button(root, text='SOLVE',  bg='white', command=lambda:solvedef())
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