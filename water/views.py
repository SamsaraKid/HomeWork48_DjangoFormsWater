from django.shortcuts import render
from .myforms import WaterOrder

# Create your views here.

def order(req):
    if req.POST:
        form = WaterOrder(req.POST)
    else:
        form = WaterOrder()
    return render(req, 'form.html', context={'form': form})