from django.urls import path
from Account.views import *

urlpatterns=[
    path('',auth_login,name='login'),
    path('register/',auth_register,name='register'),
    path('logout/',auth_logout,name='logout'),
    path('wishlist/',wishlist,name='wishlist'),
    path('home/',home,name='home')
]