from django.shortcuts import render, redirect
from .models import Wish
from django.views.decorators.http import require_POST
from django.utils import timezone


def wish_list(request):
    wishes = Wish.objects.all()
    today = timezone.now()
    return render(request, 'wishes/wish_list.html', {'wishes': wishes, 'today': today})

@require_POST
def add_wish(request):
    content = request.POST.get('wish_content')
    Wish.objects.create(content=content)
    return redirect('wishes:wish_list')
