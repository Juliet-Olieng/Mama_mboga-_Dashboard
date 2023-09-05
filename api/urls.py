from django.urls import path
from .views import CustomerListView
from .views import CustomerDetailView
from .views import CartListView
from .views import CartDetailView
from .views import ProductDetailView
from .views import ProductListView
from .views import NotificationDetailView
from .views import NotificationListView
from .views import OrderListView
from .views import OrderDetailView
from .views import ShippingListView
from .views import ShippingDetailView
from .views import PaymentListView
from .views import PaymentDetailView
from .views import VendorDetailView
from .views import VendorListView
urlpatterns=[
    path('customers/',CustomerListView.as_view(),name='customer_list_view'),
    path('customers/<int:id>/',CustomerDetailView.as_view(),name='customer_detail_view'),
    path('carts/',CartListView.as_view(),name='cart_list_view'),
    path('cart/<int:id>/', CartDetailView.as_view(),name='cart_detail_view'),
    path('products/',ProductListView.as_view(),name='product_list_view'),
    path('product/<int:id>/',ProductDetailView.as_view(), name='product_detail_view'),
    path('notifications/',NotificationListView.as_view(),name="notification_list_view"),
    path('notification/<int:id>/', NotificationDetailView.as_view(),name='notification_details_view'),
    path('orders/',OrderListView.as_view(),name='order_list_view'),
    path('order/<int:id>/', OrderDetailView.as_view(), name='order_detail_view'),
    path('payments/',PaymentListView.as_view(), name='payment_list_view'),
    path('payment/<int:id>/', PaymentDetailView.as_view(),name='payment_detail_view'),
    path('shippings/', ShippingListView.as_view(), name='shipping_list_view'),
    path('shipping/<int:id>/',ShippingDetailView.as_view(), name='shipping_detail_view'),
    path('vendors/', VendorListView.as_view(), name='vendor_list_view'),
    path('vendor/<int:id>/', VendorDetailView.as_view(),name='vendor_detail_view'),
    
]