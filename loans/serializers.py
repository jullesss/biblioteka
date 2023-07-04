from rest_framework import serializers
from .models import Loan
from users.models import User
from copies.models import Copy
from .exceptions import BlockedError, NoCopyAvailable


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = ['id', 'copy', 'loan_date', 'return_date']
        read_only_fields = ['return_date', 'copy']


    def create(self, validated_data: dict) -> Loan:
        username = validated_data.pop('username')
        user = User.objects.filter(username__iexact=username).first()

        if user.blocked:
            raise BlockedError()
        
        copy_to_relate = Copy.objects.filter(available=True, book=validated_data.get('book')).first()
        
        if not copy_to_relate:
            raise NoCopyAvailable()
        
        copy_to_relate.available = False
        copy_to_relate.save()
        
        instance = Loan.objects.create(copy=copy_to_relate, user=user)
        
        instance.save()

        return instance


