from django.urls import path
from .views import TaskList
from . import views

from rest_framework import routers
from .views import PlayerTasksViewSet, TasksViewSet, PlayerViewSet

router = routers.DefaultRouter()
router.register('api/playertasks', PlayerTasksViewSet)
router.register('api/tasks', TasksViewSet)
router.register('api/players', PlayerViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', TaskList.as_view()),
    ]
urlpatterns += router.urls
