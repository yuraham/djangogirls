from django.shortcuts import render, get_object_or_404
from .models import Friend
from django.utils import timezone


# Create your views here.

def friend_list(request):
    lists = Friend.objects.all().order_by('name')
    return render(request, 'addr/friend_list.html', {'lists': lists})


def friend_detail(request, pk):
    detail = get_object_or_404(Friend, pk=pk)
    list = Friend.objects.all()
    return render(request, 'addr/friend_detail.html', {'detail': detail, 'list': list})


def home(request):
    return render(request, 'addr/home.html', {})
