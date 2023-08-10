from django.db import models

# Create your models here.
class Shipping(models.Model):
    date = models.DateField()
    order = models.CharField(max_length=48)
    location = models.CharField(max_length=48)
    delivery_options = models.CharField(max_length=48)
    shipment_cost = models.DecimalField(max_digits=6,decimal_places=2)
    delivery_time = models.TimeField()

    def __str__(self):
        return self.order

