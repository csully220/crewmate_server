from django.shortcuts import render
from django.shortcuts import redirect
#import django.utils.timezone
from schedule.models import Calendar, Event
from taskcalendar.models import Task
from schedule.periods import Period, Month, Week, Day
import datetime

# Create your views here.

def index(request):
    calendar_list = Calendar.objects.all()
    return render(request, 'taskcalendar/calendars.html')
    #return render(request, 'taskcalendar/index.html')

def calendarlist(request):
    calendar_list = Calendar.objects.all()
    context = {'calendar_list': calendar_list}
    return render(request, 'taskcalendar/calendars.html', context)

def calendar(request, slug):
    calendar = Calendar.objects.get(slug=slug)
    events = Task.objects.filter(calendar=calendar)
    tz = datetime.timezone.now(tz='UTC')
    period = Period(datetime.datetime.now(tz=tz))
    print(events)
    context = {'calendar': calendar, 'events':events}
    return render(request, 'taskcalendar/calendar.html', context)

def month(request, slug):
    c = Calendar.objects.get(slug=slug)
    ev = Task.objects.filter(calendar=c)
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    p = Month(ev, now)
    oc = p.get_occurrences()
    context = {'calendar': c, 'occurrences':oc, 'period':p}
    return render(request, 'taskcalendar/month.html', context)

def week(request, slug):
    c= Calendar.objects.get(slug=slug)
    ev= Task.objects.filter(calendar=c)
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    p = Week(ev, now)
    oc = p.get_occurrences()
    context = {'calendar': c, 'occurrences':oc, 'period':p}
    return render(request, 'taskcalendar/week.html', context)

def day(request, slug):
    c= Calendar.objects.get(slug=slug)
    ev= Task.objects.filter(calendar=c)
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    p = Day(ev, now)
    oc = p.get_occurrences()
    context = {'calendar': c, 'occurrences':oc, 'period':p}
    return render(request, 'taskcalendar/day.html', context)

def tasklist(request):
    tasks = Task.objects.all()
    context = {'tasks' : tasks}
    return render(request, 'taskcalendar/tasklist.html', context)

def uicalendar(request, slug):
    c= Calendar.objects.get(slug=slug)
    ev = Task.objects.filter(calendar=c)
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    p = Month(ev, now)
    oc = p.get_occurrences()
    context = {'calendar': c, 'occurrences':oc, 'period':p}
    return render(request, 'taskcalendar/UICalendar.html', context)


