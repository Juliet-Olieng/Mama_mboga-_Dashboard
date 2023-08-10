from django.db import models

# Create your models here.
class Notifications(models.Model):
    message = models.CharField(max_length=48)
    time = models.TimeField()
    date = models.DateField()
    customer = models.CharField(max_length=48)
    identification_number = models.CharField(max_length=48)

    def __str__(self):
        return self.message
