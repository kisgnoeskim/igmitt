from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Stopwatch(models.Model):
    is_running = models.BooleanField(default=False)
    elapsed_time = models.PositiveIntegerField(default=0)