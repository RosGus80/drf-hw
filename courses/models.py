from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Price(models.Model):
    str_id = models.CharField(max_length=100, default='None', unique=True)
    currency = models.CharField(max_length=3, default='rub')
    unit_amount = models.IntegerField()
    recurring_days = models.IntegerField()
    product_id = models.CharField(max_length=100)


class Product(models.Model):
    str_id = models.CharField(max_length=100, default='', unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(**NULLABLE, upload_to='previews/')
    owner = models.ForeignKey(User, **NULLABLE, default=None, on_delete=models.CASCADE)
    url = models.URLField(**NULLABLE, default=None)
    price_id = models.CharField(max_length=100, default='', **NULLABLE)


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


