# Generated by Django 4.2.7 on 2023-11-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_remove_stopwatch_is_running_stopwatch_start_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stopwatch',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='stopwatch',
            name='elapsed_time',
            field=models.IntegerField(default=0),
        ),
    ]
