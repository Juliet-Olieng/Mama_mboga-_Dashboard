from django.contrib import admin

# Register your models here.
from .models import Vendor
class VendorAdmin(admin.ModelAdmin):
    list_display = ("date","orderStatus","deliveryCost","deliveryMethod","date_created","deliveryDuration","deliveryPersonName")
admin.site.register(Vendor, VendorAdmin)
