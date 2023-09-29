from django.urls import path
from Category.views import *

urlpatterns=[
    path('',category,name='category'),
    path('category-list/',category_list,name='category_list')
]