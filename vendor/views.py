from django.shortcuts import render
from vendor.models import Vendor
from.form import DisplayVendor

# Create your views here.
def display_vendor(request):
    vendors=Vendor.objects.all()
    return render(request,"vendor/display_vendor.html",{"vendors": vendors})
def vendor_detail(request,id):
    vendor=Vendor.objects.get(id=id)
    return render(request,"vendor/vendor_detail.html",{"vendor":vendor})

def add_vendor(request):
    if request.method == "POST":
        form = DisplayVendor(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    else:
        form = DisplayVendor()
    return render(request,"vendor/add_vendor.html",{"form":form})