from django.contrib import admin
from .models import Task, Player

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
        readonly_fields = ['last_completed']


admin.site.register(Task, TaskAdmin)
admin.site.register(Player)
