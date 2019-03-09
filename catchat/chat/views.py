from django.shortcuts import render
from django.views.generic import ListView
from .models import Message

# Create your views here.

def home(request):
    context = {
        'messages': Message.objects.all()
    }
    return render(request, 'chat/home.html', context)

