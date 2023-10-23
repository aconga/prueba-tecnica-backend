import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from shop.models import Product, Category
from user_app.models import CustomUser
from django.core.exceptions import ValidationError
from django.urls import reverse


class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Project", slug="project")
        self.user = CustomUser.objects.create(username="tester")
        self.client = APIClient()

    def test_sku_validation(self):
        # Attempt to create a product with a valid SKU
        valid_product = Product(
            sku="ABC12348",
            name="Sample Product",
            slug="sample-product",
            description="Product Description",
            price=100.0,
            category=self.category,
            user=self.user,
        )
        valid_product.full_clean()
        valid_product.save()
        # Verify that the product is created successfully
        self.assertEqual(Product.objects.count(), 1)

        # Attempt to create a product with an invalid SKU (too long)
        with self.assertRaises(ValidationError) as context:
            invalid_product = Product(
                sku="A" * 51,  # SKU too long (more than 50 characters)
                name="Another product",
                slug="another-product",
                description="Another product description",
                price=100.0,
                category=self.category,
                user=self.user,
            )
            invalid_product.full_clean()

        self.assertIn(
            "'Invalid SKU format. It should be in the format ABC12345.",
            str(context.exception),
        )
