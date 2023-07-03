from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=50)
    is_colaborator = models.BooleanField(default=False)
    is_student = models.BooleanField(null=True, blank=True, default=True)
    blocked = models.BooleanField(default=False)
