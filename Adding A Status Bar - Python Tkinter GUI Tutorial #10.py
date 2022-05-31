from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.configure(bg="black")
root.title("Image Viewer (countries)")
root.iconbitmap('images/icon.ico')
root.geometry("618x700")
root.resizable(False, False)

my_img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/7.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("images/8.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("images/9.jpg"))
my_img10 = ImageTk.PhotoImage(Image.open("images/10.jpg"))
my_img11 = ImageTk.PhotoImage(Image.open("images/11.jpg"))
my_img12 = ImageTk.PhotoImage(Image.open("images/12.jpg"))
my_img13 = ImageTk.PhotoImage(Image.open("images/13.jpg"))
my_img14 = ImageTk.PhotoImage(Image.open("images/14.jpg"))
my_img15 = ImageTk.PhotoImage(Image.open("images/15.jpg"))
my_img16 = ImageTk.PhotoImage(Image.open("images/16.jpg"))
my_img17 = ImageTk.PhotoImage(Image.open("images/17.jpg"))
my_img18 = ImageTk.PhotoImage(Image.open("images/18.jpg"))
my_img19 = ImageTk.PhotoImage(Image.open("images/19.jpg"))
my_img20 = ImageTk.PhotoImage(Image.open("images/20.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11,
              my_img12, my_img13, my_img14, my_img15, my_img16, my_img17, my_img18, my_img19, my_img20]
spacing1 = Label(root, text="   ", bg="black")
spacing1.grid(row=0, column=1)

heading = Label(root, text="Image Viewer", bg="#d7d3f5", font="times 20 bold", fg="#4c3996")
heading.grid(row=1, column=2)

spacing2 = Label(root, text="   ", bg="black")
spacing2.grid(row=2, column=1)

my_label = Label(image=my_img1)
my_label.grid(row=3, column=1, columnspan=3)

spacing3 = Label(root, text="   ", bg="black")
spacing3.grid(row=4, column=1)

spacing4 = Label(root, text="   ", bg="black")
spacing4.grid(row=6, column=1)

china = "China"
japan = "Japan"
korea = "Korea"
thailand = "Thailand"
greece = "Greece"
new_zealand = "New zealand"
chile = "Chile"
italy = "Italy"
vietnam = "Vietnam"
switzerland = "Switzerland"
ireland = "Ireland"
slovenia = "Slovenia"
south_africa = "South Africa"
canada = "Canada"
sweden = "Sweden"
indonesia = "Indonesia"
wales = "Wales"
iceland = "Iceland"
romania = "Romania"
the_netherlands = "The Netherlands"
name_of_the_image = Label(root, text=china, bg="#faa2d0", fg="black", font="times 16 bold")
name_of_the_image.grid(row=5, column=2)
namelist = [china, japan, korea, thailand, greece, new_zealand, chile, italy, vietnam, switzerland, ireland, slovenia,
            south_africa, canada, sweden
    , indonesia, wales, iceland, romania, the_netherlands]


def forward(image_number):
    global button_back
    global button_forward
    global my_label
    global name_of_the_image
    my_label.grid_forget()
    name_of_the_image.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    name_of_the_image = Label(root, text=namelist[image_number - 1], bg="#faa2d0", fg="black", font="times 16 bold")
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1), font="helvatica 14 bold",
                            width=5,
                            bg="#5ca2f2", fg="black")
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1), font="helvatica 14 bold", width=5,
                         bg="#5ca2f2", fg="black")
    if image_number == 20:
        button_forward = Button(root, text=">>", state=DISABLED, font="helvatica 14 bold", width=5, bg="#5ca2f2",
                                fg="black")
    button_back.grid(row=5, column=1)
    button_forward.grid(row=5, column=3)
    name_of_the_image.grid(row=5, column=2)
    my_label.grid(row=3, column=1, columnspan=3)

    # update the status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E,bg="#62a3a0",fg="#472669",font="helvatica 12 bold")
    status.grid(row=7, column=1, columnspan=5, sticky=W + E)


def back(image_number):
    global button_back
    global button_forward
    global my_label
    global name_of_the_image
    my_label.grid_forget()
    name_of_the_image.grid_forget()
    name_of_the_image = Label(root, text=namelist[image_number - 1], bg="#faa2d0", fg="black", font="times 16 bold")
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1), font="helvatica 14 bold",
                            width=5,
                            bg="#5ca2f2", fg="black")
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1), font="helvatica 14 bold", width=5,
                         bg="#5ca2f2", fg="black")
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED, font="helvatica 14 bold", width=5, bg="#5ca2f2",
                             fg="black")

    button_back.grid(row=5, column=1)
    button_forward.grid(row=5, column=3)
    name_of_the_image.grid(row=5, column=2)

    my_label.grid(row=3, column=1, columnspan=3)

    # update the status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E,bg="#62a3a0",fg="#472669",font="helvatica 12 bold")
    status.grid(row=7, column=1, columnspan=5, sticky=W + E)


spacing10 = Label(root, text="        ", bg="black")
spacing10.grid(row=6, column=0)

button_back = Button(root, text="<<", command=back, state=DISABLED, bg="#5ca2f2", fg="black", font="helvatica 14 bold",
                     width=5)
button_forward = Button(root, text=">>", command=lambda: forward(2), bg="#5ca2f2", fg="black", font="helvatica 14 bold",
                        width=5)

button_back.grid(row=5, column=1)
button_forward.grid(row=5, column=3)

name = Label(root, text="< Coded by VP >", bg="black", fg="white", font="times 6 bold")
name.grid(row=0, column=0)

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E,bg="#62a3a0",fg="#472669",font="helvatica 12 bold")
status.grid(row=7, column=1, columnspan=5, sticky=W + E)

root.mainloop()
