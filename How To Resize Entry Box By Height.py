from tkinter import *

root =Tk()
root.title('How to resize entry box by height')
root.iconbitmap('images/encrypt.ico')
root.geometry('400x400')

def myClick():
    hello ="Hello "+e.get()
    myLabel=Label(root,text=hello)
    e.delete(0,'end')
    myLabel.pack(pady=10)

e = Entry(root,width=50,font=('Helvatica',24))
e.pack(padx=10,pady=10)

button= Button(root,text='Enter your name',command=myClick)
button.pack(pady=10)

root.mainloop()