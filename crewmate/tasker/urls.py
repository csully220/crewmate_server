from django.urls import path
from .views import TaskList
from . import views

from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'api', TaskViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('alltasks/', TaskList.as_view()),
    ]
urlpatterns += router.urls
