from django.shortcuts import render
from .models import Auction

# Create your views here.


def auction(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        bid = request.POST.get('bid', '')
        # value = request.POST.get('value', '')


        bids = Auction(username=username, bid=bid)
        bids.save()

    return render(request, 'auction.html')