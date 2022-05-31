from tkinter import *
root = Tk()
root.title("drop down boxes")
root.iconbitmap("images/icon.ico")
root.geometry("400x400")

list =[
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"


]

def show():
    label = Label(root, text=clicked.get())
    label.pack()
# drop down boxes 
clicked=StringVar()
clicked.set(list[1])


drop = OptionMenu(root,clicked,*list)
drop.pack()

btn= Button(root,text="Show Selection",command=show)
btn.pack()

root.mainloop()











