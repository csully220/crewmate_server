from django.urls import path
from .views import TaskList
from . import views

from rest_framework import routers
from .views import TaskViewSet, PlayerViewSet

router = routers.DefaultRouter()
router.register(r'api/tasks', TaskViewSet)
router.register(r'api/players', PlayerViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('alltasks/', TaskList.as_view()),
    ]
urlpatterns += router.urls
