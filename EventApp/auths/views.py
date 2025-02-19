from rest_framework import generics, status
from rest_framework.response import Response

from django.contrib.auth.models import User

from auths.serializers import (
    RegistrationSerializer,
    AuthorizationSerializer,
)

from auths.views_utils import login_user


class Register_User(generics.CreateAPIView):

    # Endpoint for user registration.

    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):

        response = super().create(request, *args, **kwargs)
        return Response({
            'detail': 'User successfully registered',
            'user': response.data
        }, status=status.HTTP_201_CREATED)


class Login_User(generics.GenericAPIView):

    # Endpoint for user authentication.

    serializer_class = AuthorizationSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        return login_user(serializer=serializer)