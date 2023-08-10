from django.shortcuts import render
from vendor.models import Vendor

# Create your views here.
def display_vendor(request):
    vendors=Vendor.objects.all()
    return render(request,"vendor/display_vendor.html",{"vendors": vendors})
def vendor_detail(request,id):
    vendor=Vendor.objects.get(id=id)
    return render(request,"vendor/vendor_detail.html",{"vendor":vendor})