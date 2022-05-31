
# Python program to create a table
  
from tkinter import *
 
 
class Table:
     
    def __init__(self,root):
 
      
  
        frame = Frame(root)
        sb = Scrollbar(frame,orient=HORIZONTAL)
        sb.pack(side=BOTTOM, fill='x')

        sb1 = Scrollbar(frame)
        sb1.pack(side=RIGHT, fill='y')
        text_box = Text(
            frame,
            height=26,
            width=60,
            wrap=NONE,
            yscrollcommand=sb1.set,
            xscrollcommand=sb.set
        )
        
        text_box.pack(expand = 0, fill = BOTH)






        sb.config(command=text_box.xview)
        sb1.config(command=text_box.yview)

        frame.grid(row=2, column=1)
        

        
        for i in range(total_rows):
            button = Button(text_box,text='x')
            text_box.window_create(END, window=button)
            for x in range(total_columns):
                self.e = Entry(text_box, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                
                self.e.insert(END, lst[i][x])
                self.e.config(state='disabled')
                
                text_box.window_create(END, window=self.e)
                
            text_box.insert(END,'\n')
       
# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21),
       (6,'Shubham','Delhi',21),
       (7,'Shubham','Delhi',21),
       (8,'Shubham','Delhi',21),
       (9,'Shubham','Delhi',21),
       (10,'Shubham','Delhi',21),
       (11,'Shubham','Delhi',21),
       (11,'Shubham','Delhi',21),
       (12,'Shubham','Delhi',21),
       (13,'Shubham','Delhi',21),
       (14,'Shubham','Delhi',21),
       (15,'Shubham','Delhi',21),
       (16,'Shubham','Delhi',21),
       (17,'Shubham','Delhi',21),
       (18,'Shubham','Delhi',21),
       (19,'Shubham','Delhi',21)]
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = Tk()
t = Table(root)
root.mainloop()
