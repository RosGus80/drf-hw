# Generated by Django 5.0.1 on 2024-03-08 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_alter_price_str_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='str_id',
            field=models.CharField(default='None', max_length=100, unique=True),
        ),
    ]