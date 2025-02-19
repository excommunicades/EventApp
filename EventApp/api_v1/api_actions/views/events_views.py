from django_filters import rest_framework as filters

from rest_framework import status, viewsets, filters as drf_filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from event.models import (
    Event,
    EventRegistration,
)
from api_v1.api_actions.serializers.events_serializers import (
    EventSerializer,
    EventRegistrationSerializer
)

from api_v1.api_actions.utils.views_utils import EventRegistrationService
from api_v1.api_actions.views.events_filters import EventFilter


from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(summary="Get the list of events"),
    create=extend_schema(summary="Create a new event"),
    retrieve=extend_schema(summary="Get detailed information about an event"),
    update=extend_schema(summary="Update an event"),
    partial_update=extend_schema(summary="Partially update an event"),
    destroy=extend_schema(summary="Delete an event")
)
@extend_schema(tags=["Events"])
class EventViewSet(viewsets.ModelViewSet):

    """
    ViewSet for managing events with filtering, searching, and ordering.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = (drf_filters.OrderingFilter, filters.DjangoFilterBackend, drf_filters.SearchFilter)
    filterset_class = EventFilter
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['date', 'title']
    ordering = ['date']

    my_tags = ['Events']

    def perform_destroy(self, instance):

        user = self.request.user

        if instance.organizer != user:
            raise PermissionDenied("You are not the owner of this event and cannot delete it.")
        
        instance.delete()

    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(
    list=extend_schema(summary="Get the list of event registrations"),
    create=extend_schema(summary="Create a registration for an event"),
    retrieve=extend_schema(summary="Get information about a registration"),
    update=extend_schema(summary="Update registration information"),
    partial_update=extend_schema(summary="Partially update a registration"),
    destroy=extend_schema(summary="Delete a registration")
)
@extend_schema(tags=["Event Registrations"])
class EventRegistrationViewSet(viewsets.ModelViewSet):

    """
    ViewSet for managing event registrations.
    """

    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        user = self.request.user
        event = serializer.validated_data.get('event')
        registration = EventRegistrationService.register_user_for_event(user, event, serializer)
        
        if registration is None:
            return None

    my_tags = ['Event Registrations']


@extend_schema_view(
    list=extend_schema(summary="Get the list of registrants for an event"),
    retrieve=extend_schema(summary="Get information about a registrant")
)
@extend_schema(tags=["Event Registrants"])
class EventRegistrantsViewSet(viewsets.ReadOnlyModelViewSet):

    """
    ViewSet for retrieving registrants of an event.
    """

    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        event_id = self.kwargs['event_id']
        return EventRegistration.objects.filter(event_id=event_id)

    my_tags = ['Event Registrants']
