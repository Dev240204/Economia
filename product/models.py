from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Shoes(models.Model):
    product_name = models.CharField(max_length=200),
    product_original_price = models.IntegerField(),
    product_discounted_price = models.IntegerField(),
    product_description = models.TextField(),
    product_image = models.TextField(),
    product_category = models.CharField(max_length=50),
    product_brand = models.CharField(max_length=50),
    # product_review = models.IntegerField(),
    product_rating = models.IntegerField(),
    product_sizes = models.TextField(),
    product_colors = models.TextField(),
    product_link = models.TextField(),

    def __str__(self):
        return self.product_name
