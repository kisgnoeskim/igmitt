from django.shortcuts import redirect, render
from .models import Task
from django.views import View
from django.http import JsonResponse
from .models import Stopwatch

def index(request):
    return render(request, 'todo/task_list.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('todolist:task_list')
    return render(request, 'todo/add_task.html')

def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('todolist:task_list')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist:task_list')

class StopwatchView(View):
    template_name = 'todo/task_list.html'

    def get(self, request):
        stopwatch, created = Stopwatch.objects.get_or_create(pk=1)
        return render(request, self.template_name, {'stopwatch': stopwatch})

    def post(self, request):
        stopwatch = Stopwatch.objects.get(pk=1)

        if request.POST.get('action') == 'start':
            stopwatch.is_running = True
            stopwatch.save()

        elif request.POST.get('action') == 'stop':
            stopwatch.is_running = False
            stopwatch.save()

        elif request.POST.get('action') == 'reset':
            stopwatch.is_running = False
            stopwatch.elapsed_time = 0
            stopwatch.save()

        elif request.POST.get('action') == 'update':
            if stopwatch.is_running:
                stopwatch.elapsed_time += 1
                stopwatch.save()

        return JsonResponse({'elapsed_time': stopwatch.elapsed_time, 'is_running': stopwatch.is_running})