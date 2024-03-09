from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, \
    CourseUpdateAPIView, CourseDestroyAPIView, SubscriptionAPIView, CourseRetrieveModeratorAPIView, \
    SubscriptionRetrieveAPIView, LessonRetrieveModeratorAPIView, ProductCreateAPIView, ProductListAPIView, \
    ProductRetrieveAPIView, ProductDeleteAPIView, PriceCreateAPIView, PriceListAPIView, CreateSessionAPIView

app_name = 'courses'

router = DefaultRouter()
# router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/list/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/view/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_view'),
    path('lesson/view/<int:pk>/owner', LessonRetrieveModeratorAPIView.as_view(), name='lesson_view_owner'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('courses/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('courses/list/', CourseListAPIView.as_view(), name='course_list'),
    path('courses/view/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course_view'),
    path('courses/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course_update'),
    path('courses/delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='course_delete'),
    path('courses/view/<int:pk>/owner', CourseRetrieveModeratorAPIView.as_view(), name='course_view_owner'),

    path('subscribe/', SubscriptionAPIView.as_view(), name='subscribe'),
    path('subscription/view/<int:pk>/', SubscriptionRetrieveAPIView.as_view(), name='subscription view'),

    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/list/', ProductListAPIView.as_view(), name='product_list'),
    path('product/retrieve/<product_id>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/delete/<product_id>/', ProductDeleteAPIView.as_view(), name='product_delete'),

    path('price/create/', PriceCreateAPIView.as_view(), name='price_create'),
    path('price/list', PriceListAPIView.as_view(), name='price_list'),

    path('session/create/', CreateSessionAPIView.as_view(), name='create_session'),
    ] + router.urls
