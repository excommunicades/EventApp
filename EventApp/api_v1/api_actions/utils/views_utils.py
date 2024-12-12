from django.core.mail import send_mail
from django.conf import settings

class EventRegistrationService:

    """
    Service class for handling event registrations and sending confirmation emails.
    """

    @staticmethod
    def register_user_for_event(user, event, serializer):

        """
        Registers a user for an event and sends a confirmation email.
        """

        registration = serializer.save(user=user)
        
        if registration and registration.pk:
            EventRegistrationService.send_registration_email(user, event)
        
        return registration

    @staticmethod
    def send_registration_email(user, event):

        """
        Sends a confirmation email to the user upon successful event registration.
        """

        subject = f'Event Registration Confirmation: {event.title}'
        message = f'Hello, {user.username}!\n\nYou have successfully registered for the event "{event.title}". The event will take place on {event.date}.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]
        
        send_mail(subject, message, from_email, recipient_list)