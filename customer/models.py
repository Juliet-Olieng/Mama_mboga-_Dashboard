from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=48)
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    address = models.CharField(max_length=48)

    def __str__(self):
        return self.name