from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from auths.serializers import RegistrationSerializer
from event.models import (
    Event,
    EventRegistration,
)

from api_v1.api_actions.utils.serializers_utils import EventRegistrationService

class EventSerializer(serializers.ModelSerializer):

    """
    Serializer for creating and updating event objects.
    """

    organizer = RegistrationSerializer(read_only=True)

    class Meta:

        model = Event

        fields = [
            'id',
            'title',
            'description',
            'date',
            'location',
            'organizer',
            ]


    def create(self, validated_data):

        user = self.context['request'].user
        validated_data['organizer'] = user
        event = Event.objects.create(**validated_data)

        return event

    def update(self, instance, validated_data):

        user = self.context['request'].user

        if instance.organizer != user:
            raise PermissionDenied("You are not the owner of this event.")
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance


    def delete(self, instance):

        user = self.context['request'].user
        
        if instance.organizer != user:
            raise PermissionDenied("You are not the owner of this event and cannot delete it.")
        
        instance.delete()
        return None

class EventRegistrationSerializer(serializers.ModelSerializer):

    """
    Serializer for managing event registrations.
    """

    user = RegistrationSerializer(read_only=True)

    class Meta:
        model = EventRegistration
        fields = [
            'event',
            'user',
            'registration_date',
        ]
        read_only_fields = ['user', 'registration_date']

    def create(self, validated_data):

        user = self.context['request'].user
        event = validated_data.get('event')
        existing_registration = EventRegistrationService.cancel_existing_registration(user, event)

        if existing_registration:
            return existing_registration
        
        registration = EventRegistrationService.create_registration(user, event, validated_data)

        return registration