from django.urls import path
from.views import display_payment
from.views import payment_detail


urlpatterns = [
    path("payments/list",display_payment,name="display_payment_view"),
    path("payments/<int:id>/",payment_detail,name="payment_detail_view"),
]
