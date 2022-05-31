from email.mime import text
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import requests
import json

root1 = Tk()
root1.title('Location details')
root1.iconbitmap('images/world.ico')
root1.geometry("625x630")
root1.resizable(False,False)
global root

def find():
    if latitudeEntry.get()=="" and longitudeEntry.get()=="":
        messagebox.showerror('empty fields',"Please fill latitude and longitude fields")
    elif latitudeEntry.get()=="":
        messagebox.showerror('empty field',"Please fill latitude field")
    elif longitudeEntry.get()=="":
        messagebox.showerror('empty field',"Please fill longitude field")
    else:


        root=Tk()
        root.title('Details')
        root.iconbitmap('images/world.ico')
        root.geometry("355x350")
        root.resizable(False,False)
    
        # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=7655357F-EB0D-4E44-A469-413585CBC7B9
        
        try:
            import requests

            url = "https://geodatasource-geodatasource-location-search-web-service-v1.p.rapidapi.com/city"

            querystring = {"lng":longitudeEntry.get(),"key":"QSYFOGSZYPK224TDYPCSVEHH4IMTPIGK","lat":latitudeEntry.get()}

            headers = {
            'x-rapidapi-host': "geodatasource-geodatasource-location-search-web-service-v1.p.rapidapi.com",
            'x-rapidapi-key': "c89c07abdbmsh786e4e9d290334ap19101bjsn9abf96aff586"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            responejson=json.loads(response.content)
            country = responejson['country']
            region = responejson['region']
            city = responejson['city']
            latitude = responejson['latitude']
            longitude = responejson['longitude']
            currency_code = responejson['currency_code']
            currency_name = responejson['currency_name']
            currency_symbol = responejson['currency_symbol']
            sunrise_time = responejson['sunrise']
            sunset_time = responejson['sunset']
            time_zone = responejson['time_zone']
            distance_km = responejson['distance_km']


        except Exception as e:
            responejson = "Error..."
            error = Label(root, text=responejson).grid(row=0,column=0)
        longitudeEntry.delete(0,END)
        latitudeEntry.delete(0,END)
        country_label = Label(root,text="Country :- "+country,font=('helvatica',12))
        country_label.grid(row=0,column=0,)

        region_label = Label(root,text="Region :- "+region,font=('helvatica',12))
        region_label.grid(row=1,column=0)

        city_label = Label(root,text="City :- "+city,font=('helvatica',12))
        city_label.grid(row=2,column=0)

        latitude_label = Label(root,text="Latitude :- "+latitude,font=('helvatica',12))
        latitude_label.grid(row=3,column=0)

        longitude_label = Label(root,text="Longitude :- "+longitude,font=('helvatica',12))
        longitude_label.grid(row=4,column=0)

        currency_code_label = Label(root,text="Currency code :- "+currency_code,font=('helvatica',12))
        currency_code_label.grid(row=5,column=0)

        currency_name_label = Label(root,text="Currency name :- "+currency_name,font=('helvatica',12))
        currency_name_label.grid(row=6,column=0)

        currency_symbol_label = Label(root,text="Currency symbol :- "+currency_symbol,font=('helvatica',12))
        currency_symbol_label.grid(row=7,column=0)

        sunrise_time_label = Label(root,text="Sunrise time :- "+sunrise_time,font=('helvatica',12))
        sunrise_time_label.grid(row=8,column=0)

        sunset_time_label = Label(root,text="Sunset time :- "+sunset_time,font=('helvatica',12))
        sunset_time_label.grid(row=9,column=0)

        time_zone_label = Label(root,text="Time zone :- "+time_zone,font=('helvatica',12))
        time_zone_label.grid(row=10,column=0)

        distance_km_label = Label(root,text="Distance km :- "+distance_km,font=('helvatica',12))
        distance_km_label.grid(row=11,column=0)

imageFrame =LabelFrame(root1)
imageFrame.grid(row=0,column=0,pady=10,padx=30)
my_img = ImageTk.PhotoImage(Image.open("images/world.png"))
image = Label(imageFrame,image =my_img)
image.grid(row=0,column=0)

formFrame=LabelFrame(root1,padx=70,pady=30)
formFrame.grid(row=1,column=0,pady=20,padx=30)

latitudeLabel=Label(formFrame,text="Latitude : ",font=("helvatica",11))
latitudeLabel.grid(row=0,column=0)

longitudeLabel = Label(formFrame,text="Longitude : ",font=("helvatica",11))
longitudeLabel.grid(row=2,column=0)

space = Label(formFrame,text="")
space.grid(row=1,column=0)

latitudeEntry=Entry(formFrame,width=20,font=("helvatica",11))
latitudeEntry.grid(row=0,column=1)

longitudeEntry=Entry(formFrame,width=20,font=("helvatica",11))
longitudeEntry.grid(row=2,column=1)

submitButton = Button(formFrame,text="submit",font=("helvatica",10),command=find)
submitButton.grid(row=4,column=1)

space1 = Label(formFrame,text="")
space1.grid(row=3,column=0)

instructionFrame=LabelFrame(root1,padx=30,pady=20)
instructionFrame.grid(row=3,column=0,padx=20)

head=Label(instructionFrame,text="Instructions",font=("helvatica 12 bold"))
head.grid(row=0,column=0,columnspan=2)

instruction1=Label(instructionFrame,text="1.This application needs internet connection.",font=("helvatica",11))
instruction2=Label(instructionFrame,text="2.Format of latitude & longitude fields - Latitude : 39.9042 | Longitude : 116.4074",font=("helvatica",11))
instruction1.grid(row=1,column=0)
instruction2.grid(row=2,column=0)
root1.mainloop()
