from django.shortcuts import render,redirect
from Product.models import *
from Category.models import *
from Account.utils import *
import joblib

# Create your views here.
def product_list(request,pk):
    related_products = Product.objects.all()[15:20]
    product = Product.objects.filter(product_name=pk)
    product = product[0]
    type = product.product_category
    if type == 'mobile':
        product_detail = Mobile.objects.filter(product=product)
        product_detail = product_detail[0]
    product_detail_dict = {
        'color':product_detail.color,
        'ram':product_detail.ram,
        'brand':product_detail.brand,
        'is_available':product_detail.is_available,
    }
    reviews = Review.objects.all()
    reviews = reviews.filter(product=product)

    model = joblib.load('static/model.sav')
    new_data = int(product.product_original_price.replace(',',''))
    new_data = [[new_data]]

    predicted_price = model.predict(new_data)
    predicted_price = int(predicted_price[0])

    predicted_chart = predicted_price_chart(predicted_price,product.product_discounted_price)
    context = {
        'product':product,
        'product_detail_dict':product_detail_dict,
        'reviews':reviews,
        'related_products':related_products,
        'predicted_price':predicted_price,
        'predicted_chart':predicted_chart,
    }

    return render(request,'Product/product.html',context=context)

def review(request,pk):
    if request.method == 'POST':
        product = Product.objects.all().filter(product_name=pk)
        product_review = request.POST.get('product_review')
        product_rating = request.POST.get('product_rating')

        review = Review()
        review.name = request.user.username
        review.product = product[0]
        review.review = product_review
        review.rating = product_rating
        review.save()
        return redirect('/product')
    return render(request,'Product/product.html')

def wishlist(request,pk):
    if request.method == 'GET':
        product = Product.objects.all().filter(product_name=pk)
        user = request.user
        user.products.add(product[0])
        url = "/product/"+pk
        return redirect(url)
    return render(request,'Product/product.html')

def quick_view(request,pk):
    product = Product.objects.filter(product_name=pk)
    context = {
        'product':product[0]
    }
    return render(request,'Product/product-quick-view.html',context=context)