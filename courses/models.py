from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(**NULLABLE, upload_to='previews/')
    owner = models.ForeignKey(User, **NULLABLE, default=None, on_delete=models.CASCADE)
    url = models.URLField(**NULLABLE, default=None)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(**NULLABLE, upload_to='previews/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, **NULLABLE, default=None, on_delete=models.CASCADE)
    url = models.URLField(**NULLABLE, default=None)


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


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Price(models.Model):
    currency = models.CharField(max_length=3)
    unit_amount = models.IntegerField()
    recurring_days = models.IntegerField()
    product_name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.ForeignKey(Price, on_delete=models.CASCADE)