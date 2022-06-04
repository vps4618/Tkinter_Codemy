from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.
def home(request, year, month):
    name='Vishwa'
    month=month.title() #convert to  uppercase
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number=int(month_number)

    return render(request,
    'home.html',{
        'name':name,
        'year':year,
        'month':month,
        'month_number':month_number
        })