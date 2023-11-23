from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Stopwatch(models.Model):
    elapsed_time = models.IntegerField(default=0)
    is_running = models.BooleanField(default=False)

class Quote(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f'{self.author} - {self.text}'