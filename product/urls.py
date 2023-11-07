from django.urls import path
from Product.views import *

urlpatterns=[
    path('<str:pk>/',product_list,name='product_list'),
    path('review/<str:pk>/',review,name='review'),
    path('wishlist/<str:pk>/',wishlist,name='wishlist'),
    path('quick-view/<str:pk>/',quick_view,name='quick_view'),
]