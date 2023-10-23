import os
from .base import *

DEBUG = False

ADMINS = [
    ("Abdon Conga", "acongacardenas@gmail.com"),
]

ALLOWED_HOSTS = ["myshoplunna.com", "www.myshoplunna.com"]


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "email-smtp.{region}.amazonaws.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "YOUR_SES_SMTP_USERNAME"
EMAIL_HOST_PASSWORD = "YOUR_SES_SMTP_PASSWORD"
