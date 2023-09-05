from django.shortcuts import render
from .myforms import WaterOrder, fields

# Create your views here.

def orderform(req):
    if req.POST:
        form = WaterOrder(req.POST)
        if form.is_valid():
            data = form.cleaned_data.values()
            print(data)
            data = {'data': zip(fields, data)}
            return render(req, 'result.html', context=data)
    else:
        form = WaterOrder()
    return render(req, 'form.html', context={'form': form})
