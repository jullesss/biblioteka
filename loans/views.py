from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import LoanSerializer
from permissions.permissions import IsAdminOrOwner, IsAdminUser
from .models import Loan
from users.models import User
from copies.models import Copy
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


class ReturnView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def update(self, request, *args, **kwargs):
        found_copy = self.kwargs.get("pk")
        copy = get_object_or_404(Copy, pk=found_copy)

        username = request.data.pop('username')
        user = User.objects.filter(username__iexact=username).first()

      #  copy_related = Copy.objects.filter(user=user, book=validated_data.get('book')).first()
        print(user)
        print(copy)
        #user_loan = Loan.objects.filter(**{"user_id":user.id, "copy_id":copy.id}).first()

        """ if not user_loan:
            raise NoLoan() """


        serializer = self.get_serializer(copy, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(copy=copy, user=user, username=username, found_copy=found_copy)








"""     def patch(self, request, *args, **kwargs):
        found_book = self.kwargs.get("pk")
        book = get_object_or_404(Book, pk=found_book)

        print('entra na view')
        .save(book=book, username=self.request.data.get('username')) """

"""         loan = self.get_object()
        return_date = request.data.get("return_date")

        if return_date:
            loan.return_date = return_date
            loan.save() """

        
