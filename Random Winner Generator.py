from tkinter import *
from random import randint

root=Tk()
root.title('Random Winner Generator')
root.iconbitmap('images/encrypt.ico')
root.geometry('400x400')



def pick():
    # 21 entries
    entries = ['Vishwa','Mandipa','Navitha','Supun','Yasitha','Miyuru','Chanithu','Sachin','Uthsala','Amayuru','Dulaj','Sithil','Yumeth','Sahan','Anupama','Dimuthu','Tharuka','Vihanga','Janidu','Hashen','Vishwa']
    
    # convert list to set (to remove duplicate values)
    entries_set=set(entries)
    
    # convert back to list - 20
    unique_entries=list(entries_set)

    # create our list size variable
    our_number = len(unique_entries)-1

    # create a random number between 0 and 19
    rando = randint(0,our_number)

    winnnerLabel=Label(root,text=unique_entries[rando],font=('Helvatica',18))
    winnnerLabel.pack(pady=50)

topLabel=Label(root,text='Win-O-Rama!',font=('Helvatica', 24))
topLabel.pack(pady=20)

winButton=Button(root,text='PICK OUR WINNERS!!',font=('Helvatica',24),command=pick)
winButton.pack(pady=20)

root.mainloop()