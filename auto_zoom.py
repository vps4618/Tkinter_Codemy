from os import link
from tkinter import *
from tkinter import messagebox
import pyautogui
pyautogui.FAILSAFE=False

global root
root = Tk()
root.iconbitmap('images/zoom.ico')
root.title('auto_zoom_meeting')
root.geometry("300x240")
root.resizable(False,False)
def goZoomWithLink():
    if linkBox.get() !="" :
        linkInput=linkBox.get()  
        link.destroy()
        import webbrowser
        webbrowser.open(linkInput)
            # press ok button after first meeting ended
        while True:    
            while True:
                    join6 = pyautogui.locateOnScreen('images/ok.png')
                    if join6!=None:

                        def click(picture):
                            a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                            b=pyautogui.center(a)  
                            x,y=b
                            pyautogui.click(x, y)
                        click('images/ok.png')
                        webbrowser.open(linkInput)
                        break
            
                
    elif linkBox.get()=="":
        messagebox.showerror("error in starting","Please fill link field")            
            
def linkScreen():

    global linkBox
    global link  


    link = Tk()
    link.iconbitmap('images/zoom.ico')
    link.title('login with link')
    link.geometry("320x200")
    link.resizable(False,False)

    linkBox=Entry(link,width=30)
    linkBox.grid(row=1,column=1)

   
    space3 = Label(link, text="")
    space3.grid(row=0,column=0)
    
    linkLabel = Label(link, text="Enter link : ")
    linkLabel.grid(row=1,column=0)

    submitButton= Button(link,text="submit",command=goZoomWithLink)
    submitButton.grid(row=3,column=1)

    space4= Label(link,text="")
    space4.grid(row=2,column=0)

    space12= Label(link,text="")
    space12.grid(row=4,column=0)

    
    

def goZoomWithId():
    if idBox.get()!="" and passwordBox.get()!="":
        idInput=idBox.get()
        passwordInput=passwordBox.get()
        id.destroy()
         
        import pyautogui
     
        while True:
            join1 = pyautogui.locateOnScreen('images/join.png')
            joinnew=pyautogui.locateOnScreen('images/joinnew.png')
            if join1!=None or joinnew!=None:

                def click(picture):
                    a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    b=pyautogui.center(a)  
                    x,y=b
                    pyautogui.click(x, y)
                try:

                    click('images/join.png')
                except:
                    click('images/joinnew.png')    
            
        
                
                break
   
        # type id
        while True:
            join2 = pyautogui.locateOnScreen('images/id.png')
            if join2!=None:
                def click(picture):
                    a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    b=pyautogui.center(a)  
                    x,y=b
                    pyautogui.click(x, y)
                click('images/id.png')
                pyautogui.typewrite(idInput)
                       
                break

        
        # press join after id
        while True:
            join3 = pyautogui.locateOnScreen('images/join2.png')
            if join3!=None:
                def click(picture):
                    a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    b=pyautogui.center(a)  
                    x,y=b
                    pyautogui.click(x, y)
                click('images/join2.png')
                    
                break
        # type password
        while True:
            join4 = pyautogui.locateOnScreen('images/pass.png')
            join41 = pyautogui.locateOnScreen('images/pass1.png')
            if join4!=None or join41!=None:
                def click(picture):
                    a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    b=pyautogui.center(a)  
                    x,y=b
                    pyautogui.click(x, y)
                try:
                    click('images/pass.png')
                except:
                    click('images/pass1.png')    
                pyautogui.typewrite(passwordInput)
                
                break
                                 
        # press join after typing password    
        while True:
            join5 = pyautogui.locateOnScreen('images/join3.png')
            if join5!=None:
                def click(picture):
                    a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    b=pyautogui.center(a)  
                    x,y=b
                    pyautogui.click(x, y)
                click('images/join3.png')
              
                break
                                                 
        # press ok button after first meeting ended
        while True:
            join6 = pyautogui.locateOnScreen('images/ok.png')
            if join6!=None:
                def click(picture):
                    a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    b=pyautogui.center(a)  
                    x,y=b
                    pyautogui.click(x, y)
                click('images/ok.png')
                      
                break
                    
        while True:
                while True:
                    join1 = pyautogui.locateOnScreen('images/join.png')
                    joinnew = pyautogui.locateOnScreen('images/joinnew.png')
                    if join1!=None or joinnew!=None:
                        def click(picture):
                            a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                            b=pyautogui.center(a)  
                            x,y=b
                            pyautogui.click(x, y)
                        try:    
                            click('images/join.png')
                        except:
                            click('images/joinnew.png')    
                                                     
                        break
                                                    
            # type id
                while True:
                    join2 = pyautogui.locateOnScreen('images/id.png')
                    if join2!=None:
                        def click(picture):
                            a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                            b=pyautogui.center(a)  
                            x,y=b
                            pyautogui.click(x, y)
                        click('images/id.png')
                        pyautogui.typewrite(idInput)
                                               
                        break
                                                
                
                # press join after id
                while True:
                    join3 = pyautogui.locateOnScreen('images/join2.png')
                    if join3!=None:
                        def click(picture):
                            a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                            b=pyautogui.center(a)  
                            x,y=b
                            pyautogui.click(x, y)
                        click('images/join2.png')
                           
                        break
                  
                # type password
                while True:
                    join4 = pyautogui.locateOnScreen('images/pass.png')
                    join41 = pyautogui.locateOnScreen('images/pass1.png')
                    if join4!=None or join41!=None:
                        def click(picture):
                            a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                            b=pyautogui.center(a)  
                            x,y=b
                            pyautogui.click(x, y)
                        try:

                            click('images/pass.png')
                        except:
                            click('images/pass1.png')    
                        pyautogui.typewrite(passwordInput)
                                               
                        break
                
                # press join after typing password    
                while True:
                    join5 = pyautogui.locateOnScreen('images/join3.png')
                    if join5!=None:
                        def click(picture):
                            a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                            b=pyautogui.center(a)  
                            x,y=b
                            pyautogui.click(x, y)
                        click('images/join3.png')
                                           
                        break
                                                                  
                # press ok button after first meeting ended
                while True:
                    join6 = pyautogui.locateOnScreen('images/ok.png')
                    if join6!=None:
                        def click(picture):
                            a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                            b=pyautogui.center(a)  
                            x,y=b
                            pyautogui.click(x, y)
                        click('images/ok.png')
                                            
                        break
   
    elif idBox.get()=="" and passwordBox.get()=="":
        messagebox.showerror('error in starting',"Please fill id and password fields")
    elif idBox.get()=="":
        messagebox.showerror('error in starting',"Please fill id field")
    elif passwordBox.get()=="":
        messagebox.showerror('error in starting',"Please fill password field")
   
def idScreen():
    global idBox
    global passwordBox
    global id
    global startTimeBox
    global endTimeBox

    
    id = Tk()
    id.iconbitmap('images/zoom.ico')
    id.title('login with id')
    id.geometry("350x200")
    id.resizable(False,False)

    idBox=Entry(id,width=30)
    idBox.grid(row=1,column=1)


    passwordBox=Entry(id,width=30)
    passwordBox.grid(row=3,column=1)



    space3 = Label(id, text="")
    space3.grid(row=0,column=0)
    
    idLabel = Label(id, text="Enter id : ")
    idLabel.grid(row=1,column=0)

    passwordLabel = Label(id, text="Enter password : ")
    passwordLabel.grid(row=3,column=0)
    

    submitButton= Button(id,text="submit",command=goZoomWithId)
    submitButton.grid(row=5,column=1)

    space24=Label(id,text="")
    space24.grid(row=4,column=0)
    
    space25=Label(id,text="")
    space25.grid(row=2,column=0)

btn=Button(root,text="id",width=5,bg='lightgrey',font="3",command=idScreen)
btn.grid(row=1,column=1)

btn1=Button(root,text="link",width=5,bg='lightgrey',font="3",command=linkScreen)
btn1.grid(row=3,column=1)

instruction1 = Label(root,text="1.Minimize other windows")
instruction2 = Label(root,text="2.Click above suitable button")
instruction3 = Label(root,text="3.Enter details")
instruction4 = Label(root,text="4.Click submit button")
instruction5 = Label(root,text="5.Run Zoom App")


instruction1.grid(row=5,column=1)
instruction2.grid(row=6,column=1)
instruction3.grid(row=7,column=1)
instruction4.grid(row=8,column=1)
instruction5.grid(row=9,column=1)

space=Label(root,text="")
space.grid(row=2,column=0)


space1=Label(root,text="                     ")
space1.grid(row=4,column=0)

space2=Label(root,text="")
space2.grid(row=0,column=0)





root.mainloop()
