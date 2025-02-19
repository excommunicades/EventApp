from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from django.urls import path

from auths.views import (
    Register_User,
    Login_User
)


urlpatterns = [
    path('register/', Register_User.as_view(), name='register-user'),
    path('login/', Login_User.as_view(), name='login-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='register-user'),
]
