from django.urls import path
from . import views

from rest_framework import routers
from .views import PlayerTasksViewSet, TasksViewSet, PlayerViewSet, CalendarViewSet, PlayerListViewSet, OccurrenceViewSet 

router = routers.DefaultRouter()
router.register('playertasks', PlayerTasksViewSet)
router.register('tasks', TasksViewSet)
router.register('playerlist', PlayerListViewSet)
router.register('player', PlayerViewSet)
router.register('calendar', CalendarViewSet)
router.register('occurrences', OccurrenceViewSet)

urlpatterns = router.urls
