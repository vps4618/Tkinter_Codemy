from tkinter import *
import tkinter
from PIL import ImageTk,Image


ws = Tk()
ws.title('English to English Dictionary')
ws.geometry('680x840')
ws.resizable(False,False)
ws.iconbitmap('images/world.ico')
text="""
hi
"""


def get():
    text_box.insert(END,"""
    s




    sss
    ss

    sssss












    ssss































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    fuck
    
    """)

        
    
  


text_box = Text(
ws,
height=10,
width=10,
wrap='word',
fg="black",

font=("helvatica",13)

)


text_box.pack()
button=Button(ws,text="submit",command=lambda:get(),font=("helvatica",10))
button.pack()

ws.mainloop()