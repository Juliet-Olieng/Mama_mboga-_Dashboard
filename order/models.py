from django.db import models
from cart.models import Cart
# from customer.models import Customer
from shipping.models import Shipping


# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=48)
    order_total = models.CharField(max_length=48)
    date = models.DateField()
    location = models.CharField(max_length=48)
    delivery_options = models.CharField(max_length=48)
    delivery_date = models.DateField()
    basket = models.ForeignKey(Cart,on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipping,on_delete=models.CASCADE,null=True,related_name="related_shipments")


    def __str__(self):
        return self.order_number



