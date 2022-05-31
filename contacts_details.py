
from os import error
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import font

root=Tk()
root.title("Contacts' details")
root.iconbitmap("images/table.ico")
root.geometry("560x750")
root.resizable(False,False)
root.configure(bg="#878ca8")
  

# create a database and connect to one

conn = sqlite3.connect('address_book.db')

# create a cursor
c=conn.cursor()

# create table 
try:
    c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode text,
        phone_number text,
        country text
    )
    """)
except:
    pass   



    

def update():
            # create a database and connect to one

            conn = sqlite3.connect('address_book.db')

            # create a cursor
            c=conn.cursor()
            if (f_name_editor.get()=="" and l_name_editor.get()=="") and (address_editor.get()=="" and city_editor.get()=="") and (state_editor.get()=="" and zipcode_editor.get()=="") and (phone_number_editor.get()=="" and country_editor.get()==""):
                # create a database and connect to one

                conn = sqlite3.connect('address_book.db')

                # create a cursor
                c=conn.cursor()
                # delete a record 
                c.execute("DELETE from addresses WHERE oid="+record_id)
                

                # commit changes
                conn.commit()

                # close connection
                conn.close()
                
                error3=messagebox.showwarning("informaing",f"Record in id {record_id} ,deleted !")
                editor.destroy()
            else:
                c.execute("""UPDATE addresses SET
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode,
                    phone_number=:phone_number,
                    country=:country
                        
                    WHERE oid=:oid""",
                    {
                        'first':f_name_editor.get(),
                        'last':l_name_editor.get(),
                        'address':address_editor.get(),
                        'city':city_editor.get(),
                        'state':state_editor.get(),
                        'zipcode':zipcode_editor.get(),
                        'phone_number':phone_number_editor.get(),
                        'country':country_editor.get(),
                        'oid':record_id

                    }
                
                        
                )


                # commit changes
                conn.commit()

                # close connection
                conn.close()
                response = messagebox.showinfo("Updating record", "You successfully updated the record !")
                editor.destroy()


# create a edit function
def edit():
    
    if delete_box.get()=="":
        error4=messagebox.showerror("error in updating","Please fill select id field !")
    else:
                
                    # create a database and connect to one

                    conn = sqlite3.connect('address_book.db')

                    # create a cursor
                    c=conn.cursor()
                    c.execute("SELECT * FROM addresses WHERE oid="+delete_box.get())
                    records = c.fetchall()
                    if records==[]:
                        error2=messagebox.showerror("error in updating","Selected id has no record !")
                        delete_box.delete(0,END)
                    else:
                        # make variables global
                        global f_name_editor
                        global l_name_editor
                        global address_editor
                        global city_editor
                        global state_editor
                        global zipcode_editor
                        global phone_number_editor
                        global country_editor
                        global record_id
                        global editor

                        editor=Tk()
                        editor.title("Update record")
                        editor.iconbitmap("images/table.ico")
                        editor.geometry("530x400")
                        editor.resizable(False,False)
                        editor.configure(bg="#878ca8")


                        
                        record_id=delete_box.get()
                        delete_box.delete(0,END)

                        # query the database
                        c.execute("SELECT * FROM addresses WHERE oid="+record_id)
                        records = c.fetchall()


                        # create text boxes
                        f_name_editor = Entry(editor, width=30,bg="#c1c1c7",fg="#000000",font="13")
                        f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))

                        l_name_editor = Entry(editor, width=30,bg="#c1c1c7",fg="#000000",font="13")
                        l_name_editor.grid(row=1,column=1,padx=20)

                        address_editor = Entry(editor, width=30,bg="#c1c1c7",fg="#000000",font="13")
                        address_editor.grid(row=2,column=1,padx=20)

                        city_editor = Entry(editor, width=30,bg="#c1c1c7",fg="#000000",font="13")
                        city_editor.grid(row=3,column=1,padx=20)

                        state_editor = Entry(editor, width=30,bg="#c1c1c7",fg="#000000",font="13")
                        state_editor.grid(row=4,column=1,padx=20)

                        zipcode_editor = Entry(editor, width=30,bg="#c1c1c7",fg="#000000",font="13")
                        zipcode_editor.grid(row=5,column=1,padx=20)

                        phone_number_editor = Entry(editor, width=30,bg="#c1c1c7",fg="#000000",font="13")
                        phone_number_editor.grid(row=6,column=1,padx=20)

                        country_editor = Entry(editor, width=30,bg="#c1c1c7",fg="#000000",font="13")
                        country_editor.grid(row=7,column=1,padx=20)

                        #create text box labels
                        f_name_label_editor=Label(editor, text="First Name :-",bg="#95addb",fg="#000000",font="13",width=20)
                        f_name_label_editor.grid(row=0,column=0,pady=(10,0))

                        l_name_label_editor=Label(editor, text="Last Name :-",bg="#c1cce3",fg="#000000",font="13",width=20)
                        l_name_label_editor.grid(row=1,column=0)

                        address_label_editor=Label(editor, text="Address :-",bg="#95addb",fg="#000000",font="13",width=20)
                        address_label_editor.grid(row=2,column=0)

                        city_label_editor=Label(editor, text="City :-",bg="#c1cce3",fg="#000000",font="13",width=20)
                        city_label_editor.grid(row=3,column=0)

                        state_label_editor=Label(editor, text="State :-",bg="#95addb",fg="#000000",font="13",width=20)
                        state_label_editor.grid(row=4,column=0)

                        zipcode_label_editor=Label(editor, text="Zipcode :-",bg="#c1cce3",fg="#000000",font="13",width=20)
                        zipcode_label_editor.grid(row=5,column=0)
                        
                        phone_number_label_editor=Label(editor, text="Phone number :-",bg="#95addb",fg="#000000",font="13",width=20)
                        phone_number_label_editor.grid(row=6,column=0)

                        country_label_editor=Label(editor, text="Country :-",bg="#c1cce3",fg="#000000",font="13",width=20)
                        country_label_editor.grid(row=7,column=0)

                        # loop through results
                        for record in records:
                            f_name_editor.insert(0,record[0])
                            l_name_editor.insert(0,record[1])
                            address_editor.insert(0,record[2])
                            city_editor.insert(0,record[3])
                            state_editor.insert(0,record[4])
                            zipcode_editor.insert(0,record[5])
                            phone_number_editor.insert(0,record[6])            
                            country_editor.insert(0,record[7])

                        # create a save button
                        save_btn = Button(editor, text="Save Record", command=update,bg="#dbd9de",fg="#000000",font="9",width=20)
                        save_btn.grid(row=8,column=0,columnspan=2,padx=10,pady=10,ipadx=145)
                            
                        # commit changes
                        conn.commit()

                        # close connection
                        conn.close()


# create a function to delete a record
def delete():
    if delete_box.get()=="":
        error5=messagebox.showerror("error in deleting","Please fill select id field !")
    else:
        

        # create a database and connect to one

        conn = sqlite3.connect('address_book.db')

        # create a cursor
        c=conn.cursor()
        c.execute("SELECT * FROM addresses WHERE oid="+delete_box.get())
        records = c.fetchall()
        if records==[]:
            error6=messagebox.showerror("error in deleting","Selected id has no record !")
            delete_box.delete(0,END)
        else:    
            # delete a record 
            c.execute("DELETE from addresses WHERE oid="+delete_box.get())
            delete_box.delete(0,END)
            # commit changes
            conn.commit()

            # close connection
            conn.close()
            response=messagebox.showinfo("Deleting a Record","You successfully deleted the record from the database !")


# create submit function for database
def submit():
    if (f_name.get()=="" and l_name.get()=="") and (address.get()=="" and city.get()=="") and (state.get()=="" and zipcode.get()=="") and (phone_number.get()=="" and country.get()==""):
        error10=messagebox.showerror("error in submitting","Please fill all fields !")
    
    elif f_name.get()=="":
        error11=messagebox.showerror("error in submitting","Please fill first name field !")    
    elif l_name.get()=="":
        error12=messagebox.showerror("error in submitting","Please fill last name field !")    
    elif address.get()=="":
        error13=messagebox.showerror("error in submitting","Please fill address field !")    
    elif city.get()=="":
        error14=messagebox.showerror("error in submitting","Please fill city field !")    
    elif state.get()=="":
        error15=messagebox.showerror("error in submitting","Please fill state field !")    
    elif zipcode.get()=="":
        error16=messagebox.showerror("error in submitting","Please fill zipcode field !")    
    elif phone_number.get()=="":
        error17=messagebox.showerror("error in submitting","Please fill phone number field !")
    elif country.get()=="":
        error18=messagebox.showerror("error in submitting","Please fill country field !")                                                                
    elif (f_name.get()!="" and l_name.get()!="") and (address.get()!="" and city.get()!="") and (state.get()!="" and zipcode.get()!="") and (phone_number.get()!="" and country.get()!=""):
            

        # create a database and connect to one

        conn = sqlite3.connect('address_book.db')

        # create a cursor
        c=conn.cursor()

        # Insert into the table
        c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode,:phone_number,:country)",
        {
            'f_name':f_name.get(),
            'l_name':l_name.get(),
            'address':address.get(),
            'city':city.get(),
            'state':state.get(),
            'zipcode':zipcode.get(),
            'phone_number':phone_number.get(),
            'country':country.get()
        })

        # commit changes
        conn.commit()

        # close connection
        conn.close()
        response=messagebox.showinfo("Adding a Record","You successfully added a record to the database !")

        f_name.delete(0,END)
        l_name.delete(0,END)
        address.delete(0,END)
        city.delete(0,END)
        state.delete(0,END)
        zipcode.delete(0,END)
        phone_number.delete(0,END)
        country.delete(0,END)
    else:
        pass    

# create a query function
def query():
    from tkinter import ttk
    results=Tk()
    results.title("Database content")
    results.iconbitmap("images/table.ico")
    results.geometry("1200x500")
    results.resizable(False,False)
    results.configure(bg="#878ca8")
    
    # Steps to create full screen scroll bar

    # 1.Create a main frame
    main_frame = Frame(results)
    main_frame.pack(fill=BOTH,expand=1)
    main_frame.configure(bg="#878ca8")

    # 2.Create a canvas
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)


    # 3.Add Scroll bar to the canvas
    my_scrollbar_veritcal=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar_veritcal.pack(side=RIGHT,fill=Y)
    my_scrollbar_horizontal=ttk.Scrollbar(main_frame,orient=HORIZONTAL,command=my_canvas.xview)
    my_scrollbar_horizontal.pack(side=BOTTOM,fill=X)
    
    # 4.Configure canvas
    my_canvas.configure(yscrollcommand=my_scrollbar_veritcal.set)
    my_canvas.configure(xscrollcommand=my_scrollbar_horizontal.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    
    # 5.Create another frame inside canvas
    second_frame = Frame(my_canvas)

    # 6.Add that New frame to to a window in the canvas
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")
    my_canvas.configure(bg="#878ca8")
    # create a database and connect to one
    second_frame.configure(bg="#878ca8")
    conn = sqlite3.connect('address_book.db')
    
    # create a cursor
    c=conn.cursor()

    # query the database
    
    id_heading=Label(second_frame, text="ID",fg="#000000",font="15")
    id_heading.grid(row=0,column=0,padx=30,pady=20)

    f_heading=Label(second_frame, text="First name",fg="#000000",font="15")
    f_heading.grid(row=0,column=1,padx=20,pady=20)

    l_heading=Label(second_frame, text="Last name",fg="#000000",font="15")
    l_heading.grid(row=0,column=2,padx=20,pady=20)

    address_heading=Label(second_frame, text="Address",fg="#000000",font="15")
    address_heading.grid(row=0,column=3,padx=20,pady=20)    

    city_heading=Label(second_frame, text="City",fg="#000000",font="15")
    city_heading.grid(row=0,column=4,padx=20,pady=20)
    
    state_heading=Label(second_frame, text="State",fg="#000000",font="15")
    state_heading.grid(row=0,column=5,padx=20,pady=20)    
    
    zipcode_heading=Label(second_frame, text="Zipcode",fg="#000000",font="15")
    zipcode_heading.grid(row=0,column=6,padx=20,pady=20)    

    phone_number_heading=Label(second_frame, text="Phone number",fg="#000000",font="15")
    phone_number_heading.grid(row=0,column=7,padx=20,pady=20)    

    country_heading=Label(second_frame, text="Country",fg="#000000",font="15")
    country_heading.grid(row=0,column=8,padx=20,pady=20)    

    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()

    print_records=""
    
    for record in records:
        print_records+=str(record[8])+"\n"
    id_label=Label(second_frame,text=print_records,bg="#878ca8",fg="#ffffff",font="12")
    id_label.grid(row=1,column=0,pady=20)    
    
    print_records1=""
    
    for record in records:
        print_records1+=str(record[0])+"\n"
    id_label1=Label(second_frame,text=print_records1,bg="#878ca8",fg="#ffffff",font="12")
    id_label1.grid(row=1,column=1,pady=20)    
    
    print_records2=""
    
    for record in records:
        print_records2+=str(record[1])+"\n"
    id_label2=Label(second_frame,text=print_records2,bg="#878ca8",fg="#ffffff",font="12")
    id_label2.grid(row=1,column=2,pady=20)    

    print_records3=""
    
    for record in records:
        print_records3+=str(record[2])+"\n"
    id_label3=Label(second_frame,text=print_records3,bg="#878ca8",fg="#ffffff",font="12")
    id_label3.grid(row=1,column=3)    

    print_records4=""
    
    for record in records:
        print_records4+=str(record[3])+"\n"
    id_label4=Label(second_frame,text=print_records4,bg="#878ca8",fg="#ffffff",font="12")
    id_label4.grid(row=1,column=4)    

    print_records5=""
    
    for record in records:
        print_records5+=str(record[4])+"\n"
    id_label5=Label(second_frame,text=print_records5,bg="#878ca8",fg="#ffffff",font="12")
    id_label5.grid(row=1,column=5)    

    print_records6=""
    
    for record in records:
        print_records6+=str(record[5])+"\n"
    id_label6=Label(second_frame,text=print_records6,bg="#878ca8",fg="#ffffff",font="12")
    id_label6.grid(row=1,column=6)    

    print_records7=""
    
    for record in records:
        print_records7+=str(record[6])+"\n"
    id_label7=Label(second_frame,text=print_records7,bg="#878ca8",fg="#ffffff",font="12")
    id_label7.grid(row=1,column=7)    
    

    print_records8=""
    
    for record in records:
        print_records8+=str(record[7])+"\n"
    id_label8=Label(second_frame,text=print_records8,bg="#878ca8",fg="#ffffff",font="12")
    id_label8.grid(row=1,column=8)    

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create text boxes
f_name = Entry(root, width=30,bg="#c1c1c7",fg="#000000",font="13")
f_name.grid(row=0,column=1,padx=20,pady=(10,0))

l_name = Entry(root, width=30,bg="#c1c1c7",fg="#000000",font="13")
l_name.grid(row=1,column=1,padx=20)

address = Entry(root, width=30,bg="#c1c1c7",fg="#000000",font="13")
address.grid(row=2,column=1,padx=20)

city = Entry(root, width=30,bg="#c1c1c7",fg="#000000",font="13")
city.grid(row=3,column=1,padx=20)

state = Entry(root, width=30,bg="#c1c1c7",fg="#000000",font="13")
state.grid(row=4,column=1,padx=20)

zipcode = Entry(root, width=30,bg="#c1c1c7",fg="#000000",font="13")
zipcode.grid(row=5,column=1,padx=20)


phone_number = Entry(root, width=30,bg="#c1c1c7",fg="#000000",font="13")
phone_number.grid(row=6,column=1,padx=20)


country = Entry(root, width=30,bg="#c1c1c7",fg="#000000",font="13")
country.grid(row=7,column=1,padx=20)

delete_box = Entry(root, width=30,bg="#c1c1c7",fg="#000000",font="13")
delete_box.grid(row=11,column=1,padx=20,pady=20)

#create text box labels
f_name_label=Label(root, text="First Name :-",bg="#95addb",font="13",width=20)
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root, text="Last Name :-",bg="#c1cce3",font="13",width=20)
l_name_label.grid(row=1,column=0)

address_label=Label(root, text="Address :-",bg="#95addb",fg="#000000",font="13",width=20)
address_label.grid(row=2,column=0)

city_label=Label(root, text="City :-",bg="#c1cce3",fg="#000000",font="13",width=20)
city_label.grid(row=3,column=0)

state_label=Label(root, text="State :-",bg="#95addb",fg="#000000",font="13",width=20)
state_label.grid(row=4,column=0)

zipcode_label=Label(root, text="Zipcode :-",bg="#c1cce3",fg="#000000",font="13",width=20)
zipcode_label.grid(row=5,column=0)

phone_number_label=Label(root, text="Phone number :-",bg="#95addb",fg="#000000",font="13",width=20)
phone_number_label.grid(row=6,column=0)

country_label=Label(root, text="Country :-",bg="#c1cce3",fg="#000000",font="13",width=20)
country_label.grid(row=7,column=0)

delete_box_label=Label(root, text="Select ID :-",bg="#95addb",fg="#000000",font="13",width=20)
delete_box_label.grid(row=11,column=0,pady=5)

    

# create submit button
submit_button = Button(root, text="Add Record to the Database",command=submit,bg="#dbd9de",fg="#000000",font="9",width=5)
submit_button.grid(row=8,column=0,columnspan=2,pady=20,padx=10,ipadx=100)

# create a query button
query_btn = Button(root, text="Show Records", command=query,bg="#dbd9de",fg="#000000",font="9",width=5)
query_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=100)



# create a delete button
delete_btn = Button(root, text="Delete Record", command=delete,bg="#dbd9de",fg="#000000",font="9",width=5)
delete_btn.grid(row=12,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

# create an update button
edit_btn = Button(root, text="Update Record", command=edit,bg="#dbd9de",fg="#000000",font="9",width=5)
edit_btn.grid(row=13,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

# CREATE CHECKBOX

var = StringVar()
check = Checkbutton(root, text="Check here to send the database to developer",variable=var,onvalue="on",offvalue="off",bg="#c1c1c7",fg="#000000",font="11")
check.deselect()
check.grid(row=14,column=0,columnspan=2,pady=20)

my_name_input=Entry(root,width=20,bg="#c1c1c7",fg="#000000",font="13")
my_name_input.grid(row=15,column=1,pady=5,padx=5)

my_name=Label(root,text="Please enter your name here :-",bg="#c1cce3",fg="#000000",font="13")
my_name.grid(row=15,column=0,pady=10)

# create send function
def send():
    if var.get()=="off" and my_name_input.get()=="":
        error9=messagebox.showerror("error in sending","check box is not checked and your name not entered !")
    elif var.get()=="off":
        error7=messagebox.showerror("error in sending","Check box not checked !")
    elif my_name_input.get()=="":
        error8=messagebox.showerror("error in sending","Enter your name !")
    
                
    elif var.get()=="on" and my_name_input!="":
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        mail_content = f"This is address_book.db file sent by {my_name_input.get()}"

        #The mail addresses and password
        sender_address = 'vishwapraveen2021@gmail.com'
        sender_pass = 'vishwa@Praveen2021'
        receiver_address = 'vishwapraveen4618@gmail.com'

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = f'address_book.db sent by {my_name_input.get()}'

        #The subject line

        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'address_book.db'
        attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload) #encode the attachment

        #add payload header with filename
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)

        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        responsenew=messagebox.showinfo("Sending database","You successfully send the database to developer !")
        my_name_input.delete(0,END)
        check.deselect()
    else:
        pass    
        

#create check box button
check_btn = Button(root,text="Send",command=send,bg="#dbd9de",fg="#000000",font="10")
check_btn.grid(row=21,column=0,columnspan=2,pady=10)

# instructions
instruction1=Label(root,text="1.Check the box.",fg="#f2f0f5",font="11",bg="#878ca8")
instruction1.grid(row=16,column=0,columnspan=2)

instruction2=Label(root,text="2.Enter your name.",fg="#f2f0f5",font="11",bg="#878ca8")
instruction2.grid(row=18,column=0,columnspan=2)

instruction3=Label(root,text="3.Click send button.",fg="#f2f0f5",font="11",bg="#878ca8")
instruction3.grid(row=19,column=0,columnspan=2)

instruction4=Label(root,text="** This use some time to send the database.So ,wait patiently !. **",fg="#f2f0f5",font="11",bg="#878ca8")
instruction4.grid(row=20,column=0,columnspan=2)


# commit changes
conn.commit()

# close connection
conn.close()
root.mainloop()
