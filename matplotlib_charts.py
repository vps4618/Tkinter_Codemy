from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
import full_text_window_scrollbar
root = Tk()
root.title('Matplotlib charts')
root.iconbitmap('images/english.ico')
root.geometry("400x200")

def graph():
    house_prices=np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()
my_button = Button(root,text="Graph it!",command=graph)
my_button.pack()    
a=full_text_window_scrollbar.HTMLLabel(html='''<a href="https://vpsoftwares.herokuapp.com">My website</a>
                            <ul>
                                <li>vishwa</li>
                                <li>praveen</li>
                            </ul>    ''')
a.pack()
b=full_text_window_scrollbar.HTMLScrolledText(html="""<h1>hi</h1>
                                       <code>if x==0:
                                       print('hi')""",height=50)
b.pack()
root.mainloop()