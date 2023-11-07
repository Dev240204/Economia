from django.urls import path
from Category.views import *

urlpatterns=[
    path('<str:pk>/',category,name='category'),
    path('brand/<str:pk>/',brand,name='brand'),
    path('color/<str:pk>/',color,name='color'),
    path('price/',price,name='price'),
    # path('category-list/',category_list,name='category_list')
]