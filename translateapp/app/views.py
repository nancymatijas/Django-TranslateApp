from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Bid

# Create your views here.
def home(request):
    context = {}
    return render(request, 'app/home.html', context)

def accept_bid(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id)
    job = bid.job
    if request.user == job.user and not bid.accepted:
        job.bid_set.update(accepted=False)
        bid.accepted = True
        bid.save()
        job.status = 'assigned'
        job.save()
    return redirect('accounts:dashboard')