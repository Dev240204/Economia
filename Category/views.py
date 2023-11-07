from django.shortcuts import render
from Product.models import Product
from Category.models import *

# Create your views here.
def category(request,pk):
    products=Product.objects.filter(product_category=pk)
    related_products = Product.objects.all()[20:23]
    context = {
        'products':products,
        'related_products':related_products,
    }
    return render(request,'Category/category.html',context=context)

def brand(request,pk):
    products=Product.objects.filter(product_brand=pk)
    related_products = Product.objects.all()[20:23]
    context = {
        'products':products,
        'related_products':related_products,
    }
    return render(request,'Category/category.html',context=context)

def color(request,pk):
    products=Product.objects.filter(product_color=pk)
    related_products = Product.objects.all()[20:23]
    context = {
        'products':products,
        'related_products':related_products,
    }
    return render(request,'Category/category.html',context=context)

def price(request):
    pass