from django.shortcuts import render
from . import models
from dynamicnav.models import AbstractPainting


def cart(request):
    if request.method == 'POST':
        user = request.user
        i_id = request.POST['i_id']
        painting = models.AddToCart.objects.filter(user=user)
        for i in painting:
            if i_id == i.i_id:
                message = "Item added more than once to the cart"
                break
            else:
                cart = models.AddToCart(user=user, i_id=i_id)
                cart.save()
                message = "Item is successfully added"
        painting = AbstractPainting.objects.filter(painting_id=i_id).first()
        return render(request, "dynamicnav/base.html", {"painting": painting})