import smtplib
import datetime

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import BASE_DIR
from courses.models import Subscription, Course
from users.models import User


@shared_task
def send_mail_course_updated(course_id):
    subscriptions = Subscription.objects.filter(course=Course.objects.get(pk=course_id))
    users = []
    for sub in subscriptions:
        users.append(sub.user.email)

    try:
        send_mail(subject='Курс обновлен',
                  message=f'Курс {Course.objects.get(pk=course_id).name} обновлен',
                  from_email='noreply@gmail.com',
                  recipient_list=users)
    except smtplib.SMTPDataError:
        pass


@shared_task
def block_inactive_users():
    users = User.objects.filter(is_active=True)
    for user in users:
        minimal_allowed_date = datetime.datetime.now() - datetime.timedelta(30)
        aware_date = timezone.make_aware(minimal_allowed_date)
        if user.last_login < aware_date:
            user.is_active = False
            user.save()

