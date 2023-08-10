from django.db import models

# Create your models here.
class Cart(models.Model):
    products = models.TextField()
    number_of_products = models.DecimalField(decimal_places=2,max_digits=6)
    shipping_cost = models.DecimalField(decimal_places=2,max_digits=6)
    delivery_options = models.CharField(max_length=48)
    payment_options = models.CharField(max_length=48)

    def __str__(self):
        return self.products
