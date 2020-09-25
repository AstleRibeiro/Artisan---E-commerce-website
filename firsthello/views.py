from django.shortcuts import render
from django.urls import reverse_lazy
from dynamicnav.models import AbstractPainting, WildlifePainting
from firstproject.settings import EMAIL_HOST_USER
from forposters.models import ShowPosters
from frames.models import TableTop
from django.core.mail import send_mail
from django.conf import settings

from . import forms


def index(request):
    return render(request, 'splash.html')


def contact(request):
    return render(request, 'contactus.html')


def home(request):
    abs_painting = AbstractPainting.objects.all()
    wild_painting = WildlifePainting.objects.all()
    show_poster = ShowPosters.objects.all()
    tableframe = TableTop.objects.all()

    dict = {
        "abs_painting": abs_painting,
        "wild_painting": wild_painting,
        "show_poster": show_poster,
        "tableframe": tableframe,
    }
    return render(request, 'index.html', dict)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST["email"]
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoyin your Django Tutorials'
        email_from = settings.EMAIL_HOST_USER
        recepient = "zendeomkar45@gmail.com"
        send_mail(subject, message, email_from, recepient, fail_silently=False)
    return render(request, 'index.html', {'form': sub})
