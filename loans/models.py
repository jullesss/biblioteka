from django.db import models
from datetime import timedelta
from django.utils import timezone

class Loan(models.Model):        
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_loans"
    )
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="copy_loans"
    )
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=timezone.now()+timedelta(days=3))



