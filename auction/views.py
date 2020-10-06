from django.db.models import Max
from django.shortcuts import render
from .models import Auction
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


def auction(request):
    if request.method == 'POST':

        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        bid = request.POST.get('bid', '')


        ogval = 12000

        og = int(ogval)
        bid1 = int(bid)

        subject = "Bid Succssfully Placed"
        message = "Thankyou for bidding in the auction dated 6/10/2020. Your order details are: \n Name: " + username + "\n starting bid: " + str(
            ogval) + "\n Your bid: " + bid + "\n \n \n Yours sincerely, \n The Artisan"

        # value = request.POST.get('value', '')
        if bid1 > og:
            bids = Auction(username=username, bid=bid)
            bids.save()
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)

    cbid = Auction.objects.aggregate(Max('bid'))

    return render(request, 'auction.html', {'cbid': cbid})
