import csv
from tkinter import *
import mysql.connector 
from tkinter import ttk
from tkinter import messagebox
from tkhtmlview import HTMLLabel
from tkinter.filedialog import asksaveasfile
import time
def login_to_sql():
    password = password_box.get()
    username = username_box.get()
    if password_box.get()=='' and username_box.get()=='':
        messagebox.showerror('Login error','Please enter login credentials')
    elif password_box.get()=='':
        messagebox.showerror('Login error','Please enter login password')
    elif username_box.get()=='':
        messagebox.showerror('Login error','Please enter login username')
    else:

        login_window.destroy()

        root = Tk()
        root.title('Customer Relationship Management Tool')
        root.iconbitmap('images/cus.ico')
        root.geometry("400x600")
        root.resizable(False,False)

        # connect to mysql database
        try:
            mydb = mysql.connector.connect(
                host = "localhost",
                user = username,
                passwd = password,
                
            )
        except mysql.connector.errors.ProgrammingError as login_error:
            messagebox.showerror('login error',login_error)
            root.destroy()

        

        # check whether connection to MySQL was created
        # print(mydb)

        try:        
            # create a cursor and initialize it 
            my_cursor = mydb.cursor()
        except mysql.connector.errors.ProgrammingError as login_error:
            messagebox.showerror('login error',login_error)
            root.destroy()

        try:            
            # create database
            my_cursor.execute("CREATE DATABASE IF NOT EXISTS CRM")
        except:
            messagebox.showerror('login error','Cound not login')
            root.destroy()
            

        try:        
            mydb = mysql.connector.connect(
                host = "localhost",
                user = username,
                passwd = password,
                database = "crm"
            )
        except:
            messagebox.showerror('login error','Cound not login')
            root.destroy()
      
        # Test to see database created 
        # my_cursor.execute("SHOW DATABASES")
        # for db in my_cursor:
        #     print(db)
        try:        
            # create a cursor and initialize it 
            my_cursor = mydb.cursor()
        except:
            messagebox.showerror('login error','Cound not login')
            root.destroy()

        try:            
            # create database
            my_cursor.execute("CREATE DATABASE IF NOT EXISTS CRM")
        except:
            messagebox.showerror('login error','Cound not login')
            root.destroy()
            
        try:        
            # Create a table
            my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255),last_name VARCHAR(255),zipcode INT(10),price_paid DECIMAL(10, 2),user_id INT AUTO_INCREMENT PRIMARY KEY,email VARCHAR(255),address_1 VARCHAR(255),address_2 VARCHAR(255),city VARCHAR(50),state VARCHAR(50),country VARCHAR(255),phone VARCHAR(255),payment_method VARCHAR(50),discount_code VARCHAR(255))")
        except:
            messagebox.showerror('login error','Cound not login')
            root.destroy()
            
        # show table
        # my_cursor.execute("SELECT * FROM customers")
        #for thing in my_cursor.description:
        #     print(thing)

        # delete table
        # my_cursor.execute("DROP TABLE customers")

        # alter the table
        # my_cursor.execute("ALTER TABLE customers ADD (email VARCHAR(255),address_1 VARCHAR(255),address_2 VARCHAR(255),city VARCHAR(50),state VARCHAR(50),country VARCHAR(255),phone VARCHAR(255),payment_method VARCHAR(50),discount_code VARCHAR(255))")
        def info_developer():
            info_window = Toplevel()
            info_window.title('Info')
            info_window.iconbitmap('images/cus.ico')
            info_window.geometry("200x300")
            info_window.resizable(False,False)
            html_details = HTMLLabel(info_window,html="""<p>Coded by Vishwa Praveen(Vpsoftwares) with the help of John Elder(Codemy.com).</p><br><center><img src='images/logo.jpg'></center><br><br><a href='https://vpsoftwares.herokuapp.com/'>Visit developer's website</a>""")
            html_details.pack()
     
        def help_user():


            def email_question():
                if (name_box.get()=='' and email_help_box.get()=="") and question_text_box.get("1.0", "end-1c")=='':
                    messagebox.showwarning('Emailing question','Please fill all entries !')
                elif name_box.get()=='':
                    messagebox.showwarning('Emailing question','Please fill name entry !')
                elif email_help_box.get()=='':
                    messagebox.showwarning('Emailing question','Please fill email entry !')
                elif question_text_box.get("1.0", "end-1c")=='':
                    messagebox.showwarning('Emailing question','Please fill question entry !')
                else:
                    try:
                        import smtplib
                        from email.mime.multipart import MIMEMultipart
                        from email.mime.text import MIMEText
                        from email.mime.base import MIMEBase
                        from email import encoders

                        mail_content = f"""[name :{name_box.get()}][email :{email_help_box.get()}][question:{question_text_box.get("1.0", "end-1c")}]"""

                        #The mail addresses and password
                        sender_address = 'stesting562@gmail.com'
                        sender_pass = 'testing@computer1234'
                        receiver_address = 'vishwapraveen4618@gmail.com'

                        #Setup the MIME
                        message = MIMEMultipart()
                        message['From'] = sender_address
                        message['To'] = receiver_address
                        message['Subject'] = f'Customer relationship management tool question by {name_box.get()}'

                        #The subject line

                        #The body and the attachments for the mail
                        message.attach(MIMEText(mail_content, 'plain'))
                        #attach_file_name = 'address_book.db'
                        #attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
                        #payload = MIMEBase('application', 'octate-stream')
                        #payload.set_payload((attach_file).read())
                        #encoders.encode_base64(payload) #encode the attachment

                        #add payload header with filename
                        #payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
                        #message.attach(payload)

                        #Create SMTP session for sending the mail
                        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                        session.starttls() #enable security
                        session.login(sender_address, sender_pass) #login with mail_id and password
                        text = message.as_string()
                        session.sendmail(sender_address, receiver_address, text)
                        session.quit()

                        name_box.delete(0,END)
                        email_help_box.delete(0,END)
                        question_text_box.delete("1.0", "end-1c")

                        messagebox.showinfo('Emailing question','Question successfully emailed to developer !') 

                    except:
                        messagebox.showerror('Emailing question','Sending question unsuccessful !')

            help_window = Toplevel()
            help_window.title('Help')
            help_window.iconbitmap('images/cus.ico')
            help_window.geometry("450x400")
            help_window.resizable(False,False)
            
            space3 = Label(help_window, text='').grid(row=0,column=0)
            space4 = Label(help_window, text='').grid(row=1,column=0)
            
            name_label = Label(help_window, text='Name :').grid(row=1,column=1)            
            name_box = Entry(help_window,width=30)
            name_box.grid(row=1,column=2)

            space5 = Label(help_window, text='').grid(row=2,column=0)

            email_help_label = Label(help_window, text='Email :').grid(row=3,column=1)            
            email_help_box = Entry(help_window,width=30)
            email_help_box.grid(row=3,column=2)
            
            space6 = Label(help_window, text='').grid(row=4,column=0)

            question_label = Label(help_window,text='Question/Bug/Error/Help :').grid(row=5,column=1)
            question_text_box = Text(help_window,wrap='word',height=10,width=30)
            question_text_box.grid(row=5,column=2)

            space7 = Label(help_window, text='').grid(row=6,column=0)

            help_button = Button(help_window, text='Send to developer',command=email_question)
            help_button.grid(row=7,column=2)

            space8= Label(help_window, text='').grid(row=8,column=0)
           

          

        # Clear text fields
        def clear_fields():
            first_name_box.delete(0,END)
            last_name_box.delete(0,END)
            address1_box.delete(0,END)
            address2_box.delete(0,END)
            city_box.delete(0,END)
            state_box.delete(0,END)
            zipcode_box.delete(0,END)
            country_box.delete(0,END)
            phone_box.delete(0,END)
            email_box.delete(0,END)
            payment_method_box.delete(0,END)
            discount_code_box.delete(0,END)
            price_paid_box.delete(0,END)
            messagebox.showinfo('Clearing Entries','Entries cleared !')
        # Submit customer to database (%s is a placeholder)
        def add_customer():
            if (first_name_box.get()=='' and last_name_box.get()=='') and (address1_box.get()=='' and address2_box.get()=='') and (city_box.get()=='' and state_box.get()=='') and (zipcode_box.get()=='' and country_box.get()=='') and (phone_box.get()=='' and email_box.get()=='') and (payment_method_box.get()=='' and discount_code_box.get()=='') and price_paid_box.get()=='':
                messagebox.showwarning('Entering data','Please enter data into entries !')
            elif first_name_box.get()=='':
                messagebox.showwarning('Entering data','Please enter first name !')
            elif last_name_box.get()=='':
                messagebox.showwarning('Entering data','Please enter last name !')        
            elif address1_box.get()=='':
                messagebox.showwarning('Entering data','Please enter Address 1 !')
            elif city_box.get()=='':
                messagebox.showwarning('Entering data','Please enter city !')
            elif country_box.get()=='':
                messagebox.showwarning('Entering data','Please enter country !')
            elif phone_box.get()=='':
                messagebox.showwarning('Entering data','Please enter phone number !')
            elif email_box.get()=='':
                messagebox.showwarning('Entering data','Please enter email !')
            elif zipcode_box.get()=='':
                messagebox.showwarning('Entering data','Please enter zipcode !')
            elif price_paid_box.get()=='':
                messagebox.showwarning('Entering data','Please enter price paid !')       
            else:
                try:
                                            
                    sql_command= "INSERT INTO customers (first_name,last_name,zipcode,price_paid,email,address_1,address_2,city,state,country,phone,payment_method,discount_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (first_name_box.get(),last_name_box.get(),zipcode_box.get(),price_paid_box.get(),email_box.get(),address1_box.get(),address2_box.get(),city_box.get(),state_box.get(),country_box.get(),phone_box.get(),payment_method_box.get(),discount_code_box.get())
                    my_cursor.execute(sql_command, values)

                    # Commit the changes to the database
                    mydb.commit()

                    # clear the fields
                    clear_fields()
                    messagebox.showinfo('Entering data','Record successfully added to database !')
                except mysql.connector.errors.DatabaseError as d:
                    messagebox.showerror('Entering Data',d)
        # Write to csv  Excel function ('a' stands for append, 'w' stands for write)
        def write_to_csv(result):
                 
            f = asksaveasfile(initialfile = 'Untitled.csv',title='Save to a excel file',
defaultextension=".csv",filetypes=[("Excel csv files","*.csv")])

            try:
                
                with open(f.name,'w',newline='') as f:
                    w = csv.writer(f,dialect='excel')
                    
                    
                    w.writerow(('first name','last name','zip code','price paid','id','email','address 1','address 2','city','state','country','phone number','payment method','discount code'))
                    w.writerow('\n')
                    for record in result:
                        w.writerow(record)
            except AttributeError as attribute:
                messagebox.showerror('Saving to Excel',attribute)                    
                   
        # Search Customers
        def search_customers():
            search_customers_window = Toplevel()
            search_customers_window.title('Search Customers')
            search_customers_window.iconbitmap('images/cus.ico')
            search_customers_window.geometry("980x680")
            


            

        
            def search_now():
   
                text_box.config(state='normal')
                
                def delete_record():
                    answer1=messagebox.askyesno('Deleting Record','Are you sure about deleting record ?')
                    if answer1==True:
                        id_box_edit.config(state= "normal")
                        id_value = id_box_edit.get()
                        my_cursor.execute(f'DELETE FROM customers WHERE user_id={id_value}')
                        mydb.commit()
                        messagebox.showinfo('Delete record','Record deleted from the database successfully !')
                        edit_window.destroy()
                    elif answer1==False:
                        messagebox.showinfo('Deleting Record','Record not deleted !')

                def update_record():
                    answer=messagebox.askyesno('Updating record','Are you sure updating record ?')
                    
                    if answer==True:
                        if (first_name_box_edit.get()=='' and last_name_box_edit.get()=='') and (address1_box_edit.get()=='' and address2_box_edit.get()=='') and (city_box_edit.get()=='' and state_box_edit.get()=='') and (zipcode_box_edit.get()=='' and country_box_edit.get()=='') and (phone_box_edit.get()=='' and email_box_edit.get()=='') and (payment_method_box_edit.get()=='' and discount_code_box_edit.get()=='') and price_paid_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter data into entries !')
                        elif first_name_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter first name !')
                        elif last_name_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter last name !')        
                        elif address1_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter Address 1 !')
                        elif city_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter city !')
                        elif country_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter country !')
                        elif phone_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter phone number !')
                        elif email_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter email !')
                        elif zipcode_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter zipcode !')
                        elif price_paid_box_edit.get()=='':
                            messagebox.showwarning('Entering data','Please enter price paid !')       
                        else:                    
                            try:
                                id_box_edit.config(state= "normal")
                                sql_command = """UPDATE customers SET first_name = %s,last_name = %s,zipcode = %s,price_paid = %s,email = %s,address_1 = %s,address_2 = %s,city = %s,state = %s,country = %s,phone = %s,payment_method = %s,discount_code = %s WHERE user_id = %s"""
                                first_name=first_name_box_edit.get()
                                last_name=last_name_box_edit.get()
                                address1=address1_box_edit.get()
                                address2=address2_box_edit.get()
                                city=city_box_edit.get()
                                state=state_box_edit.get()
                                zipcode=zipcode_box_edit.get()
                                country=country_box_edit.get()
                                phone=phone_box_edit.get()
                                email=email_box_edit.get()
                                payment_method=payment_method_box_edit.get()
                                discount_code=discount_code_box_edit.get()
                                price_paid=price_paid_box_edit.get()

                                id_value = id_box_edit.get()
                                
                        
                                inputs = (first_name,last_name,zipcode,price_paid,email,address1,address2,city,state,country,phone,payment_method,discount_code,id_value)
                                my_cursor.execute(sql_command,inputs)
                                mydb.commit()
                                messagebox.showinfo('Updating record','Record updated successfully !')
                                edit_window.destroy()
                            except mysql.connector.errors.DatabaseError as d1:
                                messagebox.showerror('Updating record',d1)
                                id_box_edit.config(state= "disabled")
                    elif answer==False:
                        messagebox.showinfo('Updating record','Record not updated !')
                def edit_details(text):
            
                    sql2 = 'SELECT * FROM customers WHERE user_id = %s'
                
                    #sql = 'SELECT * FROM customers WHERE last_name = %s'
                    name2 = (text, )
                    my_cursor.execute(sql2, name2) 
                    result2 = my_cursor.fetchall()

                    global edit_window    

                    edit_window = Toplevel()
                    edit_window.title(f'Edit Customers Details (id {text})')
                    edit_window.iconbitmap('images/cus.ico')
                    edit_window.geometry("400x550")
                    edit_window.resizable(False,False)
                    
                    # Create main frame to enter customer data
                    first_name_label = Label(edit_window, text="First Name :").grid(row=1,column=0,sticky=W,padx=10)
                    last_name_label = Label(edit_window, text="Last Name :").grid(row=2,column=0,sticky=W,padx=10)
                    address1_label = Label(edit_window, text="Address 1 :").grid(row=3,column=0,sticky=W,padx=10)
                    address2_label = Label(edit_window, text="Address 2 :").grid(row=4,column=0,sticky=W,padx=10)
                    city_label = Label(edit_window, text="City :").grid(row=5,column=0,sticky=W,padx=10)
                    state_label = Label(edit_window, text="State :").grid(row=6,column=0,sticky=W,padx=10)
                    zipcode_label = Label(edit_window, text="Zipcode :").grid(row=7,column=0,sticky=W,padx=10)
                    country_label = Label(edit_window, text="Country :").grid(row=8,column=0,sticky=W,padx=10)
                    phone_label = Label(edit_window, text="Phone Number :").grid(row=9,column=0,sticky=W,padx=10)
                    email_label = Label(edit_window, text="Email Address :").grid(row=10,column=0,sticky=W,padx=10)
                    payment_method_label = Label(edit_window, text="Payment Method :").grid(row=11,column=0,sticky=W,padx=10)
                    discount_code_label = Label(edit_window, text="Discount Code :").grid(row=12,column=0,sticky=W,padx=10)
                    price_paid_label = Label(edit_window, text="Price Paid :").grid(row=13,column=0,sticky=W,padx=10)
                    id_label = Label(edit_window, text="ID :").grid(row=14,column=0,sticky=W,padx=10)
                

                    # Create entry boxes
                    global first_name_box_edit
                    first_name_box_edit = Entry(edit_window)
                    first_name_box_edit.grid(row=1,column=1,pady=5)
                    first_name_box_edit.insert(0, result2[0][0])

                    global last_name_box_edit
                    last_name_box_edit = Entry(edit_window)
                    last_name_box_edit.grid(row=2,column=1,pady=5)
                    last_name_box_edit.insert(0, result2[0][1])

                    global address1_box_edit
                    address1_box_edit = Entry(edit_window)
                    address1_box_edit.grid(row=3,column=1,pady=5)
                    address1_box_edit.insert(0, result2[0][6])

                    global address2_box_edit
                    address2_box_edit = Entry(edit_window)
                    address2_box_edit.grid(row=4,column=1,pady=5)
                    address2_box_edit.insert(0, result2[0][7])

                    global city_box_edit
                    city_box_edit = Entry(edit_window)
                    city_box_edit.grid(row=5,column=1,pady=5)
                    city_box_edit.insert(0, result2[0][8])

                    global state_box_edit
                    state_box_edit = Entry(edit_window)
                    state_box_edit.grid(row=6,column=1,pady=5)
                    state_box_edit.insert(0, result2[0][9])

                    global zipcode_box_edit
                    zipcode_box_edit = Entry(edit_window)
                    zipcode_box_edit.grid(row=7,column=1,pady=5)
                    zipcode_box_edit.insert(0, result2[0][2])

                    global country_box_edit
                    country_box_edit = Entry(edit_window)
                    country_box_edit.grid(row=8,column=1,pady=5)
                    country_box_edit.insert(0, result2[0][10])

                    global phone_box_edit
                    phone_box_edit = Entry(edit_window)
                    phone_box_edit.grid(row=9,column=1,pady=5)
                    phone_box_edit.insert(0, result2[0][11])

                    global email_box_edit
                    email_box_edit = Entry(edit_window)
                    email_box_edit.grid(row=10,column=1,pady=5)
                    email_box_edit.insert(0, result2[0][5])

                    global payment_method_box_edit
                    payment_method_box_edit = Entry(edit_window)
                    payment_method_box_edit.grid(row=11,column=1,pady=5)
                    payment_method_box_edit.insert(0, result2[0][12])

                    global discount_code_box_edit
                    discount_code_box_edit = Entry(edit_window)
                    discount_code_box_edit.grid(row=12,column=1,pady=5)
                    discount_code_box_edit.insert(0, result2[0][13])

                    global price_paid_box_edit
                    price_paid_box_edit = Entry(edit_window)
                    price_paid_box_edit.grid(row=13,column=1,pady=5)
                    price_paid_box_edit.insert(0, result2[0][3])

                    global id_box_edit
                    id_box_edit = Entry(edit_window)
                    id_box_edit.grid(row=14,column=1,pady=5)
                    id_box_edit.insert(0, result2[0][4])
                    id_box_edit.config(state= "disabled")

                    save_record_button =Button(edit_window,text='Update Record', command=update_record)
                    save_record_button.grid(row=15,column=1)

                    delet_record_button = Button(edit_window,text='Delete Record',command=delete_record)
                    delet_record_button.grid(row=15,column=0,padx=10)
                
                text_box.config(state='normal')   

                selected = drop.get()
                if selected =='Search by ...':
                    sql=''
                    
                    test = 'Hey! you forgot to drop down selection'
                    messagebox.showwarning('Selection',test)
                    text_box.config(state='disabled')
                    text_box.delete("1.0","end")
                if selected =='Last Name':
                    sql = 'SELECT * FROM customers WHERE last_name = %s'
                            
                if selected =='Email Address':
                    sql = 'SELECT * FROM customers WHERE email = %s'
                    
                if selected =='Customer ID':
                    sql = 'SELECT * FROM customers WHERE user_id = %s'
                            

                searched = search_box.get()
                #sql = 'SELECT * FROM customers WHERE last_name = %s'
                name = (searched, )
                my_cursor.execute(sql, name) 
                
                result = my_cursor.fetchall()   
                
                if not result:
                    text_box.delete("1.0","end")
                    result = ' Record Not Found.......'
                    searched_label =result
                    
                    messagebox.showerror('Query',searched_label)
                    text_box.config(state='disabled')
                    text_box.delete("1.0","end")
                    
                else:
                    text_box.delete("1.0","end")
                    list = [('First Name','Last Name','Zipcode','Price Paid','User id','Email','Address 1','Address 2','City','State','Country','Phone number','Payment method','Discount code')]
                    
                    edit_button = Button(text_box, text="          ", padx=2, pady=2)
                    text_box.window_create(END, window=edit_button)
                    for i in range(14):
                        e = Entry(text_box, width=20, fg='blue',
                            font=('Arial',16))
                        text_box.insert(END,' ')
                        e.insert(END,list[0][i])
                        e.config(state='disabled')
            
                        text_box.window_create(END, window=e)
                        
                    text_box.insert(END,'\n')                           
                    for x in result:
                        edit_button = Button(text_box, text="Edit "+str(x[4]), padx=2, pady=2,command=lambda text=str(x[4]):edit_details(text))
                        text_box.window_create(END, window=edit_button)
                        for i in x:
                            e = Entry(text_box, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                            text_box.insert(END,' ')
                            
                
                            e.insert(END,i)
                            e.config(state='disabled')
                
                            text_box.window_create(END, window=e)
                   
                        text_box.insert(END,'\n')   
                    
                    text_box.config(state='disabled')   
                         

                    
                    
        

            
        # Write to csv  Excel function ('a' stands for append, 'w' stands for write)
            def write_to_csv_new():
                                

                selected = drop.get()
                if selected =='Search by ...':
                    sql=''
                    
                    
                if selected =='Last Name':
                    sql = 'SELECT * FROM customers WHERE last_name = %s'
                            
                if selected =='Email Address':
                    sql = 'SELECT * FROM customers WHERE email = %s'
                    
                if selected =='Customer ID':
                    sql = 'SELECT * FROM customers WHERE user_id = %s'
                            

                searched = search_box.get()
                #sql = 'SELECT * FROM customers WHERE last_name = %s'
                name = (searched, )
                my_cursor.execute(sql, name) 
                
                result = my_cursor.fetchall()  
                    
                f = asksaveasfile(initialfile = 'Untitled.csv',title='Save to a excel file',
    defaultextension=".csv",filetypes=[("Excel csv files","*.csv")])

                try:
                    
                    with open(f.name,'w',newline='') as f:
                        w = csv.writer(f,dialect='excel')
                        
                        
                        w.writerow(('first name','last name','zip code','price paid','id','email','address 1','address 2','city','state','country','phone number','payment method','discount code'))
                        w.writerow('\n')
                        for record in result:
                            w.writerow(record)
                except AttributeError as attribute:
                    messagebox.showerror('Saving to Excel',attribute)                    
                    
            
            sb = Scrollbar(search_customers_window,orient=HORIZONTAL)
            sb.pack(side=BOTTOM, fill='x')

            sb1 = Scrollbar(search_customers_window)
            sb1.pack(side=RIGHT, fill='y')            
            
            frame=Frame(search_customers_window)
            frame.pack(fill=BOTH,expand=True)

            # Entry box label to search for customers
            search_box_label = Label(frame, text='Search :')
            search_box_label.pack(side=LEFT,expand=True)
            # Entry box to search for customers
            search_box = Entry(frame)
            search_box.pack(side=LEFT,expand=True) 


            # Drop down box
            drop = ttk.Combobox(frame,values=['Search by ...','Last Name','Email Address','Customer ID'])
            drop.current(0)
            drop.pack(side=LEFT,expand=True)
            # Entry box search button for customer
            search_button = Button(frame, text='Search Customers', command=search_now) 
            search_button.pack(side=LEFT,pady=40,expand=True) 





            text_box = Text(
                search_customers_window,
               
                wrap=NONE,
                yscrollcommand=sb1.set,
                xscrollcommand=sb.set
            )
            text_box.config(state='disabled')
            text_box.pack(expand = 1, fill = BOTH)


            sb.config(command=text_box.xview)
            sb1.config(command=text_box.yview)

            csv_button = Button(search_customers_window, text='Save to Excel',command=write_to_csv_new)        
            csv_button.pack(side=LEFT,padx=10,expand=True)
        
        # List customers 
        def list_customers():
            list_customer_query = Tk()
            list_customer_query.title('List All Customers')
            list_customer_query.iconbitmap('images/cus.ico')
            list_customer_query.geometry("920x650")

            
           
            sb = Scrollbar(list_customer_query,orient=HORIZONTAL)
            sb.pack(side=BOTTOM, fill='x')

            sb1 = Scrollbar(list_customer_query)
            sb1.pack(side=RIGHT, fill='y')
            text_box = Text(
                list_customer_query,
                height=30,
                wrap=NONE,
                yscrollcommand=sb1.set,
                xscrollcommand=sb.set
            )
            
            text_box.pack(expand = True, fill = BOTH)

            




            sb.config(command=text_box.xview)
            sb1.config(command=text_box.yview)

            
            # Query the database
            my_cursor.execute("SELECT * FROM customers")
            result  = my_cursor.fetchall()
            list = [('First Name','Last Name','Zipcode','Price Paid','User id','Email','Address 1','Address 2','City','State','Country','Phone number','Payment method','Discount code')]
                    
            for i in range(14):
                e = Entry(text_box, width=20, fg='blue',
                    font=('Arial',16))
                text_box.insert(END,' ')
                e.insert(END,list[0][i])
                e.config(state='disabled')
    
                text_box.window_create(END, window=e)
                
            text_box.insert(END,'\n')                           
            for x in result:

                for i in x:
                    e = Entry(text_box, width=20, fg='blue',
                        font=('Arial',16,'bold'))
                    text_box.insert(END,' ')
                    
        
                    e.insert(END,i)
                    e.config(state='disabled')
        
                    text_box.window_create(END, window=e)
            
                text_box.insert(END,'\n')   
            text_box.config(state='disabled')
            
            csv_button = Button(list_customer_query, text='Save to Excel',command=lambda:write_to_csv(result))        
            csv_button.pack(side=LEFT,expand=True)


        # Create a label
        title_label = Label(root, text="Customers Database", font=("Helvatica", 16))
        title_label.grid(row=0,column=0,columnspan=2,pady="10")

        # Create main frame to enter customer data
        first_name_label = Label(root, text="First Name :").grid(row=1,column=0,sticky=W,padx=10)
        last_name_label = Label(root, text="Last Name :").grid(row=2,column=0,sticky=W,padx=10)
        address1_label = Label(root, text="Address 1 :").grid(row=3,column=0,sticky=W,padx=10)
        address2_label = Label(root, text="Address 2 :").grid(row=4,column=0,sticky=W,padx=10)
        city_label = Label(root, text="City :").grid(row=5,column=0,sticky=W,padx=10)
        state_label = Label(root, text="State :").grid(row=6,column=0,sticky=W,padx=10)
        zipcode_label = Label(root, text="Zipcode :").grid(row=7,column=0,sticky=W,padx=10)
        country_label = Label(root, text="Country :").grid(row=8,column=0,sticky=W,padx=10)
        phone_label = Label(root, text="Phone Number :").grid(row=9,column=0,sticky=W,padx=10)
        email_label = Label(root, text="Email Address :").grid(row=10,column=0,sticky=W,padx=10)
        payment_method_label = Label(root, text="Payment Method :").grid(row=11,column=0,sticky=W,padx=10)
        discount_code_label = Label(root, text="Discount Code :").grid(row=12,column=0,sticky=W,padx=10)
        price_paid_label = Label(root, text="Price Paid :").grid(row=13,column=0,sticky=W,padx=10)


        # Create entry boxes
        first_name_box = Entry(root)
        first_name_box.grid(row=1,column=1,pady=5)
        last_name_box = Entry(root)
        last_name_box.grid(row=2,column=1,pady=5)
        address1_box = Entry(root)
        address1_box.grid(row=3,column=1,pady=5)
        address2_box = Entry(root)
        address2_box.grid(row=4,column=1,pady=5)
        city_box = Entry(root)
        city_box.grid(row=5,column=1,pady=5)
        state_box = Entry(root)
        state_box.grid(row=6,column=1,pady=5)
        zipcode_box = Entry(root)
        zipcode_box.grid(row=7,column=1,pady=5)
        country_box = Entry(root)
        country_box.grid(row=8,column=1,pady=5)
        phone_box = Entry(root)
        phone_box.grid(row=9,column=1,pady=5)
        email_box = Entry(root)
        email_box.grid(row=10,column=1,pady=5)
        payment_method_box = Entry(root)
        payment_method_box.grid(row=11,column=1,pady=5)
        discount_code_box = Entry(root)
        discount_code_box.grid(row=12,column=1,pady=5)
        price_paid_box = Entry(root)
        price_paid_box.grid(row=13,column=1,pady=5)

        # create buttons
        add_customer_button = Button(root, text="Add Customer to Database", command=add_customer)
        add_customer_button.grid(row=14,column=0,padx=10,pady=10)

        clear_fields_button= Button(root, text="Clear Fields",command=clear_fields)
        clear_fields_button.grid(row=14,column=1)

        # list customers button 
        list_customers_button = Button(root, text="List Customer", command =list_customers)
        list_customers_button.grid(row=15,column=0,sticky=W,padx=10)

        # Search customers
        search_customers_button = Button(root, text="Search/Edit Customers", command =search_customers)
        search_customers_button.grid(row=15,column=1,sticky=W,padx=10)

        space = Label(root,text='').grid(row=16,column=0)
        space1 = Label(root,text='').grid(row=17,column=1)
        

        help_button = Button(root, text='Help',command=help_user)
        help_button.grid(row=18,column=3)

     
        info_button = Button(root,text='Info',command=info_developer)
        info_button.grid(row=18,column=2)


        # Query the database
        # my_cursor.execute("Select * FROM customers")
        # result= my_cursor.fetchall()
        # for x in result:
        #     print(x)

        root.mainloop()
    
login_window = Tk()
login_window.title('Login to MySQL Database')
login_window.iconbitmap('images/cus.ico')
login_window.geometry("250x150")
login_window.resizable(False,False)


global password_box,username_box
password_box = Entry(login_window,textvariable='password', show='*')
password_box.grid(row=1,column=1,padx=10,pady=10)

password_label = Label(login_window, text='Password :')
password_label.grid(row=1,column=0,padx=10,pady=10)

username_box_text = StringVar()
username_box_text.set("root")

username_box = Entry(login_window,textvariable=username_box_text)

username_box.grid(row=0,column=1,padx=10,pady=10)

username_label = Label(login_window, text='Username :')
username_label.grid(row=0,column=0,padx=10,pady=10)

submit_button = Button(login_window, text='Login',command = login_to_sql)
submit_button.grid(row=2,column=1,padx=10,pady=10)

login_window.mainloop()

















