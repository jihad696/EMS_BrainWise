from django.contrib.auth.models import AbstractUser
from django.db import models

class UserAccount(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
