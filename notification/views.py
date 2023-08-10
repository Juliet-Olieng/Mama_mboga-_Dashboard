from django.shortcuts import render
from notification import Notifications

# Create your views here.
def notification_list(request):
    notifications=Notifications.objects.all()
    return render(request,'notification/notification_list.html',{"notifications": notifications})