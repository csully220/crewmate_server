from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, Player
from django.contrib.auth.models import User

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TaskSerializer, PlayerSerializer

# use for debugging, remove later
from django.http import HttpResponse

# Create your views here.
class PlayerTasksViewSet(viewsets.ViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        pk = self.request.GET.get('assignee')
        queryset = Task.objects.all()
        if pk != None:
            queryset = queryset.filter(assignee=pk)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TaskList(ListView):
    model = Task

def index(request):
    task_list = Task.objects.all()[:5]
    context = {'task_list': task_list}
    return render(request, 'tasker/index.html', context)


