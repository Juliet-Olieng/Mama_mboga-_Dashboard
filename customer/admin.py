from django.contrib import admin
from.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","phone_number","email_address")
admin.site.register(Customer,CustomerAdmin)    
