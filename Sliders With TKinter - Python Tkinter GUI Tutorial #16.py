from tkinter import *

root = Tk()
root.title('sliders')
root.iconbitmap("images/icon.ico")
root.geometry("400x400")
vertical = Scale(root, from_=0,to=400)
vertical.pack()

def slide():
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
horizontal = Scale(root, from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()
btn=Button(root, text="click to change geometry",command=slide)
btn.pack()


root.mainloop()