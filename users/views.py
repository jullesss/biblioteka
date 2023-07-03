from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.serializers import UserSerializer
from rest_framework import generics, permissions


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdmin]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
