from tkinter import *
root = Tk()
string = 'Question #'
nums = ['1', '2', '3']
labels=[] #creates an empty list for your labels
c = 10
for x in nums: #iterates over your nums
    jk = string + x
    label = Label(root,text=jk)
    label.place(x=c+10, y=c+10) #set your text
    labels.append(label) #appends the label to the list for further use

for x, l in zip(nums,labels): #change your for loops to this
    jk = string + x
    l.config(text=jk)

root.mainloop()