from django.urls import path
from Product.views import *

urlpatterns=[
    path('',product_list,name='product_list'),
    path('quick-view/',quick_view,name='quick_view'),
]