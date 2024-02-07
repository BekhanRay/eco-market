from .views import UserCreateView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/', UserCreateView.as_view(), name='user_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify/', TokenVerifyView.as_view(), name='verify_token')
]