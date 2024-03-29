from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name='Vishwa'
    month=month.title() #convert to  uppercase
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number=int(month_number)

    # create a calendar
    cal=HTMLCalendar().formatmonth(year, month_number)

    # get current year
    now1=datetime.now()
    current_year=now1.year

    # get current time
    time =now1.strftime('%I:%M %p')


    
    return render(request,
    'events/home.html',{
        'name':name,
        'year':year,
        'month':month,
        'month_number':month_number,
        'cal':cal,
        'current_year':current_year,
        'time':time,
       
        })