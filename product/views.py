from django.shortcuts import render

# Create your views here.
def product_list(request):
    return render(request,'Product/product.html')

def quick_view(request):
    return render(request,'Product/product-quick-view.html')