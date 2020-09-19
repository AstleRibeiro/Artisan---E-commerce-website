from django.shortcuts import render
from .forms import FormName
from django.urls import reverse_lazy
from dynamicnav.models import AbstractPainting


def index(request):
    return render(request, 'splash.html')

def home(request):
    abs_painting = AbstractPainting.objects.all()
    return render(request, 'index.html', {"abs_painting": abs_painting})





