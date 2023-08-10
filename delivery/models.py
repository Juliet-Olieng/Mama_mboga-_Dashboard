from django.db import models

# Create your models here.
class Vendor(models.Model):
      date = models.DateField(auto_created=True)
      orderStatus = models.CharField(max_length=32)
      deliveryCost=models.DecimalField(max_digits=6,decimal_places=2)
      deliveryMethod = models.CharField(max_length=32)
      deliveryPersonName = models.CharField(max_length=32)
      deliveryDuration = models.DurationField()
      date_created = models.DateTimeField(auto_now_add=True)
      date_update = models.DateTimeField(auto_now=True)
      def __str__(self):
          return self.orderStatus
