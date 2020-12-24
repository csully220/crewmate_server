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

    def __str__(self):
        return self.name


class Task(models.Model):
    assignee = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(schedule.models.Event, on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=60)
    LOCATIONS = [('livingroom', 'Living Room'),
                 ('kitchen', 'Kitchen'),
                 ('mstr_bed', 'Master Bedroom'),
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

    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    last_completed = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.complete:
            self.last_completed = django.utils.timezone.now()
        return super(Task,self).save(*args, **kwargs)

    def __str__(self):
        return self.desc

