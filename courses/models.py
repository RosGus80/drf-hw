from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(**NULLABLE, upload_to='previews/')


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(**NULLABLE, upload_to='previews/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

