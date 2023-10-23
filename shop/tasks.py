# tasks.py
from celery import shared_task
from django.conf import settings
from shop.utils import send_email


@shared_task
def send_price_change_notification(message, recipient):
    subject = "Notification: Product Price Change"
    from_email = settings.EMAIL_HOST_USER
    send_email(subject, message, from_email, recipient)
