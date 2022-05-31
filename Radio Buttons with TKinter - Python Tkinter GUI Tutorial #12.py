from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Buttons')
root.iconbitmap('images/icon.ico')
# r = IntVar()
# r.set("3")
MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    number = Label(root, text=value)
    number.pack()


# Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda :clicked(r.get())).pack()
# Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda :clicked(r.get())).pack()
# Radiobutton(root, text="Option 3", variable=r, value=3, command=lambda: clicked(r.get())).pack()

# number = Label(root, text=pizza.get())
# number.pack()

b = Button(root, text="click", command=lambda: clicked(pizza.get()))
b.pack()
root.mainloop()
