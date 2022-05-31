from tkinter import *
from PIL import ImageTk,Image
def destroy1():
    top1.destroy()
global root
root=Tk()
root.title("new windows")
root.iconbitmap("images/icon.ico")
def open():

    
    # we need to make image variable as global to show it up on the second window
    global img
    global top1
    top1 = Toplevel()
    top1.title('My second window')
    top1.iconbitmap('images/icon.ico')
    label=Label(top1,text="Hello world!")
    label.grid(row=0,column=1)
    img= ImageTk.PhotoImage(Image.open("images/icon.ico"))
    label1=Label(top1,image=img)
    label1.grid(row=1,column=1)
    btn=Button(top1,text="Close",command=destroy1)
    btn.grid(row=2,column=1)
    
def open1():


   # we need to make image variable as global to show it up on the second window
    global img
    top = Toplevel()
    top.title('My third window')
    top.iconbitmap('images/4.jpg')
    label=Label(top,text="Hi guys!")
    label.grid(row=0,column=1)
    img= ImageTk.PhotoImage(Image.open("images/4.jpg"))
    label1=Label(top,image=img)
    label1.grid(row=1,column=1)


btn = Button(root,text="second window",command=open).pack(padx=5,pady=5)
btn1 = Button(root,text="third window",command=open1).pack(padx=5,pady=5)
root.mainloop()
