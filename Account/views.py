from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'User/login.html')

def register(request):
    return render(request,'User/register.html')

def logout(request):
    pass

def wishlist(request):
    return render(request,'User/wishlist.html')

def home(request):
    return render(request,'Index/home.html')