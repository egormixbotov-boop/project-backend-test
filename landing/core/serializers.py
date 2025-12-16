from rest_framework import serializers
from .models import UsersInfo


class UsersInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersInfo
        fields = ["id", "name", "email", "message", "created_at"]


