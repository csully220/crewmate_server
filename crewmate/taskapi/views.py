from django.shortcuts import render
from taskcalendar.models import Task, Player
from schedule.models import Calendar, Occurrence
from schedule.periods import Period, Week, Day, Month
import datetime

from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TaskSerializer, PlayerSerializer, OccurrenceSerializer, CalendarSerializer

# Create your views here.

#def updateOccurrence(request):

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

class PlayerListViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        playerid = self.request.GET.get('playerid')
        p = Player.objects.get(id=playerid)
        c = p.calendar
        events = Task.objects.filter(calendar=c)

        now = datetime.datetime.now(datetime.timezone.utc)
        period = self.request.GET.get('period')

        p = None
        if period == 'day':
            p = Day(events, now)
        if period == 'week':
            p = Week(events, now)
        queryset = p.get_occurrences()
        serializer = OccurrenceSerializer(queryset, many=True)
        return Response(serializer.data)

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

    def list(self, request):
        slug = self.request.GET.get('slug')
        queryset = Calendar.objects.all()
        if slug != None:
            queryset = queryset.filter(slug=slug)
        serializer = CalendarSerializer(queryset, many=True)
        return Response(serializer.data)

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def list(self, request):
        pk = self.request.GET.get('id')
        queryset = Calendar.objects.all()
        if pk != None:
            queryset = queryset.filter(id=pk)
        serializer = CalendarSerializer(queryset, many=True)
        return Response(serializer.data)

