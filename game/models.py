from django.db import models
from django.contrib.auth.models import AbstractUser

class BankModel(models.Model):
    taken = models.BooleanField(default=False, blank=False)
    ids = models.PositiveIntegerField(default=0, blank=False)
    assets = models.PositiveIntegerField(default=0, blank=False)
    name = models.CharField(max_length=100, blank=False)
    fullName = models.CharField(max_length=100, blank=False)
