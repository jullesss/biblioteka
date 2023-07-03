from django.urls import path

from . import views
from copies import views as copy_views

urlpatterns = [
    path("book/<int:book_id>/copies/", copy_views.CopyView.as_view()),
    path("book/<int:book_id>/copies/<int:copy_id>/", copy_views.CopyDetailsView.as_view()),
]