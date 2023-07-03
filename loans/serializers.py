from rest_framework import serializers
from .models import Loan
from users.serializers import UserSerializer

class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'user', 'copy', 'loan_date', 'retun_date']
        extra_kwargs = {"return_date": {"read_only": True}}

