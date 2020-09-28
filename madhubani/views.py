from django.shortcuts import render
from .models import Madhubani


def MadhubaniHome(request):
    madhubani = Madhubani.objects.all()
    return render(request, "madhubani/madhubanihome.html", {"madhubani": madhubani})

