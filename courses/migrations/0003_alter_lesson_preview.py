# Generated by Django 5.0.1 on 2024-01-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='previews/'),
        ),
    ]
