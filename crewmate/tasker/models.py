from django.db import models
from datetime import datetime

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
    created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name


class Task(models.Model):
    assignee = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=60)
    location = models.CharField(max_length=20, default='N/A')

    once = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    biweekly = models.BooleanField(default=False)
    duethiswk = models.BooleanField(default=False)
    monthly = models.BooleanField(default=False)
    quarterly = models.BooleanField(default=False)

    complete = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField()
    updated.auto_now = True
    last_completed = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if self.complete:
            self.last_completed = datetime.now()
        super(Task,self).save(*args, **kwargs)


    def __str__(self):
        return self.desc

