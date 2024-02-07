from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from courses.models import Payment
from users.serializers import PaymentSerializer


# Create your views here.


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['payment_date']
    search_fields = ['course_bought', 'lesson_bought', 'payment_method']

