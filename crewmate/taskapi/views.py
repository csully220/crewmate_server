from django.shortcuts import render
from taskcalendar.models import Task, Player
from schedule.models import Calendar, Occurrence

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TaskSerializer, PlayerSerializer, OccurrenceSerializer, CalendarSerializer

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

class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

    def list(self, request):
        pk = self.request.GET.get('id')
        queryset = Calendar.objects.all()
        if pk != None:
            queryset = queryset.filter(id=pk)
        serializer = CalendarSerializer(queryset, many=True)
        return Response(serializer.data)

