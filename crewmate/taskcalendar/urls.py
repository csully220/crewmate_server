
from django.urls import path
from . import views

app_name='taskcalendar'
urlpatterns = [ path('', views.index, name='index'),
        path('calendars/', views.calendars, name='calendars'),
        path('calendar/<slug:slug>/', views.calendar, name='calendar'),
              ]
