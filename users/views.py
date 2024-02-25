from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from courses.models import Payment
from courses.paginators import CoursesLessonsPaginator
from users.models import User
from users.permissions import IsModerator, IsUserOrModerator
from users.serializers import PaymentSerializer, UserSerializer


# Create your views here.


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['payment_date']
    search_fields = ['course_bought', 'lesson_bought', 'payment_method']


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsModerator]
    pagination_class = CoursesLessonsPaginator


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserOrModerator]


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserOrModerator]


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUserOrModerator]


