from django.shortcuts import render
from .models import DeepSet, Modern, Floating, TableTop, Gallery


def DeepSet1(request):
    deepset = DeepSet.objects.all()
    return render(request, "deepset.html", {"deepset": deepset})


def Gallery1(request):
    gallery = Gallery.objects.all()
    return render(request, "gallery.html", {"gallery": gallery})


def Modern1(request):
    modern = Modern.objects.all()
    return render(request, "modern.html", {"modern": modern})


def Floating1(request):
    floating = Floating.objects.all()
    return render(request, "floating.html", {"floating": floating})


def TableTop1(request):
    tabletop = TableTop.objects.all()
    return render(request, "tabletop.html", {"tabletop": tabletop})



def table_description(request, id):
    tableframe = TableTop.objects.filter(painting_id=id).first()
    return render(request, "table_description.html", {"tableframe": tableframe})


def deepset_description(request, id):
    deepsetFrame = DeepSet.objects.filter(painting_id=id).first()
    return render(request, "deepset_description.html", {"deepsetFrame": deepsetFrame})

