from tkinter import *

root = Tk()
e = Entry(root, width=50, bg="grey", fg="white", borderwidth=5)
e.grid(row=0, column=0)
e.get()
e.insert(2, "Enter your name :")


def myName():
    myLabel = Label(root, text=f"Answer is {2 * float(e.get())}")
    myLabel.grid(row=1, column=0)


myButton = Button(root, text="Enter your name", command=myName, fg="blue", bg="light blue")
myButton.grid(row=2, column=0)
root.mainloop()
