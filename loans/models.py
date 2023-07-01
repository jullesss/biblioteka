from django.db import models
from datetime import datetime, timedelta
import holidays

holidays_list = holidays.Brazil()

def get_next_business_day(date, holidays_list):
    next_day = date + timedelta(days=1)
    while not is_business_day(next_day, holidays_list):
        next_day += timedelta(days=1)
    return next_day

def is_business_day(date, holidays_list):
    return date.weekday() < 5 and date not in holidays_list

current_date = datetime.now()
return_date = get_next_business_day(current_date, holidays_list)

class ReturnModel:

    def returning_date(self):
        self.data_futura = get_next_business_day(datetime.now(), holidays_list)
        return self.data_futura.strftime("%d/%m/%Y")
    
class Loan(models.Model):        

    user_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_loan"
    )
    copy_id = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="copy_loan"
    )
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = ReturnModel.returning_date(self=ReturnModel)



