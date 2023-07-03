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
            "password",
            "email",
            "is_colaborator",
            "is_student"
            "blocked",
        ]
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This email is already been used",
                    )
                ]
            },
            "id": {"read_only": True},
            "password": {"write_only": True},
            "is_colaborator": {"required": True},
        }

    def create(self, validated_data: dict) -> User:
        is_colaborator = validated_data.get("is_colaborator", False)
        validated_data["is_student"] = not is_colaborator
        is_superuser = is_colaborator

        if is_colaborator:
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
