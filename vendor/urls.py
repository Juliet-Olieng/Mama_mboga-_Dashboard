from .views import display_vendor
from.views import vendor_detail
from django.urls import path
from django.shortcuts import redirect

urlpatterns = [
    path("vendors/list",display_vendor,name="display_vendor_view"),
    path("vendors/<int:id>/",vendor_detail,name="vendor_detail_view"),]