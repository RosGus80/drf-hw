import os

import requests
import stripe
from django.conf import settings
from rest_framework import validators

from courses.models import Product, Price


def create_product(name, description):
    stripe.api_key = os.getenv('STRIPE_API_KEY')
    response = stripe.Product.create(name=name, description=description)
    return response


def product_list():
    """Получает продукты из страйпа, а не из бд,
    поэтому желательно сделать метод, чистящий страйп от несуществующих в бд продуктов"""
    stripe.api_key = os.getenv('STRIPE_API_KEY')
    response = stripe.Product.list()
    return response


def product_retrieve(product_id):
    stripe.api_key = os.getenv('STRIPE_API_KEY')
    response = stripe.Product.retrieve(product_id)
    return response


def product_update(product_id, update_dict):
    stripe.api_key = os.getenv('STRIPE_API_KEY')
    stripe.Product.update(product_id, update_dict)


def product_delete(product_id):
    stripe.api_key = os.getenv('STRIPE_API_KEY')
    response = stripe.Product.delete(product_id)
    return response


def price_create(unit_amount, product_id, recurring_days=0):
    """В поле recurring_days нужно передать целое число дней.
    Если подписка оплачивается ежедневно - 1, еженедельно - 7, ежемесячно - 30, ежегодно - 365.
    Передавайте 0, если платеж единичный"""
    stripe.api_key = os.getenv('STRIPE_API_KEY')
    recurring = {}
    if recurring_days == 365:
        recurring = {'interval': 'year'}
    elif recurring_days == 30:
        recurring = {'interval': 'month'}
    elif recurring_days == 7:
        recurring = {'interval': 'week'}
    elif recurring_days == 1:
        recurring = {'interval': 'day'}
    elif recurring_days == 0:
        recurring = {}
    else:
        raise validators.ValidationError('Invalid recurring_days value')
    response = stripe.Price.create(
        currency="rub",
        unit_amount=unit_amount,
        recurring=recurring,
        product_data={"name": Product.objects.get(str_id=product_id).name})
    return response


def get_all_prices():
    """Получает цены из страйпа, а не из бд,
        поэтому желательно сделать метод, чистящий страйп от несуществующих в бд цен"""
    stripe.api_key = os.getenv('STRIPE_API_KEY')
    output = stripe.Price.list(limit=200)
    return output


def create_session(price_id: str, quantity=1):
    stripe.api_key = os.getenv('STRIPE_API_KEY')
    response = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price_id, "quantity": quantity}],
        mode="payment",
    )
    return response

