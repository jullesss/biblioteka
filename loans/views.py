from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import LoanSerializer
from permissions.permissions import IsAdminOrOwner, IsAdminUser
from .models import Loan
from books.models import Book
from django.shortcuts import get_object_or_404

class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_create(self, serializer):
        found_book = self.kwargs.get("pk")
        book = get_object_or_404(Book, pk=found_book)

        serializer.save(book=book, username=self.request.data.get('username'))


""" class LoanRetrieveView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoanDetailsView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_create(self, serializer):
       
        today = int(datetime.now().day)
        print(today)
        return_date = int(loan.return_date.day)
        if today > return_date:
            user.blocked
            return Response(message="User is now blocked",status=status.HTTP_200_OK)
        
        return Response(message="All good, feel free to loan more books ;)",status=status.HTTP_200_OK) """
        
