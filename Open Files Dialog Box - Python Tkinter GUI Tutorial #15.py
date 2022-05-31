from os import close
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root=Tk()
root.title("new windows")
# root.attributes('-fullscreen',True)
root.iconbitmap("images/icon.ico")
global frame
frame = LabelFrame(root)

frame.grid(row=0,column=0,pady=20,padx=10)
global frame1
frame1 = LabelFrame(root)

frame1.grid(row=1,column=0,pady=10,padx=10)
def open():
    global filename1,new_image
    filename1=filedialog.askopenfilename(
    initialdir="C:/Users/vishwa praveen pc/Documents/tkinter_codemy/images",
    title="select a picture file",
    filetypes=(("all files","*.*"),("jpg files","*.jpg"),("png files","*.png"),("ico files","*.ico")))
    img= (Image.open(filename1))


    #Resize the Image using resize method
    resized_image= img.resize((width,height), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    filename=Label(frame,text=filename1).grid(row=4,column=0,padx=10,pady=5)
    
    label_img=Label(frame1,image=new_image).grid(row=0,column=0,padx=20,pady=10)

open_button=Button(frame,text="Browse images",command=open).grid(row=3,column=1,padx=10,pady=5)

e=Entry(frame, width=35, borderwidth=5)
e.grid(row=0,column=1,padx=50,pady=10)

f=Entry(frame, width=35, borderwidth=5)
f.grid(row=1,column=1,padx=50,pady=10)

def submit():
    global height,width
    height=int(f.get())
    width=int(e.get())
    


submit_button=Button(frame,text="submit",command=submit).grid(row=2,column=1,padx=10,pady=5)

elabel1=Label(frame,text="Enter width :").grid(row=0,column=0,padx=10,pady=10)
elabel2=Label(frame,text="Enter height :").grid(row=1,column=0,padx=10,pady=10)
close_button=Button(frame,text="close",command=root.destroy)
close_button.grid(row=3,column=2)
root.mainloop()