from django.contrib import admin
from .models import Shipping

# Register your models here.
class ShippingAdmin(admin.ModelAdmin):
    list_display = ("date","order","location","delivery_options","shipment_cost","delivery_time")
admin.site.register(Shipping,ShippingAdmin)    
