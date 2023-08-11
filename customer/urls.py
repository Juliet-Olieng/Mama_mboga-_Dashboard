from django.urls import path
from.views import display_customer
from.views import customer_detail
from.views import add_customer


urlpatterns = [
    path("customers/list",display_customer,name="display_customer_view"),
    path("customers/<int:id>/",customer_detail,name="customer_detail_view"),
    path("customers/upload", add_customer,name="add_customer_view"),
]
