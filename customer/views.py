from django.shortcuts import render
from.form import CustomerForm
from customer.models import Customer
from django.shortcuts import redirect

# Create your views here.
def display_customer(request):
    customers=Customer.objects.all()
    return render(request,"customer/customer_list.html",{"customers":customers})
def customer_detail(request,id):
    customer=Customer.objects.get(id=id)
    return render(request,"customer/customer_detail.html",{"customer":customer})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    else:
        form = CustomerForm()
    return render(request,"customer/add_customer.html",{"form":form})
