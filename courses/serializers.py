from rest_framework import serializers

from courses.models import Course, Lesson, Subscription, Product, Price
from courses.services import create_session
from courses.validators import LessonValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LessonValidator(url='url')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    user_is_subscribed = serializers.SerializerMethodField()
    session_url = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_session_url(self, obj):
        return create_session(obj.price_id)['url']

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_user_is_subscribed(self, obj):
        return Subscription.objects.filter(user=self.context.get('request').user, course=obj).exists()

    class Meta:
        model = Course
        fields = '__all__'
        validators = [LessonValidator(url='url')]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('str_id', )


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        exclude = ('str_id', 'currency',)

