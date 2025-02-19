"""
URL configuration for EventApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include

from api_v1.api_actions.views.events_views import (
    EventViewSet,
    EventRegistrationViewSet,
    EventRegistrantsViewSet,
)

router = DefaultRouter()

router.register(r'events', EventViewSet, basename='event')
router.register(r'event-registrations', EventRegistrationViewSet, basename='eventregistration')
router.register(r'events/(?P<event_id>\d+)/registrants', EventRegistrantsViewSet, basename='event-registrants')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auths.urls')),
    path('api/v1/', include(router.urls)),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]