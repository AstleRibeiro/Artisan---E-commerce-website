from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# from .models import AddToCart
from dynamicnav.models import AbstractPainting
from django.db.models import Case, When
from .models import Orders, OrderUpdate
import json

#
# @login_required
# def cart(request):
#     if request.method == 'POST':
#         user = request.user
#         i_id = request.POST['i_id']
#         addto = AddToCart.objects.filter(user=user)
#         for i in addto:
#             if i_id == i.i_id:
#                 message = "Item added more than once to the cart"
#                 break
#         else:
#             cart = AddToCart(user=user, i_id=i_id)
#             cart.save()
#             message = "Item is successfully added"
#
#         AbstractPainting.objects.filter(painting_id=i_id).first()
#         painting = AbstractPainting.objects.all()
#         return render(request, "base.html", {'painting': painting})
#
#     pl = AddToCart.objects.filter(user=request.user)
#     ids = []
#     for i in pl:
#         ids.append(i.i_id)
#
#     preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
#     painting = AbstractPainting.objects.filter(painting_id__in=ids).order_by(preserved)
#     return render(request, "add_to_cart/cart.html", {'painting': painting})
#

def cart(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        first_name = request.POST.get('first_name', '')
        amount = request.POST.get('amount', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Orders(items_json=items_json, first_name=first_name, last_name=last_name, email=email, address=address,
                       city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()

        thank = True
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        id = order.order_id
        return render(request, "add_to_cart/cart.html", {'thank': thank, 'id': id})

    return render(request, "add_to_cart/cart.html")


def yourorders(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '') 
       

        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')
    return render(request, "add_to_cart/yourorders.html")

































































