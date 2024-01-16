from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = None

    name = models.CharField(max_length=100, verbose_name='name')
    surname = models.CharField(max_length=100, verbose_name='surname')
    email = models.EmailField(unique=True, verbose_name='email')
    phone_number = models.CharField(max_length=15, verbose_name='phone_number', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


