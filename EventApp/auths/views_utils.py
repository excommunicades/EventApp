from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


def login_user(serializer):

    """
    Authenticates a user and generates JWT tokens.
    """

    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']

    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token

    return Response({
        'access_token': str(access_token),
        'refresh_token': str(refresh_token),
        'user': {
            'username': user.username,
            'nickname': getattr(user, 'nickname', None),
            'pk': user.pk,
            'email': user.email
        }

    }, status=status.HTTP_200_OK)

