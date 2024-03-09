from django.shortcuts import render
from rest_framework import viewsets, generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.models import Course, Lesson, Subscription, Product, Price
from courses.paginators import CoursesLessonsPaginator
from courses.permissions import IsModeratorOrOwner, IsOwner
from courses.serializers import CourseSerializer, LessonSerializer, ProductSerializer, PriceSerializer
from courses.services import create_product, product_list, product_retrieve, product_delete, price_create, \
    get_all_prices, create_session
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


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pass
        response = create_product(name=self.request.data.get('name'), description=self.request.data.get('description'))
        stripe_id = response['id']
        new_obj = serializer.save()
        new_obj.str_id = stripe_id
        serializer.save()


class ProductListAPIView(APIView):
    def get(self, request):
        return Response({'products': product_list()})


class ProductRetrieveAPIView(APIView):
    def get(self, request, product_id):
        return Response({'product': product_retrieve(product_id)})


class ProductDeleteAPIView(APIView):
    def delete(self, request, product_id):
        return Response({'deleted:': product_delete(product_id)})


class PriceCreateAPIView(generics.CreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        response = price_create(unit_amount=self.request.data.get('unit_amount')*100, recurring_days=self.request.data.get('recurring_days'), product_id=self.request.data.get('product_id'))
        new_obj = serializer.save()
        new_obj.str_id = response['id']
        new_obj.currency = 'rub'
        serializer.save()


class PriceListAPIView(APIView):
    def get(self, request):
        return Response({'prices': get_all_prices()})


class CreateSessionAPIView(APIView):
    """Принимает аргумент price_id и необязательно - quantity (по умолчанию равно 1)"""
    def post(self, request):
        if request.data.get('quantity') is None:
            return Response({'session': create_session(request.data.get('price_id'))})
        else:
            return Response({'session': create_session(request.data.get('price_id'), request.data.get('quantity'))})

