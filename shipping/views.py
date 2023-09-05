from django.shortcuts import render
from shipping.models import Shipping

# Create your views here.
def display_list(request):
    shipping=Shipping.objects.all()
    return render(request,"shipping/display_list.html",{"shipping":shipping})