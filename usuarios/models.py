from django.contrib.auth.models import AbstractUser

from django.db import models
from resto.models import Restaurante

class User(AbstractUser):
    is_owner = models.BooleanField(default=False)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurante = models.OneToOneField(Restaurante, on_delete=models.CASCADE, null=True)