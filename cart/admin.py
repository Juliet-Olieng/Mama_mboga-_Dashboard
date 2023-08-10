from django.contrib import admin
from .models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("products","number_of_products","shipping_cost","delivery_options","payment_options")
admin.site.register(Cart,CartAdmin)    