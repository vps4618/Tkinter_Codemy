from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Vishwa Praveen')
root.iconbitmap('images/icon.ico')
frame1 = LabelFrame(root, text="This is my first frame..............", padx=100, pady=100)
frame1.grid(row=0, column=0, padx=20, pady=10)
b = Button(frame1, text="click")
b.pack()
frame2 = LabelFrame(root, text="This is my second frame", padx=150, pady=100)
frame2.grid(row=0, column=1, padx=100, pady=20)
b2 = Button(frame2, text="click me")
b2.grid(row=0, column=0)
b3 = Button(frame2, text="click me")
b3.grid(row=0, column=1)
b4 = Button(frame2, text="click me")
b4.grid(row=0, column=2)
root.mainloop()
