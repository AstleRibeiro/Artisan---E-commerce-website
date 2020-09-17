from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import AddToCart
from dynamicnav.models import AbstractPainting
from django.db.models import Case, When


@login_required
def cart(request):
    if request.method == 'POST':
        user = request.user
        i_id = request.POST['i_id']
        addto = AddToCart.objects.filter(user=user)
        for i in addto:
            if i_id == i.i_id:
                message = "Item added more than once to the cart"
                break
        else:
            cart = AddToCart(user=user, i_id=i_id)
            cart.save()
            message = "Item is successfully added"

        AbstractPainting.objects.filter(painting_id=i_id).first()
        painting = AbstractPainting.objects.all()
        return render(request, "base.html", {'painting': painting})

    pl = AddToCart.objects.filter(user=request.user)
    ids = []
    for i in pl:
        ids.append(i.i_id)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    painting = AbstractPainting.objects.filter(painting_id__in=ids).order_by(preserved)
    return render(request, "add_to_cart/cart.html", {'painting': painting})
