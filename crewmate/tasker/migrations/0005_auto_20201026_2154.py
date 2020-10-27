# Generated by Django 3.1.2 on 2020-10-27 02:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0004_auto_20201026_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 2, 54, 51, 57016, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='task',
            name='freq',
            field=models.CharField(choices=[('d', 'daily'), ('w', 'weekly'), ('b', 'biweekly'), ('m', 'monthly'), ('q', 'quarterly')], default='d', max_length=20),
        ),
    ]
