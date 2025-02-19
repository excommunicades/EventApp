from datetime import datetime

from django.core.mail import send_mail
from django.conf import settings

from event.models import EventRegistration

class EventRegistrationService:

    """
    Service class for handling event registrations, cancellations, and related email notifications.
    """

    @staticmethod
    def cancel_existing_registration(user, event):

        """
        Cancels an existing registration for the user and sends a cancellation email.
        """

        existing_registration = EventRegistration.objects.filter(user=user, event=event).first()
        
        if existing_registration:
            EventRegistrationService.send_registration_cancellation_email(user, event)
            existing_registration.delete()

        return existing_registration

    @staticmethod
    def create_registration(user, event, validated_data):

        """
        Creates a new event registration for the user.
        """

        validated_data.pop('user', None)
        registration = EventRegistration.objects.create(
            user=user,
            registration_date=datetime.utcnow(),
            **validated_data
        )

        return registration

    @staticmethod
    def send_registration_cancellation_email(user, event):

        """
        Sends an email notification to the user about the cancellation of their event registration.
        """

        subject = f'Registration Cancelled: {event.title}'
        message = f'Hello, {user.username}!\n\nYour registration for the event "{event.title}" has been canceled. The event was scheduled for {event.date}.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)