from django.contrib import admin
from.models import Notifications

# Register your models here.
class NotificationsAdmin(admin.ModelAdmin):
    list_display =  ("message","time","date","customer","identification_number")
admin.site.register(Notifications,NotificationsAdmin)    
