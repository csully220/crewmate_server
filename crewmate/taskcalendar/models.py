from django.db import models
from datetime import datetime, timezone
import django.utils.timezone
import schedule

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=15)
    COLORS = [('blue','Blue'),
              ('black','Black'),
              ('white','White'),
              ('yellow','Yellow'),
              ('orange','Orange'),
              ('pink','Pink'),
              ('red','Red'),
              ('purple','Purple'),
              ('brown','Brown'),
              ('green','Green'),
              ('cyan','Cyan'),
              ('lime','Lime'),]
    color = models.CharField(max_length=20, choices=COLORS, default='wht')
    calendar = models.ForeignKey('schedule.Calendar', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(default=django.utils.timezone.now)

    account_balance = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def get_tasks(self):
        tasks = Task.objects.all().filter(assignee=self)
        print(tasks)
        return tasks

    def __str__(self):
        return self.name


class Task(schedule.models.Event):
    assignee = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    #event = models.ForeignKey(schedule.models.Event, on_delete=models.SET_NULL, null=True)
    LOCATIONS = [('livingroom', 'Living Room'),
                 ('kitchen', 'Kitchen'),
                 ('masterbed', 'Master Bedroom'),
                 ('masterbath', 'Master Bath'),
                 ('bed1', 'Bedroom 1'),
                 ('bed2', 'Bedroom 2'),
                 ('guestbath', 'Guest Bath'),
                 ('bonusroom', 'Bonus Room'),
                 ('garage', 'Garage'),
                 ('attic', 'Attic'),
                 ('frontyard', 'Front Yard'),
                 ('backyard', 'Back Yard'),
                 ('other', 'Other'),
                 ('na', 'N/A'),]

    location = models.CharField(max_length=30, choices=LOCATIONS, default='livingroom')

    def __str__(self):
        return self.title

