from django.urls import path
from . import views
from favorites import views as fav_views

urlpatterns = [
    path("fav/<int:book_id>/", fav_views.CreateFavoriteView.as_view()),
    path("fav/remove/<int:book_id>/", fav_views.FavoriteRemoveView.as_view()),
    path("fav/user/<int:user_id>/", fav_views.GetAllFavoriteUserView.as_view()),
    path("fav/", fav_views.GetAllFavoriteView.as_view()),
]


