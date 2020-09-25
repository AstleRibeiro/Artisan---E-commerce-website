from django.shortcuts import render
from .models import CampaignPosters, CorporatePosters, PoliticalPosters, ShowPosters


def corporatePosters(request):
    corporate = CorporatePosters.objects.all()
    return render(request, "corporate.html", {"corporate": corporate})


def campaignPosters(request):
    campaign = CampaignPosters.objects.all()
    return render(request, "campaign.html", {"campaign": campaign})


def politicalPosters(request):
    political = PoliticalPosters.objects.all()
    return render(request, "political.html", {"political": political})


def showPosters(request):
    show = ShowPosters.objects.all()
    return render(request, "show.html", {"show": show})


def show_description(request, id):
    showposter = ShowPosters.objects.filter(poster_id=id).first()
    return render(request, "show_description.html", {"showposter": showposter})

