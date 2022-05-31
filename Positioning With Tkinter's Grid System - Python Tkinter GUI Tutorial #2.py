# method 1
# from tkinter import *
#
# root = Tk()
#
# myLabel1 = Label(root, text="HELLO WORLD")
# myLabel2 = Label(root, text="My name id Vishwa ")
# myLabel1.grid(row=0,column=1)
# myLabel2.grid(row=0,column=2)
# root.mainloop()


# method 2
from tkinter import *

root = Tk()

myLabel1 = Label(root, text="HELLO WORLD").grid(row=0, column=1)
myLabel2 = Label(root, text="My name id Vishwa ").grid(row=0, column=2)
root.mainloop()
