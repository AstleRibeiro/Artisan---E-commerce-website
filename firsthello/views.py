from django.core.mail.backends import console
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect

from dynamicnav.models import AbstractPainting, WildlifePainting
from forposters.models import ShowPosters
from frames.models import TableTop, Floating
from photographs.models import ArchitecturalPhoto

from . import forms


def index(request):
    return render(request, 'splash.html')


def about(request):
    return render(request, 'aboutus.html')


def privacy(request):
    return render(request, 'privacy.html')


def home(request):
    abs_painting = AbstractPainting.objects.all()
    wild_painting = WildlifePainting.objects.all()
    show_poster = ShowPosters.objects.all()
    tableframe = TableTop.objects.all()
    floatingframe = Floating.objects.all()
    archi = ArchitecturalPhoto.objects.all()

    dict = {
        "abs_painting": abs_painting,
        "wild_painting": wild_painting,
        "show_poster": show_poster,
        "tableframe": tableframe,
        "floatingframe": floatingframe,
        "archi":archi,
    }
    return render(request, 'index.html', dict)


# @csrf_protect
def check(request):
    if request.method == "POST":
        filter_price1 = request.POST.get("min_price", "")
        filter_price2 = request.POST.get("max_price", "")
        print(filter_price1)
        print(filter_price2)

        # if filter_price1 == '':
        #     filter_price1 = 0
        # if filter_price2 == '':
        #     filter_price2 = 20000
        # my_paintings = AbstractPainting.objects.filter(price__range=(filter_price1, filter_price2))
    return render(request, "index.html")
