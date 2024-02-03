from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=254, unique=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'phone']

    # @property
    # def is_staff(self):
    #     """Is the user a member of staff?"""
    #     return self.is_superuser
