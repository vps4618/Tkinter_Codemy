from tkinter import *

root = Tk()


def myName():
    myLabel = Label(root, text="Hi my name is Vishwa Praveen Sarathchandra.")
    myLabel.grid(row=1, column=0)


myButton = Button(root, text="Click me!", command=myName, fg="blue")
myButton.grid(row=2, column=1)
root.mainloop()
