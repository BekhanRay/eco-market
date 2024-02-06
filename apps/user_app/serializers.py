from django.contrib.auth.hashers import make_password

from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ['username', 'password', 'address', 'email', 'phone']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
