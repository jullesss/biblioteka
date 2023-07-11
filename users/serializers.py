from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "email",
            "is_admin",
            "blocked",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "password": {"write_only": True},
            "is_admin": {"required": True},
        }

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        password = validated_data.pop("password", None)

        if password:
            instance.set_password(raw_password=password)

        instance.save()
        return instance
