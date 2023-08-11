from django.urls import path
from.views import notification_list
from.views import notification_detail
from.views import upload_notification


urlpatterns = [
    path("notifications/list",notification_list,name="notification_list_view"),
    path("notifications/upload",upload_notification,name="upload_notification_view"),
    path("notifications/<int:id>/",notification_detail,name="notification_detail_view"),
    
  
]
