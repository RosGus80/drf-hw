from django.contrib import admin

from courses.models import Product, Price


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('str_id', 'name')


@admin.register(Price)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('str_id', 'unit_amount')


