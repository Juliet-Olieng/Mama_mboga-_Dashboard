from django.shortcuts import render
from rest_framework import status
from customer.models import Customer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CustomerSerializer
from cart.models import Cart
from .serializer import CartSerializer
from inventory.models import Product
from .serializer import ProductSerializer
from notification.models import Notifications
from .serializer import NotificationSerializer
from order.models import Order
from .serializer import OrderSerializer
from payment.models import Payment
from .serializer import PaymentSerializer
from shipping.models import Shipping
from .serializer import ShippingSerializer
from vendor.models import Vendor
from .serializer import VendorSerializer

class CustomerListView(APIView):
    def get(self,request):
        customers = Customer.objects.all()
        serializer =CustomerSerializer(customers,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
class CustomerDetailView(APIView):
    def get(self, request,id, format=None):
        customer=self.get_object(id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def post (self,request, id, format=None):
        customer=self.get_object(id)
        serializer=CustomerSerializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        customer= self.get_object(id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # .........................................................
    
class CartListView(APIView):
    def get(self, request):
        carts=Cart.objects.all()
        serializer= CartSerializer(carts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CartDetailView(APIView):
    def get(self,request,id, format=None):
        cart= self.get_object(id)
        serializer= CartSerializer(cart)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        cart = self.get_object(id)
        serializer=CartSerializer(cart,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        cart= self.get_object(id)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # .........................................

class ProductListView(APIView):
    def get(self,request):
        products =Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class ProductDetailView(APIView):
    def get(self, request, id, format=None):
        product= self.get_object(id) 
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        product=self.get_object(id)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        product= self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
    # .........................................................
class NotificationListView(APIView):
    def get(self,request):
        notifications =Notifications.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= NotificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class NotificationDetailView(APIView):
    def get(self, request, id, format=None):
        notification= self.get_object(id) 
        serializer=NotificationSerializer(notification)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        notification=self.get_object(id)
        serializer=NotificationSerializer(notification,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        notification= self.get_object(id)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # ............................................  
class OrderListView(APIView):
    def get(self,request):
        orders =Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class OrderDetailView(APIView):
    def get(self, request, id, format=None):
        order= self.get_object(id) 
        serializer=OrderSerializer(order)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        order=self.get_object(id)
        serializer=OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        order= self.get_object(id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# ..............................................
class PaymentListView(APIView):
    def get(self,request):
        payments =Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class PaymentDetailView(APIView):
    def get(self, request, id, format=None):
        payment= self.get_object(id) 
        serializer=PaymentSerializer(payment)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        payment=self.get_object(id)
        serializer=PaymentSerializer(payment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        payment= self.get_object(id)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ........................................
class ShippingListView(APIView):
    def get(self,request):
        shippings =Shipping.objects.all()
        serializer = ShippingSerializer(shippings, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= ShippingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class ShippingDetailView(APIView):
    def get(self, request, id, format=None):
        shipping= self.get_object(id) 
        serializer=ShippingSerializer(shipping)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        shipping=self.get_object(id)
        serializer=ShippingSerializer(shipping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        shipping= self.get_object(id)
        shipping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # .................................
class VendorListView(APIView):
    def get(self,request):
        vendors=Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class VendorDetailView(APIView):
    def get(self, request, id, format=None):
        vendor= self.get_object(id) 
        serializer=VendorSerializer(vendor)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        vendor=self.get_object(id)
        serializer=VendorSerializer(vendor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        vendor= self.get_object(id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
    
  
         
        

            

