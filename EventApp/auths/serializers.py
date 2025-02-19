from rest_framework.exceptions import ValidationError
from rest_framework import serializers, generics

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from auths.serializers_utils import (
    UserRegistrationService,
    authenticate_user,
)

class RegistrationSerializer(serializers.ModelSerializer):

    """
    Serializer for user registration, ensuring unique username and email.
    """

    class Meta:

        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }

    def validate_username(self, value):

        UserRegistrationService.validate_username(value)

        return value

    def validate_email(self, value):

        UserRegistrationService.validate_email(value)

        return value

    def create(self, validated_data):

        return UserRegistrationService.create_user(validated_data)


class AuthorizationSerializer(serializers.Serializer):

    """
    Serializer for user authentication, accepting username and password.
    """

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):

        username = attrs.get('username')
        password = attrs.get('password')

        try:

            user = authenticate_user(username, password)
            attrs['user'] = user

        except ValidationError as e:
            raise e

        return attrs
