import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser
from .serializers import CustomRegisterSerializer


class registrationTestCase(APITestCase):

    # list_url = reverse("/rest-auth/registration/")

    # def test_registration(self):
    #     data = {'username': 'test', 'password1': 'pass@123', 'email': 'test@gmail.com'}
    #     response = self.client.post("/rest-auth/registration/", data)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def setUp(self):
        self.user = CustomUser.objects.create(username="test", password="pass@123", email="test@gmail.com", age="25", place="calicut", contact="1234")
        self.token = Token.objects.create(user=self.user)
        self.api_auth()

    def api_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_User_Auth(self):
        response = self.client.get("/rest-auth/registration/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_User_Un_Auth(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/rest-auth/registration/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
