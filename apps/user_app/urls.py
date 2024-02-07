from .views import UserCreateView

from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/', UserCreateView.as_view(), name='user_list')
]