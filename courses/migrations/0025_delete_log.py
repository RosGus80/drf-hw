# Generated by Django 5.0.1 on 2024-03-14 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_log'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Log',
        ),
    ]