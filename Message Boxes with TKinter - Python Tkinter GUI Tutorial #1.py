from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('message boxs')
root.iconbitmap('images/icon.ico')


def popup():
    response = messagebox.showinfo("Showing an information", "My name is Vishwa Praveen Sarathchandra.")
    label = Label(root, text=response).grid(row=3, column=0)


def popup1():
    response1 = messagebox.showerror("Showing an error message", "You clicked wrong button !!!!!!")


def popup2():
    response2 = messagebox.showwarning("Showing a warning", "You should respect your elders")


def popup3():
    response3 = messagebox.askquestion("Asking a question", "Do you like this?")

    if response3 == "yes":
        label3 = Label(root, text="You clicked yes").grid(row=3, column=0)
    else:
        label3 = Label(root, text="You clicked no").grid(row=3, column=0)


def popup4():
    response4 = messagebox.askokcancel("Asking for cancelling something", "Please cancel this message box")


def popup5():
    response5 = messagebox.askyesno("Asking yes no question", "Do you have a computer?")


def popup6():
    response6 = messagebox.askretrycancel("Asking for retrying and cancelling", "Please retry!")


def popup7():
    response7 = messagebox.askyesnocancel("Asking yes no cancel", "Do you like to click this?")


button1 = Button(root, text="Popup show info", command=popup).grid(row=0, column=0, padx=5, pady=10)
button2 = Button(root, text="Popup show error", command=popup1).grid(row=0, column=1, padx=5, pady=10)
button3 = Button(root, text="Popup show warning", command=popup2).grid(row=0, column=2, padx=5, pady=10)
button4 = Button(root, text="Popup ask question", command=popup3).grid(row=1, column=0, padx=5, pady=10)
button5 = Button(root, text="Popup ask cancel", command=popup4).grid(row=1, column=1, padx=5, pady=10)
button6 = Button(root, text="Popup ask yes no", command=popup5).grid(row=1, column=2, padx=5, pady=10)
button7 = Button(root, text="Popup ask retry cancel", command=popup6).grid(row=2, column=0, padx=5, pady=10)
button8 = Button(root, text="Popup ask yes no cancel", command=popup7).grid(row=2, column=1, padx=5, pady=10,
                                                                            columnspan=2)

root.mainloop()
