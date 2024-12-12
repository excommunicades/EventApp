import django_filters
from event.models import Event

class EventFilter(django_filters.FilterSet):

    '''

    FilterSet for filtering events based on various fields like title, location, and date.

    Allows filtering of events using the following fields:

    - title: Filter events by title (case-insensitive partial match).
    - location: Filter events by location (case-insensitive partial match).
    - date: Filter events by an exact date.
    - date_from: Filter events by a start date (greater than or equal to).
    - date_to: Filter events by an end date (less than or equal to).

    '''

    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    date = django_filters.DateFilter(field_name='date', lookup_expr='exact')
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['title', 'location', 'date', 'date_from', 'date_to']