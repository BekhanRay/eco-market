from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import *


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=254, unique=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()
