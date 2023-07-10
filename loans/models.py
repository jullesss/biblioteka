from django.db import models
from datetime import timedelta
from django.utils import timezone
import holidays

class Loan(models.Model):        
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_loans"
    )
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="copy_loans"
    )
    loan_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True)
    return_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            holiday_calendar = holidays.BR()
            current_date = timezone.now().date()
            days_count = 0
            while days_count < 3:
                current_date += timedelta(days=1)
                if current_date.weekday() < 5 and current_date not in holiday_calendar:
                    days_count += 1
            self.due_date = timezone.datetime.combine(current_date, timezone.now().time())
        super().save(*args, **kwargs)

