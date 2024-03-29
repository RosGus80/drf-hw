from rest_framework import serializers

from courses.models import Course, Lesson, Subscription
from courses.validators import LessonValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LessonValidator(name='name')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    user_is_subscribed = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_user_is_subscribed(self, obj):
        return Subscription.objects.filter(user=self.context.get('request').user, course=obj).exists()

    class Meta:
        model = Course
        fields = '__all__'
        validators = [LessonValidator(name='name')]


