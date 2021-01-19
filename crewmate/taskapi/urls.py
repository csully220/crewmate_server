from django.urls import path
from . import views

from rest_framework import routers
from .views import PlayerTasksViewSet, TasksViewSet, PlayerViewSet, CalendarViewSet

router = routers.DefaultRouter()
router.register('playertasks', PlayerTasksViewSet)
router.register('tasks', TasksViewSet)
router.register('players', PlayerViewSet)
router.register('calendar', CalendarViewSet)

urlpatterns = router.urls
