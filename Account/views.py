from django.http import HttpResponse
from django.shortcuts import render,redirect
from Account.models import *
from Product.models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def auth_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        context = {}

        user = authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            context['email'] = email
            context['msg'] = "Invalid Credentials"
        return render(request,'User/login.html',context)
    
    return render(request,'User/login.html')

def auth_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        context = {}
        user = User.objects.filter(username=username).first()
        if user is not None:
            context['msg'] = 'User already exists'
            return render("User/register.html",context)
        else:
            user = User.objects.create_user(username=username,email=email,password=password,phone=phone,type='customer')
            msg = 'User Created Successfully'
            return redirect('/home')
            
    return render(request,'User/register.html')

def auth_logout(request):
    logout(request)
    return redirect('/home/')

def wishlist(request):
    wishlist = request.user.products.all()
    context = {
        'wishlist':wishlist,
    }
    return render(request,'User/wishlist.html',context)

def home(request):
    featured_products = Product.objects.all()[30:35]
    new_products = Product.objects.all()[35:40]
    context = {
        'featured_products':featured_products,
        'new_products':new_products,
    }
    return render(request,'Index/home.html',context=context)