from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

from rest_framework import viewsets
from .serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskList(ListView):
    model = Task


def index(request):
    task_list = Task.objects.all()[:5]
    context = {'task_list': task_list}
    return render(request, 'tasker/index.html', context)


