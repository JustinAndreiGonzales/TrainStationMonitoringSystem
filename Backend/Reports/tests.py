from rest_framework.test import APITestCase
from rest_framework import status
from  django.urls import reverse
from unittest.mock import patch
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from .models import Reports

# Create your tests here.

User = get_user_model()

class TestReportsView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="",
            password=""
        )
        cls.token = Token.objects.create(user=cls.user)

        # TODO: create reports

        cls.url = reverse('reports')

    # Successful reports retrieval
    def test_reports_retrieval(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token (self.token)"
        )
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # requesting additional reports
    def test_additional_reports_retrieval(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token (self.token)"
        )
        response = self.client.get(self.url, {"limit": 3, "offset": 3})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # TODO: No database connections

    # unauthenticated access
    def test_unauthenticated_access(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
