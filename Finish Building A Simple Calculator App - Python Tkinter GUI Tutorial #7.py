from tkinter import *
import time

root = Tk()
root.title("Mini calculator (VP)")
root.geometry("450x520")

e = Entry(root, width=35, borderwidth=5, bg="#aae0e6", fg="#58579e", font="Helvetica 16 bold")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear1():
    e.delete(0, END)


def button_add1():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal1():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, float(f_num) + float(second_number))
    elif math == "subtraction":
        e.insert(0, float(f_num) - float(second_number))
    elif math == "multiplication":
        e.insert(0, float(f_num) * float(second_number))
    elif math == "division":
        e.insert(0, float(f_num) / float(second_number))
    else:
        time.sleep(0.0001)


def button_subtract1():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide1():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply1():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


#  define buttons

button_1 = Button(root, text="1", padx=60, pady=20, command=lambda: button_add(1), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_2 = Button(root, text="2", padx=60, pady=20, command=lambda: button_add(2), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_3 = Button(root, text="3", padx=60, pady=20, command=lambda: button_add(3), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_4 = Button(root, text="4", padx=60, pady=20, command=lambda: button_add(4), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_5 = Button(root, text="5", padx=60, pady=20, command=lambda: button_add(5), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_6 = Button(root, text="6", padx=60, pady=20, command=lambda: button_add(6), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_7 = Button(root, text="7", padx=60, pady=20, command=lambda: button_add(7), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_8 = Button(root, text="8", padx=60, pady=20, command=lambda: button_add(8), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_9 = Button(root, text="9", padx=60, pady=20, command=lambda: button_add(9), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_0 = Button(root, text="0", padx=60, pady=20, command=lambda: button_add(0), bg="#a2baeb",
                  font="Helvetica 14 bold")
button_add2 = Button(root, text="+", padx=59, pady=20, command=button_add1, bg="#c3aae6", font="Helvetica 14 bold")
button_equal = Button(root, text="=", padx=138, pady=20, command=button_equal1, bg="#c3aae6", font="Helvetica 14 bold")
button_clear = Button(root, text="Clear", padx=118, pady=20, command=lambda: button_clear1(), bg="#eba2db",
                      font="Helvetica 14 bold")

button_multiply = Button(root, text="*", padx=64, pady=20, command=button_multiply1, bg="#c3aae6",
                         font="Helvetica 14 bold")
button_subtract = Button(root, text="-", padx=60, pady=20, command=button_subtract1, bg="#c3aae6",
                         font="Helvetica 14 bold")
button_divide = Button(root, text="/", padx=65, pady=20, command=button_divide1, bg="#c3aae6", font="Helvetica 14 bold")

# put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add2.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
