from .models import Favorite
from rest_framework import serializers
from loans.serializers import LoanSerializer
from users.serializers import UserSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'book', 'user']
        read_only_fields = ['book']

    def create(self, validated_data):
        return Favorite.objects.create(**validated_data)
