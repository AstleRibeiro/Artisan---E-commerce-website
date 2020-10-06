from django.shortcuts import render
from .models import Madhubani


def MadhubaniHome(request):
    madhubani = Madhubani.objects.all()
    return render(request, "madhubani/madhubanihome.html", {"madhubani": madhubani})


def Madhubani_description(request, id):
    madhubanipainting = Madhubani.objects.filter(painting_id=id).first()
    return render(request, "madhubani/madhubani_description.html", {"madhubanipainting": madhubanipainting})
