
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

