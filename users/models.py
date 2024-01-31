from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course, Lesson

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


class Payment(models.Model):
    CHOICES = [
        ('1', "наличка"),
        ('2', "карта"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)
    course_bought = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    lesson_bought = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE)
    payment_method = models.CharField(max_length=1, choices=CHOICES)
