from django.urls import path
from.views import display_list



urlpatterns = [
    path("shippings/list",display_list,name="display_list_view"),
]
