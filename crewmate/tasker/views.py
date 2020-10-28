from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task


def index(request):
    task_list = Task.objects.all()[:5]
    context = {'task_list': task_list}
    return render(request, 'tasker/index.html', context)
