from .models import Favorite
from rest_framework import serializers
from loans.serializers import LoanSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'book', 'user']
        read_only_fields = ['book', 'user']

    def create(self, validated_data):
        return Favorite.objects.create(**validated_data)