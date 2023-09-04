from django.shortcuts import render
from .myforms import WaterOrder, fields

# Create your views here.

def order(req):
    if req.POST:
        form = WaterOrder(req.POST)
        if form.is_valid():
            data = req.POST.dict()
            data.pop('csrfmiddlewaretoken')
            data = list(data.values())
            data = {'data': zip(fields, data)}
            print(data)
            return render(req, 'result.html', context=data)
    else:
        form = WaterOrder()
    return render(req, 'form.html', context={'form': form})

