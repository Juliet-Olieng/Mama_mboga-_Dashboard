from django.contrib import admin
from.models import Payment

# Register your models here.
from.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("amount","date","receipt","status","order","payment_method")
admin.site.register(Payment,PaymentAdmin)
