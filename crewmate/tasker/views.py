from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, Player

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TaskSerializer, PlayerSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):

        pk = self.request.GET.get('assignee')
        queryset = Task.objects.all()
        if pk != None:
            queryset = queryset.filter(assignee=pk)
        return queryset

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TaskList(ListView):
    model = Task


def index(request):
    task_list = Task.objects.all()[:5]
    context = {'task_list': task_list}
    return render(request, 'tasker/index.html', context)


