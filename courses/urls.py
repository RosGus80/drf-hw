from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, \
    CourseUpdateAPIView, CourseDestroyAPIView

app_name = 'courses'

router = DefaultRouter()
# router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/list/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/view/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_view'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('courses/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('courses/list/', CourseListAPIView.as_view(), name='course_list'),
    path('courses/view/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course_view'),
    path('courses/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course_update'),
    path('courses/delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='course_delete'),

] + router.urls
