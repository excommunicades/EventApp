from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from django.urls import reverse
from django.contrib.auth.models import User

from event.models import Event, EventRegistration


client = APIClient()

def create_user(username="testuser", password="password"):

    """
    Helper function to create a user.
    """

    return User.objects.create_user(username=username, password=password)

def create_event(organizer):

    """
    Helper function to create an event.
    """

    return Event.objects.create(
        title="Test Event",
        description="Event Description",
        date="2025-12-31",
        location="Test Location",
        organizer=organizer
    )

def create_event_registration(user, event):

    """
    Helper function to create an event registration for a user.
    """

    return EventRegistration.objects.create(
        user=user,
        event=event
    )

def get_access_token(user):

    """
    Helper function to get an access token for a user.
    """

    url = reverse('login-user')
    data = {'username': user.username, 'password': 'password'}
    response = client.post(url, data, format='json')

    return response.data['access_token']

class TestEventViewSet(APITestCase):

    """
    Test case for event-related views such as creating, updating, and deleting events.
    """

    def setUp(self):

        """
        Set up test user, event, and authentication for event tests.
        """

        self.user = create_user()
        self.client.login(username=self.user.username, password="password")
        self.access_token = get_access_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.event = create_event(self.user)

    def test_create_event(self):

        """
        Test event creation with valid data.
        """

        url = reverse('event-list')
        data = {
            'title': "New Event",
            'description': "Event Description",
            'date': "2025-12-31",
            'location': "Test Location",
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_list_events(self):

        """
        Test fetching a list of events.
        """

        url = reverse('event-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_update_event(self):

        """
        Test updating an existing event.
        """

        url = reverse('event-detail', kwargs={'pk': self.event.id})
        data = {
            'title': "Updated Event",
            'description': "Updated Description",
            'date': "2025-12-31",
            'location': "Updated Location"
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_event(self):

        """
        Test deleting an event.
        """

        url = reverse('event-detail', kwargs={'pk': self.event.id})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_event_permission_denied(self):

        """
        Test that a user cannot delete an event they did not create.
        """

        other_user = create_user(username="otheruser")
        self.client.login(username=other_user.username, password="password")

        access_token = get_access_token(other_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        url = reverse('event-detail', kwargs={'pk': self.event.id})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestEventRegistrationViewSet(APITestCase):

    """
    Test case for event registration functionality.
    """

    def setUp(self):

        """
        Set up test user, event, and authentication for event registration tests.
        """

        self.user = create_user()
        self.access_token = get_access_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.event = create_event(self.user)

    def test_create_event_registration(self):

        """
        Test creating an event registration.
        """

        url = reverse('eventregistration-list')
        data = {
            'event': self.event.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['event'], self.event.id)

    def test_list_event_registrations(self):

        """
        Test listing event registrations for a user.
        """

        registration = create_event_registration(self.user, self.event)
        url = reverse('eventregistration-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_event_registration(self):

        """
        Test deleting an event registration.
        """

        registration = create_event_registration(self.user, self.event)
        url = reverse('eventregistration-detail', kwargs={'pk': registration.id})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestEventRegistrantsViewSet(APITestCase):

    """
    Test case for viewing event registrants.
    """

    def setUp(self):

        """
        Set up test user, event, and registration for viewing event registrants.
        """

        self.user = create_user()
        self.access_token = get_access_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.event = create_event(self.user)
        self.registration = create_event_registration(self.user, self.event)

    def test_list_event_registrants(self):

        """
        Test listing registrants for an event.
        """

        url = reverse('event-registrants-list', kwargs={'event_id': self.event.id})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user']['id'], self.user.id)

    def test_no_event_registrants(self):

        """
        Test when an event has no registrants.
        """

        other_event = create_event(self.user)
        url = reverse('event-registrants-list', kwargs={'event_id': other_event.id})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
