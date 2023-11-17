# wishes/urls.py
from django.urls import path
from .views import wish_list, add_wish

app_name = 'wishes'


urlpatterns = [
    path('wish-list/', wish_list, name='wish_list'),
    path('add-wish/', add_wish, name='add_wish'),
]
