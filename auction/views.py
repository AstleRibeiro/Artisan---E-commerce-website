from django.shortcuts import render
from .models import Auction

# Create your views here.


def auction(request):
    if request.method == 'POST':

        username = request.POST.get('username', '')
        ogval = request.POST.get('ogval', '')
        bid = request.POST.get('bid', '')
        # value = request.POST.get('value', '')
        if bid < ogval:
        	bids = Auction(username=username, bid=bid)
        else:
        	bids = Auction(username=username, bid=bid)
        	bids.save()
        	
       

    return render(request, 'auction.html')