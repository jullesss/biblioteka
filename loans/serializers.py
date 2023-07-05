from rest_framework import serializers
from .models import Loan
from users.models import User
from copies.models import Copy
from .exceptions import BlockedError, NoCopyAvailable, NoLoan
from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework.views import Response, status


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = ['id', 'copy', 'loan_date', 'return_date', 'user']
        read_only_fields = ['return_date', 'copy', 'user']


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
    

    def update(self, instance, validated_data: dict):

        user_loan = get_object_or_404(Loan, copy = validated_data.get('copy'), user = validated_data.get('user'))

        if not user_loan:
            raise NoLoan()
        
        user_loan.return_date = datetime.now()
        today = datetime.now().day
    
        due_date = user_loan.due_date.day

        if today > due_date:
            found_user = get_object_or_404(User, username=validated_data.get('username'))
            found_user.blocked = True
            found_user.save()

        copy_to_relate = get_object_or_404(Copy, id=validated_data.get('found_copy'))
        copy_to_relate.available = True
        copy_to_relate.save()
        
        instance.save()

        return ...

        
        
    