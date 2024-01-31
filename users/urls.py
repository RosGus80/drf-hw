from django.urls import path

from users.views import PaymentListAPIView

urlpatterns = [
    path('payments/list', PaymentListAPIView.as_view(), name='payment_list'),
]