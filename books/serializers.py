from rest_framework import serializers
from .models import Book
from copies.models import Copy


class BookSerializer(serializers.ModelSerializer):
    copies_number = serializers.SerializerMethodField()
    copies_quantity = serializers.IntegerField(required=False)

    class Meta:
        model = Book

        fields = [
            "id",
            "title",
            "author",
            "pages_number",
            "publication_year",
            "published_by",
            "img_url",
            "description",
            "copies_number",
            "copies_quantity"
        ]
        extra_kwargs = {
            "copies_quantity": {"write_only": True}
        }

    def get_copies_number(self, book):
        return book.book_copies.count()

    def create(self, validated_data) -> Book:
        copies_quantity =validated_data.pop('copies_quantity')

        user = validated_data.pop("user")
        instance_book = Book.objects.create(**validated_data)

        if copies_quantity:
            for i in range(copies_quantity):
                Copy.objects.create(book=instance_book)

        instance_book.users.add(user)
        instance_book.save()
        
        return instance_book

