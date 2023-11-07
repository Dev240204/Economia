from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from Product.models import *
from Category.models import *
import csv

def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8-sig').splitlines()
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                print(row)
                Product.objects.create(
                    product_name=row['Product_Names'],
                    product_original_price=row['Original_price'],
                    product_discounted_price=row['Discounted_price'],
                    product_category="mobile",
                    product_image_link=row['Image_links'],
                    product_checkout_link=row['URL'],
                    product_brand=row['brand'],
                    product_color=row['Color'],
                    product_description=row['Description'],
                )
                products = Product.objects.filter(product_name=row['Product_Names'])
                if products.count() == 1:
                    product = products.first()
                    Mobile.objects.create(
                        product=product,
                        color=row['Color'],
                        ram=row['Ram'],
                        brand=row['brand'],
                    )
                elif products.count() == 2:
                    product = products.last()
                    Mobile.objects.create(
                        product=product,
                        color=row['Color'],
                        ram=row['Ram'],
                        brand=row['brand'],
                    )
                else:
                    product = products.first()
                    Mobile.objects.create(
                        product=product,
                        color=row['Color'],
                        ram=row['Ram'],
                        brand=row['brand'],
                    )


            return HttpResponse('Success!') # Redirect to a success page
    else:
        form = CSVImportForm()

    return render(request, 'Scrap/index.html', {'form': form})