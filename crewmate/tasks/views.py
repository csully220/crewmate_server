from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, Player
from django.contrib.auth.models import User

# use for debugging, remove later
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html')


def task_list(request):
    task_list = Task.objects.order_by('assignee')
    #task_list = Task.objects.all()
    players = []
    prev_plyrname = ' '
    for t in task_list:
        if t.assignee.name != prev_plyrname:
            prev_plyrname = t.assignee.name
            players.append(t.assignee)

    context = {'task_list': task_list, 'players':players}
    
    return render(request, 'tasks/task_list.html', context)
