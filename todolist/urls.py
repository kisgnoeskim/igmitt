from django.urls import path
from . import views
from .views import StopwatchView

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('stopwatch/', StopwatchView.as_view(), name='stopwatch'),

]