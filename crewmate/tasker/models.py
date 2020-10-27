from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class Task(models.Model):
    created = models.DateTimeField(default=timezone.now())
    desc = models.CharField(max_length=60)
    freq_choices = [('d','daily'),
                    ('w','weekly'),
                    ('b','biweekly'), 
                    ('m','monthly'),
                    ('q','quarterly')]
    freq = models.CharField(max_length=20, choices=freq_choices, default='d')

    deadline = models.DateTimeField(blank=True,null=True)

    def save(self, *args, **kwargs):
        self.deadline = timezone.now()
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
