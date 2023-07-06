from django.db import models
from datetime import timedelta
from django.utils import timezone
from businessdays import BusinessDay, get_business_day_offset

class Loan(models.Model):        
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_loans"
    )
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="copy_loans"
    )
    loan_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=get_business_day_offset(3))#default=timezone.now()+timedelta(days=3))
    return_date = models.DateTimeField(null=True)



