# Generated by Django 4.2.7 on 2023-11-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_stopwatch_delete_timer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stopwatch',
            name='is_running',
        ),
        migrations.AddField(
            model_name='stopwatch',
            name='start_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='stopwatch',
            name='elapsed_time',
            field=models.FloatField(default=0.0),
        ),
    ]
