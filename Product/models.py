from django.db import models

# Create your models here.
PRODUCT_CATEGORY = (
    ('shoes','Shoes'),
    ('clothes','Clothes'),
    ('mobile','Mobile'),
)

class Product(models.Model):
    product_name = models.CharField(max_length=200,null=True,blank=True)
    product_original_price = models.CharField(max_length=100,null=True,blank=True)
    product_discounted_price = models.CharField(max_length=100,null=True,blank=True)
    product_category = models.CharField(max_length=200,choices=PRODUCT_CATEGORY,null=True,blank=True)
    product_image_link = models.CharField(max_length=1000,null=True,blank=True)
    product_checkout_link = models.CharField(max_length=1000,null=True,blank=True)
    product_brand = models.CharField(max_length=200,null=True,blank=True)
    product_color = models.CharField(max_length=200,null=True,blank=True)
    product_description = models.TextField(null=True,blank=True)
    product_is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True,blank=True)
    review = models.CharField(max_length=1000,null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.product.product_name


        