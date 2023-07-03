from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import LoanSerializer
from permissions.permissions import IsAdminUser
from .models import Loan
from books.models import Book
from users.models import User
from copies.models import Copy
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_create(self, serializer):
        found_book = self.kwargs.get("pk")
        book = get_object_or_404(Book, pk=found_book)

        serializer.save(book=book)

""" class LoanDetailsView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_create(self, serializer):
       
        today = int(datetime.now().day)
        return_date = int(loan.return_date.day)
        if today > return_date:
            user.blocked
            return Response(message="User is now blocked",status=status.HTTP_200_OK)
        
        return Response(message="All good, feel free to loan more books ;)",status=status.HTTP_200_OK) """
        
