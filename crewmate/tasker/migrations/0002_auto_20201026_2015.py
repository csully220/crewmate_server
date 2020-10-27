# Generated by Django 3.1.2 on 2020-10-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='freq',
            field=models.CharField(choices=[('d', 'daily'), ('w', 'weekly'), ('b', 'biweekly'), ('m', 'monthly'), ('q', 'quarterly')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.CharField(max_length=20),
        ),
    ]
