from django.shortcuts import render
from .serializers import CopySerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Copy
from permissions.permissions import IsAdminOrReadOnly, IsAdminOrOwner


class CopyView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        return serializer.save(book_id=self.kwargs.get("pk"))


class CopyDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]
    queryset = Copy.objects.all()
    lookup_url_kwarg = "book_id"
