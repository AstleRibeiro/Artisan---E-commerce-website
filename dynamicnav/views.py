from django.shortcuts import render
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

