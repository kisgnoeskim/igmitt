from django.shortcuts import redirect, render
from .models import Quote, Task
from django.views import View
from django.http import JsonResponse
from .models import Stopwatch
from django.utils import timezone
import time


def index(request):
    tasks = Task.objects.all()
    today = timezone.now()
    stopwatch = Stopwatch.objects.first()
    return render(request, 'todo/task_list.html', {'tasks': tasks, 'today': today, 'stopwatch': stopwatch})

def task_list(request):
    tasks = Task.objects.all()
    today = timezone.now()
    quote = Quote.objects.order_by('?').first()  # 무작위 명언 선택
    return render(request, 'todo/task_list.html', {'tasks': tasks, 'today': today, 'quote':quote})

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

def update_time(request):
    if request.is_ajax() and request.method == 'POST':
        stopwatch = Stopwatch.objects.first()
        stopwatch.elapsed_time += 1
        stopwatch.save()
        return JsonResponse({'elapsed_time': stopwatch.elapsed_time})
    return JsonResponse({}, status=400)

def timer(request):
    # 세션에서 'elapsed_time' 값을 가져오고, 없으면 기본값으로 0을 사용
    elapsed_time = request.session.get('elapsed_time', 0)

    return render(request, 'timer.html', {'elapsed_time': elapsed_time})
