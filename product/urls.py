from django.urls import path
from . import views

urlpatterns = [
    path("index",views.index,name="index"),
    path("category/<str:pk>",views.category,name="category"),
    path("single/<str:pk>",views.single,name="single")
]