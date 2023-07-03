from .models import Copy
from rest_framework import serializers


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ['id', 'avaliable', 'state', 'book']
        read_only_fields = ['book']

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)
