from django.contrib import admin
from .models import Task, Player 

# Register your models here.
#class TaskAdmin(admin.ModelAdmin):
#    readonly_fields = []

admin.site.register(Task)
admin.site.register(Player)
