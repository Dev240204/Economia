from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from Product.models import *

# Create your models here.
USER_TYPE = (
    ('admin','Admin'),
    ('customer','Customer'),
)

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=50,choices=USER_TYPE,default='admin')
    phone = models.CharField(max_length=50,null=True,blank=True)
    products = models.ManyToManyField(Product,blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user