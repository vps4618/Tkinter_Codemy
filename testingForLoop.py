from tkinter import *
root=Tk()
entries=[]
for i in range(0,20,2):
    entry=Entry(root)
    entry.grid(row=i,column=0)
    entries.append(entry)
for k in range(1,20,2):
    space=Label(root,text="")
    space.grid(row=k,column=0)
    print(k)
def submit():
    dataList=[]
    for entry in entries:
        data=entry.get()
        dataList.append(data)
    print(dataList)

submit=Button(root,text="submit",command=submit)
submit.grid(row=21,column=0)    
root.mainloop()