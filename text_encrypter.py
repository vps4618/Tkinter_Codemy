from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
from tkhtmlview import HTMLLabel
root=Tk()
root.title('Text Encrypter')
root.iconbitmap('images/encrypt.ico')

# info function
def info():
    info_window = Toplevel()
    info_window.title('Info')
    info_window.iconbitmap('images/encrypt.ico')
    info_window.geometry("200x300")
    info_window.resizable(False,False)
    html_details = HTMLLabel(info_window,html="""<p>Coded by Vishwa Praveen(Vpsoftwares).</p><br><center><img src='images/logo.jpg'></center><br><br><a href='https://vpsoftwares.herokuapp.com/'>Visit developer's website</a>""")
    html_details.pack()

# decryption function

def decrypt_text_function():

    # create clear entries  function
    def clear_entries_decrypt():
        if text_box_decrypt.get("1.0","end-1c")==""  and text_box_encrypt.get("1.0","end-1c")=="" and text_box_key_decrypt.get("1.0","end-1c")=="":
            messagebox.showerror('clearing error','Entries are empty !')
        else:
            text_box_key_decrypt.delete("1.0","end-1c")
            text_box_encrypt.delete("1.0","end-1c")
            text_box_decrypt.delete("1.0","end-1c")
            messagebox.showinfo("clear","Entries  cleared successfully !")
            
    #  create copy decrypted  text function
    def copy_decrypted_text():
        if  text_box_decrypt.get("1.0","end-1c")!="":
            decrypt_window.clipboard_clear()
            decrypt_window.clipboard_append(text_box_decrypt.get("1.0","end-1c"))
            messagebox.showinfo('Copy','Decrypted  text successfully copied to clipboard !')
        else:
            messagebox.showerror('copy error','Decrypted Text field is empty !')
 

    #  create real decryption  function
    def decryption_with_fernet():
        if text_box_key_decrypt.get("1.0", "end-1c") != "" and text_box_encrypt.get("1.0", "end-1c") != "":
            try:
                text_box_decrypt.delete("1.0","end-1c")
                
                key = text_box_key_decrypt.get("1.0", "end-1c")
                contents_decrypted=Fernet(key).decrypt(bytes(text_box_encrypt.get("1.0", "end-1c"),'utf-8'))
                text_box_decrypt.insert(END,contents_decrypted)
                       
            except:
                text_box_decrypt.delete("1.0","end-1c")
                text_box_decrypt.insert(END,"error")      
        else:
            messagebox.showerror('decryption error','Encrypted Text Feild and Key Fields are empty !') 

    # window  details
    decrypt_window=Toplevel()
    decrypt_window.title('Decrypt window')
    decrypt_window.iconbitmap('images/encrypt.ico')
   
    # creating encrypted  text box label
    encrypted_text_label=Label(decrypt_window,text='Encrypted Text :',font='Helvatica 13')
    encrypted_text_label.grid(row=0,column=0,padx=20,pady=10)

    # second frame for text  box for ecrypted  text
    frame_encrypt=Frame(decrypt_window,height=5,width=10)
    frame_encrypt.grid(row=0,column=1,padx=10,pady=10)
    
    # secong scrollbar
    sb_encrypt = Scrollbar(frame_encrypt,orient=HORIZONTAL)
    sb_encrypt.pack(side=BOTTOM, fill='x')

    sb1_encrypt = Scrollbar(frame_encrypt)
    sb1_encrypt.pack(side=RIGHT, fill='y')
    
    #  text for encrypted text
    text_box_encrypt = Text(
        frame_encrypt,
        height=5,
        wrap=NONE,
        yscrollcommand=sb1_encrypt.set,
        xscrollcommand=sb_encrypt.set,
        font='Courier 12'
    )
    
    text_box_encrypt.pack(expand = True, fill = BOTH)

    sb_encrypt.config(command=text_box_encrypt.xview)
    sb1_encrypt.config(command=text_box_encrypt.yview)
    
    # key  label
    key_label=Label(decrypt_window,text='Key :',font='Helvatica 13')
    key_label.grid(row=1,column=0,padx=20,pady=10)

    # frame  for key text box
    frame_key_decrypt=Frame(decrypt_window,height=1,width=10)
    frame_key_decrypt.grid(row=1,column=1,padx=10,pady=10)
    
    # key scrollbar
    sb_key_decrypt = Scrollbar(frame_key_decrypt,orient=HORIZONTAL)
    sb_key_decrypt.pack(side=BOTTOM, fill='x')

    sb1_key_decrypt = Scrollbar(frame_key_decrypt)
    sb1_key_decrypt.pack(side=RIGHT, fill='y')
    
    #  text box  for key
    text_box_key_decrypt = Text(
        frame_key_decrypt,
        height=1,
        wrap=NONE,
        yscrollcommand=sb1_key_decrypt.set,
        xscrollcommand=sb_key_decrypt.set,
        font='Courier 12'
    )
    
    text_box_key_decrypt.pack(expand = True, fill = BOTH)

    sb_key_decrypt.config(command=text_box_key_decrypt.xview)
    sb1_key_decrypt.config(command=text_box_key_decrypt.yview)

    #  creating decrypting button
    decryting_button=Button(decrypt_window,text='Decrypt Text',font='Fixedsys 11',bg='#9daee0',command=decryption_with_fernet)
    decryting_button.grid(row=2,column=1)

    # decrypted text  label
    decrypted_text_label=Label(decrypt_window,text='Decrypted Text :',font='Helvatica 13')
    decrypted_text_label.grid(row=3,column=0,padx=20,pady=10)
    
    # first frame
    frame_decrypt=Frame(decrypt_window,height=5,width=10)
    frame_decrypt.grid(row=3,column=1,padx=10,pady=10)
    
    # first scrollbar  for  input text box
    sb_decrypt = Scrollbar(frame_decrypt,orient=HORIZONTAL)
    sb_decrypt.pack(side=BOTTOM, fill='x')

    sb1_decrypt = Scrollbar(frame_decrypt)
    sb1_decrypt.pack(side=RIGHT, fill='y')
    
    # text box for input text
    text_box_decrypt = Text(
        frame_decrypt,
        height=5,
        wrap=NONE,
        yscrollcommand=sb1_decrypt.set,
        xscrollcommand=sb_decrypt.set,
        font='Courier 12'
    )
    
    text_box_decrypt.pack(expand = True, fill = BOTH)

    sb_decrypt.config(command=text_box_decrypt.xview)
    sb1_decrypt.config(command=text_box_decrypt.yview)    

    # copy button to copy decrypted text
    copy_decrypted_text_button=Button(decrypt_window,text='Copy Decrypted Text',font='Fixedsys 11',bg='#c7b6d9',command=copy_decrypted_text)
    copy_decrypted_text_button.grid(row=4,column=1,pady=5)

    
    # clear entries button
    clear_entries_decrypt_button=Button(decrypt_window,text="Clear Entries",font='Fixedsys 11',bg='#e0ba9d',command=clear_entries_decrypt)
    clear_entries_decrypt_button.grid(row=5,column=1)

    # space  new 
    space2=Label(decrypt_window,text="").grid(row=8,column=0)

#  encryption fuction
def encrypt_text_function():

    # create clear entries  function
    def clear_entries():
        if text_box.get("1.0","end-1c")==""  and text_box_new.get("1.0","end-1c")=="" and text_box_key.get("1.0","end-1c")=="":
            messagebox.showerror('clearing error','Entries are empty !')
        else:
            text_box.delete("1.0","end-1c")
            text_box_key.delete("1.0","end-1c")
            text_box_new.delete("1.0","end-1c")
            messagebox.showinfo("clear","Entries  cleared successfully !")
            
    #  create copy encrypted  text function
    def copy_encrypted_text():
        if  text_box_new.get("1.0","end-1c")!="":
            encrypt_window.clipboard_clear()
            encrypt_window.clipboard_append(text_box_new.get("1.0","end-1c"))
            messagebox.showinfo('Copy','Encrypted  text successfully copied to clipboard !')
        else:
            messagebox.showerror('copy error','Encrypted Text field is empty !')
 
    #  create copy text function
    def copy_key():
        if  text_box_key.get("1.0","end-1c")!="":
            encrypt_window.clipboard_clear()
            encrypt_window.clipboard_append(text_box_key.get("1.0","end-1c"))
            messagebox.showinfo('Copy','Key successfully copied to clipboard !')
        else:
            messagebox.showerror('copy error','Key field is empty !')

    # create real encryption function
    def encryption_with_fernet():
       
        if text_box.get("1.0", "end-1c") != "":
            try:
                text_box_new.delete("1.0","end-1c")
                text_box_key.delete("1.0","end-1c")
                key = Fernet.generate_key()
                contents_encrypted=Fernet(key).encrypt(bytes(text_box.get("1.0", "end-1c"),'utf-8'))
                text_box_new.insert(END,contents_encrypted)
                text_box_key.insert(END,key)  
                       
            except:
                text_box_new.delete("1.0","end-1c")
                text_box_key.delete("1.0","end-1c")    
                text_box_new.insert(END,'error')
                text_box_key.insert(END,"error")      
        else:
            messagebox.showerror('encryption error','Input Text Feild is empty !') 
    # window  details
    encrypt_window=Toplevel()
    encrypt_window.title('Encrypt window')
    encrypt_window.iconbitmap('images/encrypt.ico')
   

    # input  label
    input_text_label=Label(encrypt_window,text='Input Text :',font='Helvatica 13')
    input_text_label.grid(row=0,column=0,padx=20,pady=10)
    
    # first frame
    frame=Frame(encrypt_window,height=5,width=10)
    frame.grid(row=0,column=1,padx=10,pady=10)
    
    # first scrollbar  for  input text box
    sb = Scrollbar(frame,orient=HORIZONTAL)
    sb.pack(side=BOTTOM, fill='x')

    sb1 = Scrollbar(frame)
    sb1.pack(side=RIGHT, fill='y')
    
    # text box for input text
    text_box = Text(
        frame,
        height=5,
        wrap=NONE,
        yscrollcommand=sb1.set,
        xscrollcommand=sb.set,
        font='Courier 12'
    )
    
    text_box.pack(expand = True, fill = BOTH)

    sb.config(command=text_box.xview)
    sb1.config(command=text_box.yview)

    # assign space
    space =Label(encrypt_window,text='')
    space.grid(row=1,column=0)
    
    #  creating encrypting button
    encryting_button=Button(encrypt_window,text='Encrypt Text',font='Fixedsys 11',bg='#e09da6',command=encryption_with_fernet)
    encryting_button.grid(row=1,column=1)

    # creating encrypted  text box label
    encrypted_text_label=Label(encrypt_window,text='Encrypted Text :',font='Helvatica 13')
    encrypted_text_label.grid(row=2,column=0,padx=20,pady=10)

    # second frame for text  box for ecrypted  text
    frame1=Frame(encrypt_window,height=5,width=10)
    frame1.grid(row=2,column=1,padx=10,pady=10)
    
    # secong scrollbar
    sb_new = Scrollbar(frame1,orient=HORIZONTAL)
    sb_new.pack(side=BOTTOM, fill='x')

    sb1_new = Scrollbar(frame1)
    sb1_new.pack(side=RIGHT, fill='y')
    
    #  text for encrypted text
    text_box_new = Text(
        frame1,
        height=5,
        wrap=NONE,
        yscrollcommand=sb1_new.set,
        xscrollcommand=sb_new.set,
        font='Courier 12'
    )
    
    text_box_new.pack(expand = True, fill = BOTH)

    sb_new.config(command=text_box_new.xview)
    sb1_new.config(command=text_box_new.yview)

    # key  label
    key_label=Label(encrypt_window,text='Key :',font='Helvatica 13')
    key_label.grid(row=3,column=0,padx=20,pady=10)

    # frame  for key text box
    frame_key=Frame(encrypt_window,height=1,width=10)
    frame_key.grid(row=3,column=1,padx=10,pady=10)
    
    # key scrollbar
    sb_key = Scrollbar(frame_key,orient=HORIZONTAL)
    sb_key.pack(side=BOTTOM, fill='x')

    sb1_key = Scrollbar(frame_key)
    sb1_key.pack(side=RIGHT, fill='y')
    
    #  text box  for key
    text_box_key = Text(
        frame_key,
        height=1,
        wrap=NONE,
        yscrollcommand=sb1_key.set,
        xscrollcommand=sb_key.set,
        font='Courier 12'
    )
    
    text_box_key.pack(expand = True, fill = BOTH)

    sb_key.config(command=text_box_key.xview)
    sb1_key.config(command=text_box_key.yview)

    # copy button to copy encrypted text
    copy_encrypted_text_button=Button(encrypt_window,text='Copy Encrypted Text',font='Fixedsys 11',bg='#c7b6d9',command=copy_encrypted_text)
    copy_encrypted_text_button.grid(row=4,column=1,pady=5)

    # copy button to copy key
    copy_key_button=Button(encrypt_window,text='Copy Key',font='Fixedsys 11',bg='#b6d9bc',command=copy_key)
    copy_key_button.grid(row=5,column=1,pady=10)

    # clear entries button
    clear_entries_button=Button(encrypt_window,text="Clear Entries",font='Fixedsys 11',bg='#e0ba9d',command=clear_entries)
    clear_entries_button.grid(row=7,column=1)

    # space  new 
    space2=Label(encrypt_window,text="").grid(row=8,column=0)

# encrypt button
encryption_window_button = Button(root,text="Encrypt Text",bg='#ed8a8a',font='Helvatica 15',command=encrypt_text_function)
encryption_window_button.pack(expand=1,ipady=30,ipadx=50,padx=20,pady=20,fill='x')

# decrypt button
decryption_window_button = Button(root,text="Decrypt Text",bg='#34a4eb',font='Helvatica 15',command=decrypt_text_function)
decryption_window_button.pack(expand=1,ipady=30,ipadx=50,padx=20,pady=20,fill=X)

# info button
info_window_button = Button(root,text="Info",font='Helvatica 10',command=info)
info_window_button.pack(padx=20,pady=20)

root.mainloop()