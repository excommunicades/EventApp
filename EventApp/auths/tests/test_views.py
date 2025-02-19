from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User

class UserRegistrationTestCase(APITestCase):

    """
    Test case for user registration functionality.
    """

    def test_user_registration_successful(self):

        """
        Test successful user registration with valid data.
        """

        url = '/auth/register/'
        data = {
            'username': 'testuser',
            'password': 'password123',
            'email': 'testuser@example.com',
        }
        
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['detail'], 'User successfully registered')
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], 'testuser')

    def test_user_registration_missing_data(self):

        """
        Test user registration with missing data (username only).
        """

        url = '/auth/register/'
        data = {
            'username': 'testuser',
        }
        
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UserLoginTestCase(APITestCase):

    """
    Test case for user login functionality.
    """

    def setUp(self):

        """
        Set up a test user for login tests.
        """

        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com'
        )

    def test_user_login_successful(self):

        """
        Test successful login with correct username and password.
        """

        url = '/auth/login/'
        data = {
            'username': 'testuser',
            'password': 'password123',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)

    def test_user_login_invalid_credentials(self):

        """
        Test login with invalid credentials (wrong password).
        """

        url = '/auth/login/'
        data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
