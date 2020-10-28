from django.urls import path
from .views import TaskList
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alltasks/', TaskList.as_view()),
    ]
