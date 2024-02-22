from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(**NULLABLE, upload_to='previews/')
    owner = models.ForeignKey(User, **NULLABLE, default=None, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(**NULLABLE, upload_to='previews/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, **NULLABLE, default=None, on_delete=models.CASCADE)


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

