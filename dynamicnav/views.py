from django.shortcuts import render
from .models import AbstractPainting, AcrylicPainting, PastelPainting, InkPainting


def dyna(request):
    painting = AbstractPainting.objects.all()
    return render(request, "base.html", {"painting": painting})


def acrylicpaintings(request):
    acrylicpainting = AcrylicPainting.objects.all()
    return render(request, "acrylic.html", {"acrylicpainting": acrylicpainting})


def pastelpaintings(request):
    pastelpainting = PastelPainting.objects.all()
    return render(request, "pastel.html", {"pastelpainting": pastelpainting})


def inkpaintings(request):
    inkpainting = InkPainting.objects.all()
    return render(request, "ink.html", {"inkpainting": inkpainting})
