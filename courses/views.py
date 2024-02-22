from django.shortcuts import render
from rest_framework import viewsets, generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.models import Course, Lesson, Subscription
from courses.paginators import CoursesLessonsPaginator
from courses.permissions import IsModeratorOrOwner, IsOwner
from courses.serializers import CourseSerializer, LessonSerializer
from courses.validators import LessonValidator


# Create your views here.


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CoursesLessonsPaginator


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseRetrieveModeratorAPIView(generics.RetrieveAPIView):
    """Вьюшка для просмотра от лица владельца или модератора"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]


class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]


class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all().order_by('id')
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CoursesLessonsPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonRetrieveModeratorAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionAPIView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            raise serializers.ValidationError('Only authenticated users are allowed')
        elif not Course.objects.filter(pk=request.data.get('course_id')).exists():
            raise serializers.ValidationError('Course does not exist')
        else:
            if Subscription.objects.filter(user=request.user,
                                           course=Course.objects.get(pk=request.data.get('course_id'))).exists():
                Subscription.objects.filter(user=request.user,
                                            course=Course.objects.get(pk=request.data.get('course_id'))).delete()
                return Response({'message': 'Unsubscribed successfully'})
            else:
                Subscription.objects.create(user=request.user,
                                            course=Course.objects.get(pk=request.data.get('course_id')))
                return Response({'message': 'Subscribed successfully'})


class SubscriptionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]