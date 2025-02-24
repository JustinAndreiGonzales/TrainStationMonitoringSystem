from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from django.db import connection, OperationalError
from django.urls import reverse
from unittest.mock import patch

# Create your tests here.
User = get_user_model()

class TestAuthentication(APITestCase):
    def setUp(self):
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.user_data = {
            "username": "rjcsolamo",
            "role": "admin",
            "password": "password"
        }
        User.objects.create_user(**self.user_data)

    # SIGNUP
    # no password
    def test_signup_no_password(self):
        data = self.user_data.copy()
        del data['password']
        response = self.client.post(self.signup_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # no username
    def test_signup_no_username(self):
        data = self.user_data.copy()
        del data['username']
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # username already exists
    def test_signup_username_exists(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # successful
    def test_signup_successful(self):
        data = {
            "username": "newuser",
            "role": "admin",
            "password": "securepassword123"
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # no database connection
    @patch("django.db.connection.ensure_connection", side_effect=OperationalError)
    def test_signup_no_database_connection(self, mock_db):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)


    # LOGIN
    def test_login_registered_user(self):
        data = {
            "username": "newuser",
            "role": "admin",
            "password": "securepassword123"
        }
        response = self.client.post(self.signup_url, data)
        data = {"username": "newuser", "password": "securepassword123"}
        res = self.client.post(self.login_url, data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # non registered user
    def test_login_non_registered_user(self):
        data = {"username": "unknownuser", "password": "somepassword"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # invalid username
    def test_login_invalid_username(self):
        data = {"username": "wronguser", "password": "securepassword123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # invalid password
    def test_login_invalid_password(self):
        data = {"username": "newuser", "password": "wrongpassword"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # no database connection
    @patch("django.db.connection.ensure_connection", side_effect=OperationalError)
    def test_login_no_database_connection(self, mock_db):
        data = {"username": "newuser", "password": "securepassword123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
