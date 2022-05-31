from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry('270x150')

def enter():
    if username.get()=='vishwa' and password.get()=='30145':
        enter_window=Tk()
        enter_label=Label(enter_window,text='Successfully logged in !',font='Helvatica,16,Bold',fg='Blue').pack()
    else:
        messagebox.showerror('error',"yvuyvyvyvivviu")    
username_label = Label(root,text='username :')
username_label.grid(row=0,column=0,pady=10)

username = Entry(root,width=30)
username.grid(row=0,column=1)

password_label = Label(root,text='password :')
password_label.grid(row=2,column=0)

password = Entry(root,width=30,show='*')
password.grid(row=2,column=1)

button=Button(root,text='submit',command=enter)
button.grid(row=4,column=1,pady=10)

space=Label(root,text='').grid(row=1,column=0)
space1=Label(root,text='').grid(row=3,column=0)

root.mainloop()