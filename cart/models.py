from django.db import models
from inventory.models import Product

# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    number_of_products = models.DecimalField(decimal_places=2,max_digits=6)
    shipping_cost = models.DecimalField(decimal_places=2,max_digits=6)
    delivery_options = models.CharField(max_length=48)
    payment_options = models.CharField(max_length=48)
    
    
    def add_product(self,product):
        self.products.add(product)
        self.save()
        return self
    
    def get_total(self):
        products=self.products
        total=0
        for product in products:
            total+= Product.price
            return total

    def __str__(self):
        return self.products
    
    #...................................

        
        # total=sum([product.price for producr in self.products])
    
