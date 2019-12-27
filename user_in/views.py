from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login
from SellerAdmin.models import Service
from . models import Cart

def user_index(request):
    data = Service.objects.all()
    return render(request,'user/index.html',{'data':data})

def cart(request):
    cart = Cart.objects.filter()
    return render(request, 'user/cart.html',{'cart':cart})

def details(request,pk):
    p = Service.objects.get(pk=pk)
    return render(request, 'user/details.html',{'data':p})

def add_cart(request,pk):
    service=Service.objects.get(pk=pk)
    Cart.objects.create(product_id=service,customer=request.user)
    return redirect(cart)
