from django.urls import path

from . import views
from loans.views import LoanView, LoanDetailsView

urlpatterns = [
    path("loans/<int:pk>/", LoanView.as_view()),
    path("loans/<int:pk>/<int:ik>/", LoanDetailsView.as_view()),
]
