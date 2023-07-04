from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "is_admin",
            "blocked",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "is_admin": {"required": True},
        }

    def create(self, validated_data: dict) -> User:
        is_superuser = validated_data.get("is_superuser", False)
        is_admin = validated_data.get("is_admin", False)

        if is_superuser:
            validated_data["is_admin"] = True
            user = User.objects.create_superuser(**validated_data)
        elif is_admin:
            user = User.objects.create_superuser(**validated_data)
        else:
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
