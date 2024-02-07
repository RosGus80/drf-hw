from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True, **NULLABLE)
    photo = models.ImageField(upload_to='previews/', **NULLABLE)
    city = models.CharField(max_length=100, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

