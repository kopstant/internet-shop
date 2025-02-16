from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email Address", max_length=254)
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number", unique=True, **NULLABLE)
    country = models.CharField(verbose_name="Country", max_length=254, **NULLABLE)
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Avatar", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
