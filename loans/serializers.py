from rest_framework import serializers
from .models import Loan
from users.models import User
from books.models import Book
from copies.models import Copy
from favorites.models import Favorite
from .exceptions import BlockedError, NoCopyAvailable, NoLoan
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author"]


class CopyBookSerializer(serializers.ModelSerializer):
    book = BookCopySerializer(read_only=True)

    class Meta:
        model = Copy
        fields = ["id", "book"]
        read_only_fields = ["book"]


class UserLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class LoanSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    user = UserLoanSerializer(read_only=True)
    copy = CopyBookSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = [
            "id",
            "copy",
            "loan_date",
            "return_date",
            "user",
            "due_date",
            "username",
        ]
        read_only_fields = ["return_date", "copy", "user", "due_date"]

    def create(self, validated_data: dict) -> Loan:
        username = validated_data.pop("username")
        user = User.objects.filter(username__iexact=username).first()
        the_book = validated_data.get("book")

        if user.blocked:
            raise BlockedError()

        copy_to_relate = Copy.objects.filter(
            available=True, book=the_book
        ).first()

        if not copy_to_relate:
            raise NoCopyAvailable()

        copy_to_relate.available = False
        copy_to_relate.save()

        instance = Loan.objects.create(copy=copy_to_relate, user=user)
        instance.save()

        favorites = Favorite.objects.filter(book=the_book).first()
        all_favs = favorites.book.book_copies.all().filter(available=True).count()

        user_favorited = Favorite.objects.values("user")
        print(user_favorited)
        mail_list = []
        for user in user_favorited:
            the_user = get_object_or_404(User, id=user.get("user"))
            mail_list.append(the_user.email)

        send_mail(
            subject="BiblioteKa - Aviso de cópia",
            message=f'O livro {the_book.title} que você favoritou está com {all_favs} exemplares disponíveis no momento. Aproveite para pegar emprestado!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[mail_list],
            fail_silently=False,
        )

        return instance

    def update(self, instance, validated_data: dict):
        username = validated_data.pop("username")
        user = get_object_or_404(User, username=username)
        copy = validated_data.get("copy")

        instance_loan = Loan.objects.filter(
            copy=copy, user=user, return_date=None
        ).first()

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
