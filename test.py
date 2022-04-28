from tkinter import *

root = Tk()

root.geometry("300x300")

v = StringVar()

label = Label(root, textvariable=v).pack()

v.set('holka')


root.mainloop()