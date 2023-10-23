from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from user_app.models import CustomUser


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password", "creator", "administrator")
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        if CustomUser.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError({"error": "Email already exists!"})

        custom_user = CustomUser(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
            creator=self.validated_data.get("creator", None),
            administrator=self.validated_data.get("administrator", False),
        )
        custom_user.set_password(self.validated_data["password"])
        custom_user.save()

        return custom_user


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "creator", "administrator", "email"]
