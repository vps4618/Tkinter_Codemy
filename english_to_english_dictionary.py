from email.mime import text
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import requests
import json,os

ws = Tk()
ws.title('English to English Dictionary')
ws.geometry('305x440')
ws.resizable(False,False)
ws.iconbitmap('images/english.ico')

print("*Outputs will show on this window.*")


def get():
    clear = lambda: os.system('cls')
    clear()
    if wordEntry.get()=="":
        messagebox.showerror('empty fields',"Please fill word field.")
    else:
        

        
        
            
        try:

                app_id = "291c736c"
                app_key = "c83cdf52e3e9151b0e97c03d13aad164"
                language = "en-gb"
                word_id = wordEntry.get()
                wordEntry.delete(0,END)
                url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
                r = requests.get(url, headers={"app_id":app_id, "app_key":app_key})
                result=json.loads(r.content)
                
                
                #print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'])
                #print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['definitions'])
                #print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['shortDefinitions'])
                #print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['shortDefinitions'])
                #print(result['results'][0]['lexicalEntries'][1]['phrases'])
                #print(result['results'][0]['lexicalEntries'][0]['phrases'])
                #length=len(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['examples'])
                #for i in range(length):
                #    print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['examples'][i]['text'])
                #list=[1,2,3]
                #print(len(list))
                try:
                    definition=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
                    print("1.Definition : "+definition)
                except:
                    definition='_'
                    print("1.Definition : "+definition)
                try:
                    example=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
                
                    print("  Example : "+example)
                except:
                    example='_'
                    print("  Example : "+example)
                try:
                    shortDefinition=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['shortDefinitions'][0]
                    print("  Short Definition : "+shortDefinition)
                except:
                    shortDefinition='_'
                    print("  Short Definition : "+shortDefinition)
                    
                try:
                    subsensesDefinition=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['definitions'][0]
                    
                    print("  Subsense Definition : "+subsensesDefinition)
                except:
                    subsensesDefinition='_'
                    print("  Subsense Definition : "+subsensesDefinition)
                try:
                    subsensesExample=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['examples'][0]['text']
                    print("  Subsense Examples : "+subsensesExample)
                except:
                    subsensesExample='_'
                    print("  Subsense Examples : "+subsensesExample)
                try:
                    subsensesShortDefinition=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['shortDefinitions'][0]
                    print("  Subsense Short Definition : "+subsensesShortDefinition)
                except:
                    subsensesShortDefinition="_"
                    print("  Subsense Short Definition : "+subsensesShortDefinition)
                try:
                    length=len(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms'])
                    listofsynonyms=[]
                    for i in range(length):
                        synonyms=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms'][i]['text']
                        listofsynonyms.append(synonyms)
                    try:    
                        print("  Synonyms : "+listofsynonyms[0]+","+listofsynonyms[1]+","+listofsynonyms[2]+","+listofsynonyms[3]+","+listofsynonyms[4])    
                    except:
                        try:
                            print("  Synonyms : "+listofsynonyms[0]+","+listofsynonyms[1]+","+listofsynonyms[2]+","+listofsynonyms[3])
                        except:
                            try:
                                print("  Synonyms : "+listofsynonyms[0]+","+listofsynonyms[1]+","+listofsynonyms[2])
                            except:
                                try:
                                    print("  Synonyms : "+listofsynonyms[0]+","+listofsynonyms[1])
                                except:
                                    print("  Synonyms : "+listofsynonyms[0])    


                except:
                    listofsynonyms="_"     
                    print("  Synonyms : "+listofsynonyms)
                try:
                    definition1=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['definitions'][0]
                    print("\n")
                    try:
                        lexicalCategory1=result['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']
                    
                    except:
                        lexicalCategory1=""       
                    
                    print("2.Definition ("+lexicalCategory1+") : "+definition1)
                except:
                    definition1="_"
                    print("\n")    
                    print("2.Definition : "+definition1)
                try:
                    lengthofexampleslist=len(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['examples'])
                    listofexamples=[]
                    for i in range(lengthofexampleslist):
                        examples=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['examples'][i]['text']
                        listofexamples.append(examples)
                    try:    
                        print("  Examples : "+listofexamples[0]+","+listofexamples[1]+","+listofexamples[2]+","+listofexamples[3]+","+listofexamples[4])    
                    except:
                        try:
                            print("  Examples : "+listofexamples[0]+","+listofexamples[1]+","+listofexamples[2]+","+listofexamples[3])
                        except:
                            try:
                                print("  Examples : "+listofexamples[0]+","+listofexamples[1]+","+listofexamples[2])
                            except:
                                try:
                                    print("  Examples : "+listofexamples[0]+","+listofexamples[1])
                                except:
                                    print("  Examples : "+listofexamples[0])                                                    
                except:
                    listofexamples="_"     
                    print("  Examples : "+listofexamples)
                try:
                    shortDefinition1=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['shortDefinitions'][0]
                    print("  Short Definition : "+shortDefinition1)
                except:
                    shortDefinition1="_"    
                    print("  Short Definition : "+shortDefinition1)
                try:
                    length1=len(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['synonyms'])
                    listofsynonyms1=[]
                    for i in range(length1):
                        synonyms1=result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['synonyms'][i]['text']
                        listofsynonyms1.append(synonyms1)
                    try:    
                        print("  Synonyms : "+listofsynonyms1[0]+","+listofsynonyms1[1]+","+listofsynonyms1[2]+","+listofsynonyms1[3]+","+listofsynonyms1[4])    
                    except:
                        try:
                            print("  Synonyms : "+listofsynonyms1[0]+","+listofsynonyms1[1]+","+listofsynonyms1[2]+","+listofsynonyms1[3])
                        except:
                            try:
                                print("  Synonyms : "+listofsynonyms1[0]+","+listofsynonyms1[1]+","+listofsynonyms1[2])
                            except:
                                try:
                                    print("  Synonyms : "+listofsynonyms1[0]+","+listofsynonyms1[1])
                                except:
                                    print("  Synonyms : "+listofsynonyms1[0])                        
                except:
                    listofsynonyms1="_"     
                    print("  Synonyms : "+listofsynonyms1)
                try:
                    lengthofphrases=len(result['results'][0]['lexicalEntries'][0]['phrases'])
                    
                    listofphrases=[]
                    for i in range(lengthofphrases):
                        phrases=result['results'][0]['lexicalEntries'][0]['phrases'][i]['text']
                        listofphrases.append(phrases)
                    try:    
                        print("  Phrases : "+listofphrases[0]+","+listofphrases[1]+","+listofphrases[2]+","+listofphrases[3]+","+listofphrases[4])    
                    except:
                        try:
                            print("  Phrases : "+listofphrases[0]+","+listofphrases[1]+","+listofphrases[2]+","+listofphrases[3])
                        except:
                            try:
                                print("  Phrases : "+listofphrases[0]+","+listofphrases[1]+","+listofphrases[2])
                            except:
                                try:
                                    print("  Phrases : "+listofphrases[0]+","+listofphrases[1])
                                except:
                                    print("  Phrases : "+listofphrases[0])                            
                        
                except:
                    listofphrases="_"     
                    print("  Phrases : "+listofphrases)
                try:
                    definition2=result['results'][0]['lexicalEntries'][1]['entries'][0]['senses'][0]['definitions'][0]
                    print("\n")
                    try:
                        lexicalCategory=result['results'][0]['lexicalEntries'][1]['lexicalCategory']['text']
                    
                    except:
                        lexicalCategory=""       
                    
                    print("3.Definition ("+lexicalCategory+") : "+definition2)
                except:
                    definition2="_"
                    print("\n")    
                    print("3.Definition : "+definition2)
                try:
                    example1=result['results'][0]['lexicalEntries'][1]['entries'][0]['senses'][0]['examples'][0]['text']    
                    print("  Example : "+example1)
                except:
                    example1='_'
                    print("  Example : "+example1)
                try:
                    shortDefinition2=result['results'][0]['lexicalEntries'][1]['entries'][0]['senses'][0]['shortDefinitions'][0]
                    print("  Short Definition : "+shortDefinition2)
                except:
                    shortDefinition2="_"       
                    print("  Short Definition : "+shortDefinition2)
                try:
                    lengthofphrases1=len(result['results'][0]['lexicalEntries'][1]['phrases'])
                    listofphrases1=[]
                    for i in range(lengthofphrases1):
                        phrases1=result['results'][0]['lexicalEntries'][1]['phrases'][i]['text']
                        listofphrases1.append(phrases1)
                    try:    
                        print("  Phrases : "+listofphrases1[0]+","+listofphrases1[1]+","+listofphrases1[2]+","+listofphrases1[3]+","+listofphrases1[4])    
                    except:
                        try:
                            print("  Phrases : "+listofphrases1[0]+","+listofphrases1[1]+","+listofphrases1[2]+","+listofphrases1[3])
                        except:
                            try:
                                print("  Phrases : "+listofphrases1[0]+","+listofphrases1[1]+","+listofphrases1[2])
                            except:
                                try:
                                    print("  Phrases : "+listofphrases1[0]+","+listofphrases1[1])
                                except:
                                    print("  Phrases : "+listofphrases1[0])                            
                        
                except:
                    listofphrases1="_"     
                    print("  Phrases : "+listofphrases1)
                
        except:
                
                message="Error in loading......."
                print(message)


formFrame=LabelFrame(ws,pady=10,padx=10)
formFrame.grid(row=1,column=0,pady=10)

imageFrame=LabelFrame(ws)
imageFrame.grid(row=0,column=0,pady=10,padx=20)

my_img = ImageTk.PhotoImage(Image.open("images/english.png"))
image = Label(imageFrame,image =my_img)
image.grid(row=0,column=0)


wordEntry=Entry(formFrame,font=("helvatica",11))
wordEntry.grid(row=0,column=1)

wordLabel=Label(formFrame,text="Word : ",font=("helvatica",11))
wordLabel.grid(row=0,column=0)

space=Label(formFrame,text="")
space.grid(row=1,column=0)

button=Button(formFrame,text="submit",command=get,font=("helvatica",10))
button.grid(row=2,column=1)

ws.mainloop()