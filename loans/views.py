from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import LoanSerializer
from permissions.permissions import IsAdminUser, IsAdminOrReadOnly
from .models import Loan
from copies.models import Copy
from books.models import Book
from django.shortcuts import get_object_or_404

class ListUserLoansView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer

    def get_queryset(self):
        found_user = self.kwargs.get("pk")
        return Loan.objects.filter(user_id=found_user)

class CreateLoanView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_create(self, serializer):
        found_book = self.kwargs.get("pk")
        book = get_object_or_404(Book, pk=found_book)

        serializer.save(book=book, username=self.request.data.get('username'))


class ReturnBookView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_update(self, serializer):
        found_copy = self.kwargs.get("pk")
        copy = get_object_or_404(Copy, pk=found_copy)
        serializer.save(copy=copy)


        
