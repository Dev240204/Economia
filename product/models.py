from django.db import models

# Create your models here.
PRODUCT_CATEGORY = (
    ('shoes','Shoes'),
    ('clothes','Clothes'),
    ('mobile','Mobile'),
)

class Product(models.Model):
    product_name = models.CharField(max_length=200,null=True,blank=True)
    product_original_price = models.IntegerField(null=True,blank=True)
    product_discounted_price = models.IntegerField(null=True,blank=True)
    product_category = models.CharField(max_length=200,choices=PRODUCT_CATEGORY,null=True,blank=True)
    product_image_link = models.ImageField(max_length=1000,null=True,blank=True)
    product_checkout_link = models.CharField(max_length=1000,null=True,blank=True)
    product_description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.product_name