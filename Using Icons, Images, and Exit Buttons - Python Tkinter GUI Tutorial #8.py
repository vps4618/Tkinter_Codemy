from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Vishwa Praveen')
root.iconbitmap('icon.ico')

my_img = ImageTk.PhotoImage(Image.open("icon.ico"))
my_label = Label(image =my_img)
my_label.pack()




exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack()




root.mainloop()
