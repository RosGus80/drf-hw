from django.urls import path

from users.views import PaymentListAPIView, UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserListAPIView, \
    UserDestroyAPIView

app_name = 'users'


urlpatterns = [
    path('payments/list', PaymentListAPIView.as_view(), name='payment_list'),
    path('users/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('users/<int:pk>/update', UserUpdateAPIView.as_view(), name='user_update'),
    path('users/<int:pk>/view', UserRetrieveAPIView.as_view(), name='user_view'),
    path('users/list', UserListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/delete', UserDestroyAPIView.as_view()),
]

