from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import AbstractPainting, WildlifePainting, PastelPainting, InkPainting


def dyna(request):
    painting = AbstractPainting.objects.all()
    return render(request, "basic.html", {"painting": painting})


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

def search(request):
    try:
        query = request.GET.get('search')
    except:
        query = None

    if query:
        painting = AbstractPainting.objects.filter(name__icontains=query) | AbstractPainting.objects.filter(
            artist__icontains=query, ) | AbstractPainting.objects.filter(
            description__icontains=query, ) | AbstractPainting.objects.filter(
            small_description__icontains=query, ) | AbstractPainting.objects.filter(specifications__icontains=query)

        wildlife = WildlifePainting.objects.filter(name__icontains=query) | WildlifePainting.objects.filter(
            artist__icontains=query, ) | WildlifePainting.objects.filter(
            description__icontains=query, ) | WildlifePainting.objects.filter(
            small_description__icontains=query, ) | WildlifePainting.objects.filter(specifications__icontains=query)

        pastelpainting = PastelPainting.objects.filter(name__icontains=query) | PastelPainting.objects.filter(
            artist__icontains=query, ) | PastelPainting.objects.filter(
            description__icontains=query, ) | PastelPainting.objects.filter(
            small_description__icontains=query, ) | PastelPainting.objects.filter(specifications__icontains=query)

        inkpainting = InkPainting.objects.filter(name__icontains=query) | InkPainting.objects.filter(
            artist__icontains=query, ) | InkPainting.objects.filter(
            description__icontains=query, ) | InkPainting.objects.filter(
            small_description__icontains=query, ) | InkPainting.objects.filter(specifications__icontains=query)

        context = {'query': query,
                   'painting': painting,
                   'wildlife': wildlife,
                   'pastelpainting': pastelpainting,
                   'inkpainting': inkpainting, }

        template = "search.html"
    else:
        template = "basic.html"
        context = {}

    return render(request, template, context)

