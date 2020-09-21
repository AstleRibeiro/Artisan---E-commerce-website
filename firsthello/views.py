from django.shortcuts import render
from .forms import FormName
from django.urls import reverse_lazy
from dynamicnav.models import AbstractPainting, WildlifePainting




def index(request):
    return render(request, 'splash.html')

def contact(request):
    return render(request, 'contactus.html')

def home(request):
    abs_painting = AbstractPainting.objects.all()
    wild_painting = WildlifePainting.objects.all()

    dict = {
        "abs_painting": abs_painting,
        "wild_painting": wild_painting,

    }
    return render(request, 'index.html', dict)





