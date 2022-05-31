from tkinter import *

root=Tk()
root.title("check boxs")
root.iconbitmap("images/icon.ico")
root.geometry("400x400")
def update():
    label=Label(root,text=var.get())
    label.pack()

var = StringVar()

check = Checkbutton(root, text="check",variable=var,onvalue="vishwa",offvalue="praveen")
check.deselect()
check.pack()


btn=Button(root, text="Show selection", command=update)
btn.pack()

root.mainloop()