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
    created = models.DateTimeField(default=django.utils.timezone.now)

    def get_tasks(self):
        tasks = Task.objects.all().filter(assignee=self)
        print(tasks)
        return tasks

    def __str__(self):
        return self.name


class Task(models.Model):
    assignee = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(schedule.models.Event, on_delete=models.SET_NULL, null=True)
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


    RRULES = [('daily','Every day'),
              ('weekday','Every weekday'),
              ('weekly','Weekly'),
              ('weekend','Weekends'),
              ('eoweekend','Every other weekend'),
              ('monthly','Monthly'),
              ('0','Mondays'),
              ('1','Tuesdays'),
              ('2','Wednesdays'),
              ('3','Thursdays'),
              ('4','Fridays'),
              ('5','Saturdays'),
              ('6','Sundays'),
              ('once','Once'),]

    schedule = models.CharField(max_length=30, choices=RRULES, default='weekly')
    #once = models.BooleanField(default=False)
    #monday = models.BooleanField(default=False)
    #tuesday = models.BooleanField(default=False)
    #wednesday = models.BooleanField(default=False)
    #thursday = models.BooleanField(default=False)
    #friday = models.BooleanField(default=False)
    #saturday = models.BooleanField(default=False)
    #sunday = models.BooleanField(default=False)
    #biweekly = models.BooleanField(default=False)
    #duethiswk = models.BooleanField(default=False)
    #monthly = models.BooleanField(default=False)
    #quarterly = models.BooleanField(default=False)


    def __str__(self):
        return self.event.title

