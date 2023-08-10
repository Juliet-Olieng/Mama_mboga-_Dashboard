from django.urls import path
from.views import notification_list


urlpatterns = [
    path("notifications/list",notification_list,name="notification_list_view"),
  
]
