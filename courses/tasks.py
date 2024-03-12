import smtplib

from celery import shared_task
from django.core.mail import send_mail

from courses.models import Subscription, Course


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
