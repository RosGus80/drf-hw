from django.urls import path

from users.views import PaymentListAPIView

app_name = 'users'

urlpatterns = [
    path('payments/list', PaymentListAPIView.as_view(), name='payment_list'),
]