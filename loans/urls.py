from django.urls import path

from . import views
from loans.views import LoanView, ReturnView

urlpatterns = [
    path("loans/<int:pk>/", LoanView.as_view()),
    path("loans/return/<int:pk>/", ReturnView.as_view()),

]
