from django.shortcuts import render
from .serializers import FavoriteSerializer
from rest_framework import generics, exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Favorite
from permissions.permissions import IsOwner, IsAdminUser, IsAdminOrOwner
from rest_framework.permissions import IsAuthenticated


class CreateFavoriteView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(book_id=self.kwargs.get("book_id"))

    def perform_create(self, serializer):
        user_id = self.request.user.id
        book_id = self.kwargs.get("book_id")
        exist = Favorite.objects.filter(user_id=user_id, book_id=book_id).first()
        if exist:
            raise exceptions.ValidationError("Book is already favorited.")
        return serializer.save(**{
            "book_id": book_id,
            "user_id": user_id}
            )


class GetAllFavoriteView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user_id=self.request.user.id)


class GetAllFavoriteUserView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return Favorite.objects.filter(user_id=self.kwargs.get("user_id"))


class FavoriteRemoveView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer
    lookup_field = "book_id"

    def get_queryset(self):
        user_id = self.request.user.id
        book_id = self.kwargs.get("book_id")
        return Favorite.objects.filter(user_id=user_id, book_id=book_id)