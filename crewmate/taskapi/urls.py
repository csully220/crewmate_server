from django.urls import path
from . import views

from rest_framework import routers
from .views import PlayerTasksViewSet, TasksViewSet, PlayerViewSet

router = routers.DefaultRouter()
router.register('playertasks', PlayerTasksViewSet)
router.register('tasks', TasksViewSet)
router.register('players', PlayerViewSet)

urlpatterns = router.urls
