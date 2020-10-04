from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import AbstractPainting, WildlifePainting, PastelPainting, InkPainting


def dyna(request):
    painting = AbstractPainting.objects.all()
    return render(request, "base.html", {"painting": painting})


def wildlifepaintings(request):
    wildlifepainting = WildlifePainting.objects.all()
    return render(request, "acrylic.html", {"wildlifepainting": wildlifepainting})


def pastelpaintings(request):
    pastelpainting = PastelPainting.objects.all()
    return render(request, "pastel.html", {"pastelpainting": pastelpainting})


def inkpaintings(request):
    inkpainting = InkPainting.objects.all()
    return render(request, "ink.html", {"inkpainting": inkpainting})


def abstract_description(request, id):
    painting = AbstractPainting.objects.filter(painting_id=id).first()
    return render(request, "main_description.html", {"painting": painting})


def wildlife_description(request, id):
    wildlifepainting = WildlifePainting.objects.filter(painting_id=id).first()
    return render(request, "wildlife_description.html", {"wildlifepainting": wildlifepainting})

def ink_description(request, id):
    inkpainting = InkPainting.objects.filter(painting_id=id).first()
    return render(request, "ink_description.html", {"inkpainting": inkpainting})

def pastel_description(request, id):
    pastelpainting = PastelPainting.objects.filter(painting_id=id).first()
    return render(request, "pastel_description.html", {"pastelpainting": pastelpainting})


@csrf_protect
def welcome_user(request):
    if 'min_price' in request.GET:
        filter_price1 = request.GET.get('min_price')
        val = 100
        print(val)

        filter_price2 = request.GET.get('max_price')
        # if filter_price1 == '':
        #     filter_price1 = 0
        # if filter_price2 == '':
        #     filter_price2 = 20000
        my_paintings = AbstractPainting.objects.filter(price__range=(filter_price1, filter_price2))
        print(my_paintings)
    return render(request, "index.html", {"products": my_paintings})

