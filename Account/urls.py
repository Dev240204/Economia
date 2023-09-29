from django.urls import path
from Account.views import *

urlpatterns=[
    path('',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
    path('wishlist/',wishlist,name='wishlist'),
    path('home/',home,name='home')
]