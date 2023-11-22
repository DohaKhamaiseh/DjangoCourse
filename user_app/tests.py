from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

class RegisterTestCase(APITestCase):
    """
       A class to test the registration process of a user
    """
    
    # Any test function should start with word 'test'
    def test_register(self):
        data ={
            "username": "test1",
            "email": "test@email.com",
            "password": "test123",
            "password2": "test123"
        }
        # reverse use to redirect to the link that the name atrribute value is register, check the urls.py file
        # the line before to send post request with data
        response = self.client.post(reverse('register'),data)
        # here we make sure that the user is created successfully bu compare its status with the expected status
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
class LoginLogoutTestCase(APITestCase):
     """
       A class to test the login and logout as a user
    """
    
     def setUp(self):
         """
         we can't check login process without creating a user first, so we use this function to create user then check
         """
         
         self.user = User.objects.create_user(username="test", password="test123")
    
     def test_login(self):
         # the values in data should be the same as the values that pass through setUp method
        data = {
             "username"  :"test",
             "password":"test123"
         }
        response = self.client.post(reverse('login'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)   
    
     def test_logout(self):
          
         # we can't logout without having the token for that user
         self.token = Token.objects.get(user__username = "test")
         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
         response = self.client.post(reverse('logout'))
         self.assertEqual(response.status_code,status.HTTP_200_OK)