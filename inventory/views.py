from django.shortcuts import render
from.forms import ProductAploadForm
from inventory.models import Product
from cart.models import Cart
from django.shortcuts import redirect,render,get_object_or_404



# Create your views here.
def upload_product(request):
    if request.method == "POST":
        form = ProductAploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    else:
        form = ProductAploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})

def product_list(request):
    products=Product.objects.all()
    return render(request,'inventory/product_list.html',{"products": products})
def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,"inventory/product_detail.html",{"product":product})
def addTocart(request):
    cart=[]
    return render(request,'inventory/cart.html',{"cart":cart})
def edit_product_view(request,id):
    product=Product.objects.get(id=id)
    if request.method=="POST":
        form=ProductAploadForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
        return redirect("product_detail_view",id=product.id)
    else:
        form=ProductAploadForm(instance=product)
        return render(request,"inventory/edit_product.html",{"form":form})
         
def add_to_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product.name,
        defaults={'price': product.price, 'quantity': 1, 'image': product.image}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')



