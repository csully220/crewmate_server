from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

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
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Task(models.Model):
    assignee = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=60)
    location = models.CharField(max_length=20, default='Kitchen')
    recurring = models.BooleanField(default=True)
    FREQUENCIES = [ ('o','once'),
                    ('d','daily'),
                    ('w','weekly'),
                    ('b','biweekly'), 
                    ('m','monthly'),
                    ('q','quarterly') ]
    freq_def = 'd'
    if recurring == False:
        freq_def = 'o'
    
    freq = models.CharField(max_length=20, choices=FREQUENCIES, default=freq_def)
    deadline = models.DateTimeField(blank=True,null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.deadline = timezone.now
        td = timedelta(days=0)
        if self.freq == 'd':
            td = timedelta(days=0)
            self.deadline = self.created + td
        elif self.freq == 'w':
            today = self.created.weekday()
            daystilsunday = 6 - today
            td = timedelta(days=daystilsunday)
            self.deadline = self.created + td
        elif self.freq == 'b':
            td = timedelta(days=4)
            self.deadline = self.created + td
        elif self.freq == 'm':
            td = timedelta(days=5)
            self.deadline = self.created + td
        elif self.freq == 'q':
            td = timedelta(days=6)
            self.deadline = self.created + td
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.desc

