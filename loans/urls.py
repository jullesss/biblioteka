from django.urls import path

from loans.views import CreateLoanView, ListUserLoansView, ReturnBookView

urlpatterns = [
    path("loans/book/<int:pk>/", CreateLoanView.as_view()),
    path("loans/user/<int:pk>/", ListUserLoansView.as_view()),
    path("loans/return/copy/<int:pk>/", ReturnBookView.as_view())
]
