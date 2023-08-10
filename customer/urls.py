from django.urls import path
from.views import display_customer
from.views import customer_detail


urlpatterns = [
    path("customers/list",display_customer,name="display_customer_view"),
    path("customer/<int:id>/",customer_detail,name="customer_detail_view"),
]
