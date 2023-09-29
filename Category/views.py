from django.shortcuts import render

# Create your views here.
def category(request):
    return render(request,'Category/category.html')

def category_list(request):
    return render(request,'Category/category-list.html')