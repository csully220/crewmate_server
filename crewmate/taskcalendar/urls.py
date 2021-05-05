
from django.urls import path
from . import views

app_name='taskcalendar'
urlpatterns = [ path('', views.index, name='index'),
    path('calendarlist/', views.calendarlist, name='calendarlist'),
    path('calendar/<slug:slug>/', views.calendar, name='calendar'),
    path('month/<slug:slug>/', views.month, name='month'),
    path('week/<slug:slug>/', views.week, name='week'),
    path('day/<slug:slug>/', views.day, name='day'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('uicalendar/<slug:slug>', views.uicalendar, name='uicalendar'),
        ]
