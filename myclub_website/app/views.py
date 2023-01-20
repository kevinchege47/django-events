from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request,year,month):
    name = "John"
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #Create Calendar
    cal = HTMLCalendar().formatmonth(year,month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')
    context={"name":name,"year":year,"month":month,"cal":cal,"current_year":current_year,"time":time}
    return render(request,'home.html',context)
# Create your views here.
