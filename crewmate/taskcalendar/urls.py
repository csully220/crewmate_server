
from django.urls import path
from . import views

app_name='taskcalendar'
urlpatterns = [ path('', views.index, name='index'),
              ]
