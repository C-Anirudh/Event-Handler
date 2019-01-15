from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    roll = models.CharField(max_length=200, null=True, blank=False)
    contact_no = models.IntegerField(max_length=10, null=True, blank=False, default=1234567890)
