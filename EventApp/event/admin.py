from django.contrib import admin
from django.contrib.auth.models import User
from .models import Event, EventRegistration

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'location', 'organizer')
    list_filter = ('date', 'organizer')
    search_fields = ('title', 'description', 'location')
    ordering = ('date',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'date', 'location', 'organizer')
        }),
    )

    def save_model(self, request, obj, form, change):

        if not obj.organizer:
            obj.organizer = request.user
        super().save_model(request, obj, form, change)

class EventRegistrationAdmin(admin.ModelAdmin):

    list_display = ('event', 'user', 'registration_date')
    list_filter = ('event', 'user')
    search_fields = ('user__username', 'event__title')

    fieldsets = (
        (None, {
            'fields': ('event', 'user', 'registration_date')
        }),
    )

admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)