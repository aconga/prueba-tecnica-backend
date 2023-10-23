from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from user_app.models import CustomUser
from django.urls import reverse


class UserCreateAPITestCase(TestCase):
    def setUp(self):
        # Create an admin user for testing
        self.admin_user = CustomUser.objects.create_user(
            username="admin", password="adminpassword", administrator=True
        )

        self.client = APIClient()
        refresh = RefreshToken.for_user(self.admin_user)
        self.token = str(refresh.access_token)

    def test_creacion_usuario_administrator(self):
        # Configure the authorization header with the JWT token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        nuevo_usuario_data = {
            "username": "nuevousuario",
            "email": "nuevousuario@email.com",
            "password": "nuevousuariopassword",
            "administrator": False,
        }

        response = self.client.post(
            reverse("user-create"), nuevo_usuario_data, format="json"
        )

        # Verify that the request is successful and returns code 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the user was created correctly in the database
        self.assertTrue(CustomUser.objects.filter(username="nuevousuario").exists())

    def test_creacion_usuario_no_administrator(self):
        # Create a non-administrator user for testing
        non_admin_user = CustomUser.objects.create_user(
            username="nonadmin", password="nonadminpassword", administrator=False
        )

        refresh = RefreshToken.for_user(non_admin_user)
        non_admin_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {non_admin_token}")

        nuevo_usuario_data = {
            "username": "nuevousuario",
            "password": "nuevousuariopassword",
            "administrator": False,
        }

        # Make a POST request to create a new user
        response = self.client.post(
            reverse("user-create"), nuevo_usuario_data, format="json"
        )

        # Verifies that the request is denied and returns code 403 (forbidden)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Verify that the user has not been created in the database
        self.assertFalse(CustomUser.objects.filter(username="nuevousuario").exists())
