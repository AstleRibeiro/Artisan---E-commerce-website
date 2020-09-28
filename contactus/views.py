from django.shortcuts import render
from . import models
# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        userproblem = models.ContactUs(name=name, email=email, message=message)
        userproblem.save()
    return render(request, "contactus/contactus.html")

