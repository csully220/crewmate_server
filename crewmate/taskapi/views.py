from django.shortcuts import render
from taskcalendar.models import Task, Player

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TaskSerializer, PlayerSerializer

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
