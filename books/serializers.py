from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    copies_number = serializers.SerializerMethodField()

    class Meta:
        model = Book

        fields = [
            "id",
            "title",
            "author",
            "pages_number",
            "pub_year",
            "pub_by",
            "img_url",
            "description",
            "copies_number",
        ]

    def get_copies_number(self, book):
        return book.book_copies.count()

    def create(self, validated_data) -> Book:
        user = validated_data.pop("user")
        instance_book = Book.objects.create(**validated_data)

        instance_book.users.add(user)
        instance_book.save()
        
        return instance_book

