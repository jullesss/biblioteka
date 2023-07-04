from rest_framework import serializers
from .models import Loan
from users.models import User
from copies.models import Copy
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .exceptions import BlockedError, NoCopyAvailable


class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField()

    class Meta:
        model = Loan
        fields = ['id', 'user', 'copy', 'loan_date', 'username', 'retun_date']
        read_only_fields = ['return_date']

    def create(self, instance:Loan, validated_data: dict) -> Loan:
        user = get_object_or_404(User, user=validated_data.get("username"))

        if user.blocked:
            raise BlockedError()
        
       # import ipdb; ipdb.set_trace()
       
        copy_to_relate = Copy.objects.filter(available=True, book=validated_data.get('book')).first()

        if not copy_to_relate:
            raise NoCopyAvailable()
        
        instance.save(copy=copy_to_relate)


