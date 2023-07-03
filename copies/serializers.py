from .models import Copy
from rest_framework import serializers
from loans.serializers import LoanSerializer


class CopySerializer(serializers.ModelSerializer):
    loans = LoanSerializer(read_only=True)
    class Meta:
        model = Copy
        fields = ['id', 'avaliable', 'state', 'book','loans']
        read_only_fields = ['book']

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)
