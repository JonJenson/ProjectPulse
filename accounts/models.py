# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_engineer = models.BooleanField(default=False)
    is_teamleader = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    email = models.EmailField(unique=False)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()