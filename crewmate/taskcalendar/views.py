from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'taskcalendar/index.html')

def month(request):
    return render(request, 'taskcalendar/month.html')
