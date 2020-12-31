from django.shortcuts import render
from django.shortcuts import redirect
from schedule.models import Calendar
from schedule.models import Event

# Create your views here.

def index(request):
    calendar_list = Calendar.objects.all()
    return render(request, 'taskcalendar/calendars.html')
    #return render(request, 'taskcalendar/index.html')

def month(request):
    return render(request, 'taskcalendar/month.html')

def calendars(request):
    calendar_list = Calendar.objects.all()
    context = {'calendar_list': calendar_list}
    return render(request, 'taskcalendar/calendars.html', context)

def calendar(request, slug):
    calendar = Calendar.objects.get(slug=slug)
    events = Event.objects.filter(calendar=calendar)
    print(events)
    context = {'calendar': calendar, 'events':events}
    return render(request, 'taskcalendar/calendar.html', context)

