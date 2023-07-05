from django.urls import path
from . import views
from copies import views as copy_views

urlpatterns = [
    path("books/", views.BookView.as_view()),
  #  path("books/<int:book_id>/", views.BookDetailView.as_view()),
    path("books/<int:book_id>/copies/", copy_views.CopyView.as_view()),
    path("books/<int:book_id>/copies/<int:copy_id>/", copy_views.CopyDetailsView.as_view()),
]