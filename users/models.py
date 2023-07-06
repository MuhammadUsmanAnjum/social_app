from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True )
    register_on_holiday = models.BooleanField(default=False)
    
    
    objects = CustomUserManager()


    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    