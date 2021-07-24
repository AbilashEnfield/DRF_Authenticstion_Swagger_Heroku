from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.IntegerField(default=None, blank=True, null=True)
    place = models.CharField(max_length=50,  blank=True, null=True, default=None)
    contact = models.BigIntegerField(default=None, blank=True, null=True)
