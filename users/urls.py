from django.urls import path
from .views import UserListView, UserCreateView, UserDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/create/", UserCreateView.as_view()),
    path("users/list/", UserListView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
