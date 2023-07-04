from django.urls import path

from . import views
from loans.views import LoanView

urlpatterns = [
    path("loans/<int:pk>/", LoanView.as_view()),
]
