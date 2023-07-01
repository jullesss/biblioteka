from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Book
        
        fields = ["id", "title", "author", "pages_number", "pub_year", "pub_by", "img_url", "description"]
