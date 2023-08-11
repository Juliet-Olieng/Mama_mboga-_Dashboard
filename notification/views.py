from django.shortcuts import render
from notification.models import Notifications
from.forms import NotificationAploadForm

# Create your views here.
def notification_list(request):
    notifications=Notifications.objects.all()
    return render(request,'notifications/display_notification.html',{"notifications": notifications})

def upload_notification(request):
    if request.method == "POST":
        form = NotificationAploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    else:
        form = NotificationAploadForm()
    return render(request,"notifications/notification_upload.html",{"form":form})

def notification_detail(request,id):
    notification=Notifications.objects.get(id=id)
    return render(request,"notifications/notification_details.html",{"notification":notification})