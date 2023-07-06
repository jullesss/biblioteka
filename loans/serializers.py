from rest_framework import serializers
from .models import Loan
from users.serializers import UserSerializer
from users.models import User
from books.serializers import BookSerializer
from copies.models import Copy
from .exceptions import BlockedError, NoCopyAvailable, NoLoan
from django.shortcuts import get_object_or_404
from datetime import datetime

class CopyBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Copy
        fields = ['id', 'book']
        read_only_fields = ['book']

class LoanSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    user = UserSerializer(read_only=True)
    copy = CopyBookSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'copy', 'loan_date', 'return_date', 'user', 'due_date', 'username']
        read_only_fields = ['return_date', 'copy', 'user', 'due_date']


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
        username = validated_data.pop('username')
        user =  get_object_or_404(User, username=username)
        copy = validated_data.get('copy')

        instance_loan = Loan.objects.filter(copy = copy, user = user, return_date=None).first()

        if not instance_loan:
            raise NoLoan()
        
        instance_loan.return_date = datetime.now()
        instance_loan.save()

        today = datetime.now().day
        due_date = instance_loan.due_date.day

        if today > due_date:
            user.blocked = True
            user.save()

        copy.available = True
        copy.save()

        return instance_loan
    