from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from django.db import connection


# Create your tests here.
User = get_user_model()

class TestAuthentication(APITestCase):
    def setUp(self):
        self.signup_url = '/signup/'
        self.login_url = '/login/'
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
    def test_signup_no_database_connection(self):
        connection.close()
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)


    # LOGIN

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
    def test_login_no_database_connection(self):
        connection.close()
        data = {"username": "newuser", "password": "securepassword123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
