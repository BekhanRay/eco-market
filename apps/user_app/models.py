from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import *

from apps.user_app.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=False, default='user', verbose_name='username')
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=254, unique=False)
    is_staff = models.BooleanField(default=False)

    password = models.CharField(max_length=128, verbose_name='password')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['password',]

