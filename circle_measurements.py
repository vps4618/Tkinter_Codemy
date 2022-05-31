from tkinter import *

root = Tk()
root.resizable(False,False)
root.geometry("700x620")
root.iconbitmap('images/icon1.ico')
root.title('Circle measurements')
class functions:

    def calculate(self):
        
        self.function1 = Label(root, text="Circumference", font="Helvetica 14 bold")
        self.function1.grid(row=10, column=1)
        self.equation1 = Label(root, text="=2⫪r * θ/360°", font="Helvetica 13 bold")
        self.equation1.grid(row=11, column=1)
        self.equation2 = Label(root, text=f"=2 * 22/7 * {input1.get()} * {input2.get()}/360°", font="Helvetica 13 bold")
        self.equation2.grid(row=12, column=1)
        self.equation3 = Label(root, text=f"={2 * (22 / 7) * float(input1.get()) * (float(input2.get()) / 360)}⫽",
                               font="Helvetica 13 bold")
        self.equation3.grid(row=13, column=1)
        self.spacing4 = Label(root, text="                ")
        self.spacing4.grid(row=14, column=0)

        self.function2 = Label(root, text="Area", font="Helvetica 14 bold")
        self.function2.grid(row=15, column=1)
        self.equation4 = Label(root, text="=⫪r^2 * θ/360°", font="Helvetica 13 bold")
        self.equation4.grid(row=16, column=1)
        self.equation5 = Label(root, text=f"=22/7 * {input1.get()}^2 * {input2.get()}/360°", font="Helvetica 13 bold")
        self.equation5.grid(row=17, column=1)
        self.equation6 = Label(root,
                               text=f"={(22 / 7) * float(input1.get()) * float(input1.get()) * (float(input2.get()) / 360)}⫽",
                               font="Helvetica 13 bold")
        self.equation6.grid(row=18, column=1)
        self.spacing5 = Label(root, text="                ")
        self.spacing5.grid(row=19, column=0)

        self.function3 = Label(root, text="Perimeter", font="Helvetica 14 bold")
        self.function3.grid(row=20, column=1)

        if input2.get() == "360":
            self.equation7 = Label(root, text="=2⫪r * θ/360°", font="Helvetica 13 bold")
            self.equation7.grid(row=21, column=1)
            self.equation8 = Label(root, text=f"=2 * 22/7 * {input1.get()} * {input2.get()}/360°",
                                   font="Helvetica 13 bold")
            self.equation8.grid(row=22, column=1)
            self.equation9 = Label(root, text=f"={2 * (22 / 7) * float(input1.get()) * (float(input2.get()) / 360)}⫽",
                                   font="Helvetica 13 bold")
            self.equation9.grid(row=23, column=1)
        else:
            self.equation7 = Label(root, text="=2⫪r * θ/360° + 2r", font="Helvetica 13 bold")
            self.equation7.grid(row=21, column=1)
            self.equation8 = Label(root,
                                   text=f"=2 * 22/7 * {input1.get()} * {input2.get()}/360° + 2 * {input1.get()}",
                                   font="Helvetica 13 bold")
            self.equation8.grid(row=22, column=1)
            self.equation9 = Label(root,
                                   text=f"={(2 * (22 / 7) * float(input1.get()) * (float(input2.get()) / 360)) + 2 * float(input1.get())}⫽",
                                   font="Helvetica 13 bold")
            self.equation9.grid(row=23, column=1)

        self.spacing6 = Label(root, text="                ")
        self.spacing6.grid(row=24, column=0)

    def delete(self):
        self.function1.destroy()

        self.equation1.destroy()

        self.equation2.destroy()

        self.equation3.destroy()
        self.spacing4.destroy()

        self.function2.destroy()
        self.equation4.destroy()
        self.equation5.destroy()
        self.equation6.destroy()
        self.spacing5.destroy()

        self.function3.destroy()

        self.equation7.destroy()
        self.equation8.destroy()
        self.equation9.destroy()
        self.spacing6.destroy()



obj = functions()
spacing = Label(root, text="              ")
spacing.grid(row=0, column=0)
Heading = Label(root, text="Finding circumference,area and perimeter of a circle", font="Helvetica 16 bold italic",
                fg="#9e649e", bg="#c5cff0")
Heading.grid(row=0, column=1)
spacing1 = Label(root, text="                  ")
spacing1.grid(row=1, column=0)
input1 = Entry(root, width=50, bg="white", fg="black", borderwidth=2, font="Helvetica 12 bold")
input1.grid(row=2, column=1)
input1.insert(2, "Enter the radius :-")
spacing2 = Label(root, text="             ")
spacing2.grid(row=2, column=2)
spacing3 = Label(root, text="                ")
spacing3.grid(row=3, column=0)
input2 = Entry(root, width=50, bg="white", fg="black", borderwidth=2, font="Helvetica 12 bold")
input2.grid(row=4, column=1)
input2.insert(2, "Enter the angle :-")
spacing4 = Label(root, text="                ")
spacing4.grid(row=5, column=0)
button = Button(root, text="submit", bg="light blue", command=obj.calculate, font="Helvetica 11 bold", fg="#2e2375")
button.grid(row=6, column=1)
spacing10 = Label(root, text="")
spacing10.grid(row=7, column=1)
button1 = Button(root, text="clear", bg="#e3aab3", command=obj.delete, font="Helvetica 11 bold", fg="#522375")
button1.grid(row=8, column=1)
spacing11 = Label(root, text="")
spacing11.grid(row=9, column=1)

root.mainloop()
