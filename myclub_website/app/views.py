from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import *
from .forms import VenueForm
from django.http import HttpResponseRedirect

def show_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    context = {"venue":venue}
    return render(request,'app/show_venue.html',context)
    


def list_venues(request):
    venue_list = Venue.objects.all
    context = {"venue_list":venue_list}
    return render(request,'app/venue.html',context)


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted=True

    form = VenueForm
    context = {"form":form,"submitted":submitted}

    return render(request,'app/add_venue.html',context)



def all_events(request):
    event_list = Event.objects.all
    
    context = {"event_list":event_list}
    return render(request,'app/events_list.html',context)

def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    name = "John"
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #Create Calendar
    cal = HTMLCalendar().formatmonth(year,month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M: %p')
    context={"name":name,"year":year,"month":month,"cal":cal,"current_year":current_year,"time":time}
    return render(request,'app/home.html',context)


# Create your views here.
