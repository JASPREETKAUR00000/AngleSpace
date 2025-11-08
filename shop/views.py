from django.shortcuts import render, redirect
from .models import Product, Order
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def about(request):
    return render(request, "about.html")

def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def buy(request, product_id):
    product = Product.objects.get(id=product_id)
    Order.objects.create(product=product)
    return redirect("/orders/")


def orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})

