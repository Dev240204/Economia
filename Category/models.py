from django.db import models
from Product.models import *

# Create your models here.
class Shoes(models.Model):
    product = models.ForeignKey('Product.Product',on_delete=models.CASCADE,null=True,blank=True)
    color = models.CharField(max_length=200,null=True,blank=True)
    size = models.IntegerField(null=True,blank=True)
    brand = models.CharField(max_length=200,null=True,blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.product.product_name
    
class Clothes(models.Model):
    product = models.ForeignKey('Product.Product',on_delete=models.CASCADE,null=True,blank=True)
    color = models.CharField(max_length=200,null=True,blank=True)
    size = models.IntegerField(null=True,blank=True)
    brand = models.CharField(max_length=200,null=True,blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.product.product_name
    
class Mobile(models.Model):
    product = models.ForeignKey('Product.Product',on_delete=models.CASCADE,null=True,blank=True)
    color = models.CharField(max_length=200,null=True,blank=True)
    ram = models.CharField(max_length=50,null=True,blank=True)
    brand = models.CharField(max_length=200,null=True,blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.product.product_name