from tkinter import *
from unicodedata import category
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Air Quality app')
root.iconbitmap('images/air.ico')
root.geometry("600x100")

def ziplookup():
    
  
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=7655357F-EB0D-4E44-A469-413585CBC7B9

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip.get()+"&distance=25&API_KEY=7655357F-EB0D-4E44-A469-413585CBC7B9")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        if category=="Good":
            weather_color = "#0C0"
        elif category=="Moderate":
            weather_color = "#FFFF00"
        elif category=="Unhealthy for Sensitive Groups":
            weather_color = "#FF9900"
        elif category=="Unhealthy":
            weather_color = "#FF0000"
        elif category=="Very Unhealthy":
            weather_color = "#990066"
        elif category=="Hazardous":
            weather_color = "#660000"
        root.configure(background=weather_color)    
        global myLabel
        myLabel = Label(root,text=city+" Air Quality "+str(quality)+" "+category,font=("helvatica",20),bg=weather_color)
        myLabel.grid(row=1,column=0,columnspan=2)
    except Exception as e:
        api = "Error..."
        myLabel = Label(root,text=api)
        myLabel.grid(row=1,column=0,columnspan=2)


zip = Entry(root)
zip.grid(row=0,column=0,stick=W+E+N+S)

zip_button=Button(root,text="Lookup Zipcode",command=ziplookup)
zip_button.grid(row=0,column=1,stick=W+E+N+S)
root.mainloop()