# Generated by Django 5.0.1 on 2024-03-09 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_lesson_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='product',
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.price'),
        ),
    ]
