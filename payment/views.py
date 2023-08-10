from django.shortcuts import render
from.form import PaymentForm
from payment.models import Payment

# Create your views here.
def display_payment(request):
    payments=Payment.objects.all()
    return render(request,"payment/display_payment.html",{"payments":payments})
def payment_detail(request,id):
    payment=Payment.objects.get(id=id)
    return render(request,"payment/payment_details.html",{"payment":payment})
