from django.shortcuts import render, redirect
from . models import Product
from cart.cart import Cart

def index(request):
    product=Product.objects.all()
    return render(request,"index.html",{'product':product})
def cart(request):
    return render(request,"cart.html")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    cart.remove(product)
    return redirect("index")

def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")

def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")