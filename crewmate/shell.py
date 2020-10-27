from tasker.models import Task
from django.utils import timezone
t = Task(created=timezone.now(),freq='d',desc='Seomthing here')

