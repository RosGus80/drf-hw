from django.test import TestCase
from rest_framework.reverse import reverse

from courses.models import Course, Subscription, Lesson
from users.models import User
from rest_framework.test import force_authenticate, APIClient
from rest_framework import status


# Create your tests here.


class SubscriptionTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(pk=1, name='test', description='test')
        self.user = User.objects.create(pk=1, email='test@gmail.com')
        self.sub = Subscription.objects.create(pk=1, user_id=1, course_id=1)

    def test_check_subscription(self):
        if Subscription.objects.filter(user=self.user, course=self.course).exists():
            self.assertTrue(True)
        else:
            self.assertFalse(False)

    def test_change_subscription(self):
        force_authenticate(self, user=self.user)
        response = self.client.get('/subscription/view/1')
        if Subscription.objects.filter(user=self.user, course=self.course).exists():
            Subscription.objects.filter(user=self.user, course=self.course).delete()
            self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        else:
            Subscription.objects.create(user=self.user, course=self.course)
            self.assertEqual(response.status_code, status.HTTP_200_OK)


class LessonsTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(pk=1, email='test@gmail.com')
        self.course = Course.objects.create(pk=1, name='test', description='test')
        self.lesson = Lesson.objects.create(pk=3, name='test', description='test', course=self.course)
        self.lesson_owner = Lesson.objects.create(pk=2, name='test_owner', description='test_owner', course=self.course, owner=self.user)

    def test_unauthenticated(self):
        response = self.client.get('/lesson/list/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_list(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('courses:lesson_list'))

        print(response.json())

        self.assertEqual(response.json(),
                         {'count': 2, 'next': None, 'previous': None, 'results': [{'id': 2, 'name': 'test_owner', 'description': 'test_owner', 'preview': None, 'course': 1, 'owner': 1}, {'id': 3, 'name': 'test', 'description': 'test', 'preview': None, 'course': 1, 'owner': None}]}
                    )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('courses:lesson_view', kwargs={'pk': 3}))

        self.assertEqual(response.json(),
                         {'id': 3, 'name': 'test', 'description': 'test', 'preview': None, 'course': 1, 'owner': None})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_rights(self):
        self.client.force_authenticate(user=self.user)
        response_not_owner = self.client.get('/lesson/view/3/owner')
        response_owner = self.client.get('/lesson/view/2/owner')

        self.assertEqual(response_owner.status_code, status.HTTP_200_OK)

        self.assertEqual(response_not_owner.status_code, status.HTTP_403_FORBIDDEN)

    def test_lesson_create(self):
        self.client.force_authenticate(user=self.user)

        data = {'name': 'test1', 'description': 'test1', 'course': 1}

        response = self.client.post('/lesson/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Lesson.objects.count() == 3)


