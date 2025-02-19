from rest_framework.exceptions import ValidationError, AuthenticationFailed

from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserRegistrationService:
    
    @staticmethod
    def validate_username(username: str):

        # Ensures the username is unique.

        if User.objects.filter(username=username).exists():
            raise ValidationError("User with this username already exists.")
    
    @staticmethod
    def validate_email(email: str):
        
        # Ensures the email is unique.

        if User.objects.filter(email=email).exists():
            raise ValidationError("User with this email already exists.")
    
    @staticmethod
    def create_user(validated_data: dict):

        # Creates a new user with a hashed password.

        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        return user


def authenticate_user(username, password):

    # Validates the username and password, and authenticates the user.

    if not username:
        raise AuthenticationFailed({"username": "This field is required."})

    if not password:
        raise AuthenticationFailed({"password": "This field is required."})

    try:

        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise AuthenticationFailed({"username": "User with this username does not exist."})

    user = authenticate(username=username, password=password)

    if user is None:
        raise AuthenticationFailed({"password": "Invalid username or password."})

    return user
