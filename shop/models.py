from django.db import models
from django.conf import settings
from django.urls import reverse
from .utils import validate_sku
from user_app.models import CustomUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from shop.tasks import send_price_change_notification


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    sku = models.CharField(
        max_length=8, validators=[validate_sku], default="ABC12345", unique=True
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # relation
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])


@receiver(pre_save, sender=Product)
def product_price_updated(sender, instance, **kwargs):
    if instance.pk:
        existing_product = Product.objects.get(pk=instance.pk)
        if existing_product.price != instance.price:
            # Notify other administrators via email
            message = f"The price of product {instance.name} has been updated by {instance.user.username}. New price: {instance.price}."
            notification = Notification.objects.create(message=message)
            notification.recipients.set(CustomUser.objects.filter(administrator=True))
            notification.send_notification(message)


class Notification(models.Model):
    recipients = models.ManyToManyField(CustomUser, related_name="notificaciones")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def send_notification(self, message):
        recipients = [user.email for user in self.recipients.all()]
        send_price_change_notification.delay(message, recipients)
