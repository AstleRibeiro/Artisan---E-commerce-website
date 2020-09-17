from django.shortcuts import render
from .forms import FormName
from django.urls import reverse_lazy


def index(request):
    return render(request, 'splash.html')

def home(request):
    return render(request, 'index.html')





