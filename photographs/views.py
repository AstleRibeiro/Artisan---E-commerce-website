from django.shortcuts import render
from .models import ArchitecturalPhoto, AerialPhoto, FineartPhoto, FashionPhoto, PortraitPhoto, SportsPhoto


def Architectural(request):
    architectural = ArchitecturalPhoto.objects.all()
    return render(request, "architectural.html", {"architectural": architectural})


def Aerial(request):
    aerial = AerialPhoto.objects.all()
    return render(request, "aerial.html", {"aerial": aerial})


def Fashion(request):
    fashion = FashionPhoto.objects.all()
    return render(request, "fashion.html", {"fashion": fashion})


def Fineart(request):
    fineart = FineartPhoto.objects.all()
    return render(request, "fineart.html", {"fineart": fineart})


def Portraits(request):
    portraits = PortraitPhoto.objects.all()
    return render(request, "portrait.html", {"portraits": portraits})


def Sports(request):
    sports = SportsPhoto.objects.all()
    return render(request, "sports.html", {"sports": sports})


def aerial_description(request, id):
    aerialphoto = AerialPhoto.objects.filter(painting_id=id).first()
    return render(request, "aerial_description.html", {"aerialphoto": aerialphoto})


def architectural_description(request, id):
    architecturalphoto = ArchitecturalPhoto.objects.filter(painting_id=id).first()
    return render(request, "architectural_description.html", {"architecturalphoto": architecturalphoto})
