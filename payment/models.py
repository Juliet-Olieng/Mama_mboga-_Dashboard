from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(decimal_places=2,max_digits=6)
    payment_method = models.CharField(max_length=32)
    date = models.DateField()
    receipt = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    order = models.CharField(max_length=32)

    def __str__(self):
        return self.payment_method
